from __future__ import annotations

import os
from typing import Optional, List, Dict, TYPE_CHECKING

from aws_cdk import (
    Tags,
    Duration,
    aws_ec2 as _ec2,
    aws_ecs as _ecs,
    aws_ecr as _ecr,
    aws_logs as _logs,
    aws_ecr_assets as _ecr_assets,
    aws_elasticloadbalancingv2 as _elb,
    aws_route53 as _route53,
    aws_cloudwatch as _cloudwatch,
)
from constructs import Construct

from aws_cdk_constructs.efs.volume import EFSVolume

if TYPE_CHECKING:
    from .cluster import ECSCluster


class ECSMicroservice(Construct):
    """Represents a microservice in a ECS cluster, this class aggregates all AWS entities that will become a FargateService and TaskDefinition

    Args:
        scope (Construct): Parent construct

        name (str): logical id of the new created service

        image (Optional|str): ECR docker image, it must be uploaded to the account ECR registry

        dockerfile_path (Optional|str): ECR Dockerfile directory path

        cluster (ECSCluster): ECSCluster entity where the microservice will be deployed.

        image_tag (str): tag of the ECR hosted docker image, defaults to "master".

        container_env (Dict): A dictionary that will be injected on the running containers as environment variables.

        cpu (int): Number of CPU units to be allocated to the container, see (https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_aws-ecs.FargateTaskDefinition.html#cpu) for valid cpu/mem values combination.

        memory_limit_mib (int): The hard limit (in MiB) of memory to present to the container, see (https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_aws-ecs.FargateTaskDefinition.html#memorylimitmib) for valid cpu/mem values combination.

        entry_point (List): The entry point that is passed to the container, see (https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_aws-ecs.ContainerDefinition.html#entrypoint) for more details.

        port (int): The port number on the container that is bound to the user-specified or automatically assigned host port.

        health_check_path (str): The path to the container health check, defaults to "/".

        desired_count (int): The number of instances of the task definition to place and keep running, defaults to 1.

        max_count (int): The maximum number of instances of the task definition to place and keep running, defaults to None.

        min_count (int): The minimum number of instances of the task definition to place and keep running, defaults to 1.

        cpu_threshold (int): The target value for the average CPU utilization across an application, defaults to 50.

        security_group (aws_ec2.SecurityGroup): Security group to attach to the service, if None a dedicated SG will be created.

        sends_emails (bool): If the service sends emails, defaults to False.

        healthy_threshold_count (int): The number of consecutive health checks successes required before considering an unhealthy target healthy, defaults to 2.

        unhealthy_threshold_count (int): The number of consecutive health check failures required before considering the target unhealthy, defaults to 2.

        health_check_interval (int): The approximate amount of time, in seconds, between health checks of an individual target, defaults to 30.

        health_check_timeout (int): The amount of time, in seconds, during which no response means a failed health check, defaults to 5.

        internal (bool): When set to true the ms won't be registered in the Alb target group

    """

    def __init__(
            self,
            scope: Construct,
            name: str,
            cluster: ECSCluster,
            dockerfile_path: str = None,
            image: str = None,
            image_tag: str = "master",
            container_env: dict = None,
            cpu: int = 256,
            memory_limit_mib: int = 512,
            entry_point: list = None,
            port: int = 80,
            health_check_path: str = "/",
            desired_count: int = 1,
            max_count: int = None,
            min_count: int = None,
            cpu_threshold: int = None,
            security_group: _ec2.SecurityGroup = None,
            sends_emails: bool = False,
            healthy_threshold_count: int = 2,
            unhealthy_threshold_count: int = 2,
            health_check_interval: int = 30,
            health_check_timeout: int = 5,
            internal: bool = False
    ) -> None:
        self.scope = scope
        self.id = name
        self.dockerfile_path = dockerfile_path
        self.image = image
        self.image_tag = image_tag
        self.container_env = container_env
        self.cpu = cpu
        self.memory_limit_mib = memory_limit_mib
        self.entry_point = entry_point
        self.vpc = cluster.vpc
        self.cluster = cluster
        self.port = port
        self.health_check_path = health_check_path
        self.hostname = f"{self.id}-{self.cluster.app_name}.{self.cluster.domain_name}"
        self.cname: Optional[_route53.CnameRecord] = None
        self.desired_count = desired_count
        self.max_count = max_count
        self.min_count = min_count
        self.cpu_threshold = cpu_threshold
        self.environments_parameters = self.cluster.environments_parameters
        self.environment = self.cluster.environment

        super().__init__(scope, name)

        # Create a dedicated SG if none is provided
        self.security_groups: List[_ec2.ISecurityGroup] = []
        if not security_group:
            self.security_group = self._create_sg()
        else:
            self.security_group = security_group

        self.security_groups.append(self.security_group)

        # Requirement to send emails is to have the SMTP SG attached to the service

        if sends_emails:
            smtp_relay_sg_id = self.cluster.aws_account.get(
                "smtp_relay_security_group"
            )
            smtp_relay_sg = _ec2.SecurityGroup.from_security_group_id(
                scope=scope,
                id=f"{self.id}_smtp-access-sg",
                security_group_id=smtp_relay_sg_id,
                mutable=False,
            )
            self.security_groups.append(smtp_relay_sg)

        self.task = self._create_task()
        self.main_container = self._create_main_container()
        self.service = self._create_service()

        # It will attach services to the LB listener and route them by hostname
        if self.cluster.alb is not None and internal is False:
            lb_target_priority = self.cluster.target_priority + 1
            self.cluster.target_priority = lb_target_priority
            self.target_group = self.cluster.alb.listener.add_targets(
                self.id,
                port=self.port,
                targets=[self.service],
                priority=lb_target_priority,
                protocol=_elb.ApplicationProtocol.HTTP,
                health_check=_elb.HealthCheck(
                    port=str(self.port),
                    path=self.health_check_path,
                    healthy_threshold_count=healthy_threshold_count,
                    unhealthy_threshold_count=unhealthy_threshold_count,
                    interval=Duration.seconds(health_check_interval),
                    timeout=Duration.seconds(health_check_timeout),
                ),
                conditions=[
                    _elb.ListenerCondition.host_headers(
                        [f"{self.id}-{self.cluster.app_name}.{self.cluster.domain_name}"]
                    )
                ],

            )
            self.cluster.alb.security_group.add_ingress_rule(
                peer=self.security_group,
                connection=_ec2.Port.all_traffic(),
                description="Allow ALB to access the service",
            )

        if self.cluster.hosted_zone:
            self.create_cname(self.cluster.hosted_zone)

        if self.max_count and self.min_count and self.cpu_threshold:
            self.scalable_target = self._create_autoscaling()
            if self.scalable_target:
                self.scalable_target.scale_on_cpu_utilization(
                    "CpuScaling", target_utilization_percent=self.cpu_threshold
                )

        self.create_desired_count_tag()
        if self.min_count:
            self.create_min_count_tag()
        self.create_scheduler_tag()

        cluster.register_ms(self)

    def _create_sg(self) -> _ec2.SecurityGroup:
        """Default SG creation for the service"""
        return _ec2.SecurityGroup(
            scope=self.scope,
            id=self.id + "-sg",
            vpc=self.vpc,
            allow_all_outbound=True,
        )

    def _create_task(self) -> _ecs.FargateTaskDefinition:
        """Create the task definition

        :returns: aws_ecs.FargateTaskDefinition object
        """
        return _ecs.FargateTaskDefinition(
            scope=self.scope,
            id=self.id + "-task",
            cpu=self.cpu,
            memory_limit_mib=self.memory_limit_mib,
        )

    def _create_main_container(self) -> _ecs.ContainerDefinition:
        """Create the main container for the service,  based on the ECR image and attaches it to the task definition

        :returns: aws_ecs.ContainerDefinition object
        """
        if self.image:
            image = _ecs.ContainerImage.from_ecr_repository(
                _ecr.Repository.from_repository_name(
                    scope=self.scope, id=self.id + "-ecr-repo", repository_name=self.image
                ),
                self.image_tag,
            )
        else:
            image = _ecs.ContainerImage.from_docker_image_asset(_ecr_assets.DockerImageAsset(self, f'{self.id}-main-image',
                directory=self.dockerfile_path
            ))

        return self.task.add_container(
            id=self.id + "-main-container",
            image=image,
            port_mappings=[_ecs.PortMapping(container_port=self.port)],
            logging=_ecs.LogDriver.aws_logs(
                stream_prefix=self.id + "-main-container",
                log_retention=_logs.RetentionDays.ONE_WEEK,
            ),
            environment=self.container_env,
            entry_point=self.entry_point,
        )

    def _create_autoscaling(self) -> Optional[_ecs.ScalableTaskCount]:
        """Create the autoscaling settings for the service, if there's a max_number of replicas"""
        if self.max_count:
            return self.service.auto_scale_task_count(
                min_capacity=self.min_count,
                max_capacity=self.max_count,
            )
        return None

    def _create_service(self) -> _ecs.FargateService:
        """Creates the Fargate Service"""
        return _ecs.FargateService(
            scope=self.scope,
            id=self.id + "-srv",
            task_definition=self.task,
            security_groups=self.security_groups,
            cluster=self.cluster.cluster,
            enable_execute_command=True,
            desired_count=self.desired_count,
            propagate_tags=_ecs.PropagatedTagSource.SERVICE,
        )

    def attach_volume(self, name: str, mount_point: str) -> EFSVolume:
        """Public method to create and attach an EFS volume to the containers

        :param name: Name of the volume
        :param mount_point: Mount point of the volume
        :returns: EFSVolume object
        """
        volume = EFSVolume(
            self.scope, id=name, vpc=self.vpc, volume_mount_path=mount_point, environment=self.environment,
            environments_parameters=self.environments_parameters, app_name=self.cluster.app_name)
        volume.grant_access(self.security_group)
        self.task.node.add_dependency(volume)
        self.task.add_volume(name=volume.id, efs_volume_configuration=volume.efs_volume_configuration)
        self.main_container.add_mount_points(volume.get_mount_point())
        return volume

    def add_init_container(
            self, name: str, volume: EFSVolume, dockerfile_path: str
    ) -> None:
        """Public method to add an init container to the service, init container will be created based on a Dockerfile
        present on the provided path, it can have a Volume attached to populate init values before attaching it to the main
        container. There's a dependency between the init container and the main container, so the later one will not start
        until the init finished successfully

        :param name: Name of the init container
        :param volume: EFSVolume object to attach to the init container
        :param dockerfile_path: Path to the Dockerfile to build the init container
        """
        init_container_image = _ecr_assets.DockerImageAsset(
            scope=self.scope,
            id=f"{self.id}-{self.id}-{name}-icontainer-image",
            directory=os.getcwd() + dockerfile_path,
        )

        init_container = self.task.add_container(
            id=f"{self.id}-{name}-init-container",
            image=_ecs.ContainerImage.from_docker_image_asset(init_container_image),
            essential=False,
            logging=_ecs.LogDriver.aws_logs(
                stream_prefix=f"{self.id}-{name}-init-container",
                log_retention=_logs.RetentionDays.ONE_WEEK,
            ),
        )

        init_container.node.add_dependency(volume)
        self.main_container.add_container_dependencies(
            _ecs.ContainerDependency(
                container=init_container,
                condition=_ecs.ContainerDependencyCondition.SUCCESS,
            )
        )
        init_container_mount_point = _ecs.MountPoint(
            read_only=False, container_path="/dst_dir", source_volume=volume.id
        )
        init_container.add_mount_points(init_container_mount_point)

    def create_cname(self, zone: _route53.IHostedZone) -> None:
        """Public method to create a CNAME record for the service, it will have the format <service_name>.<domain_name>
        and it will point to the lb address
        :param zone: Route53 Hosted Zone object
        """
        self.cname = _route53.CnameRecord(
            scope=self.scope,
            id=f"{self.id}-cname",
            zone=zone,
            record_name=f"{self.id}-{self.cluster.app_name}",
            domain_name=f"{self.cluster.alb.alb.load_balancer_dns_name}"
        )

    def create_desired_count_tag(self) -> None:
        """Public method to create the desired count tag for the service"""
        Tags.of(self.service).add(
            key="SchedulerDesiredCount", value=str(self.desired_count)
        )

    def create_min_count_tag(self) -> None:
        """Public method to create the min count tag in case of autoscaling"""
        Tags.of(self.service).add(
            key="SchedulerDesiredCount", value=str(self.min_count)
        )

    def create_scheduler_tag(self, disabled: bool = False) -> None:
        Tags.of(self.service).add(key="SchedulerUptime", value="8:00-20:00")
        if disabled:
            Tags.of(self.service).add(key="SchedulerSkip", value="true")


    def create_widgets(self) -> None:
        running_container_count = _cloudwatch.Metric(
            metric_name="RunningTaskCount",
            namespace="ECS/ContainerInsights",
            dimensions_map={
                "ClusterName": self.cluster.cluster.cluster_name,
                "ServiceName": self.service.service_name,
            },
            period=Duration.minutes(5),
            statistic="Average",
        )

        desired_container_count = _cloudwatch.Metric(
            metric_name="DesiredTaskCount",
            color="#98df8a",
            namespace="ECS/ContainerInsights",
            dimensions_map={
                "ClusterName": self.cluster.cluster.cluster_name,
                "ServiceName": self.service.service_name,
            },
            period=Duration.minutes(5),
            statistic="Average",
        )

        left_annotations = (
            [
                _cloudwatch.HorizontalAnnotation(
                    label="Min count", value=self.min_count, color="#98df8a"
                ),
                _cloudwatch.HorizontalAnnotation(
                    label="Max count", value=self.max_count, color="#ff9896"
                ),
            ]
            if (self.min_count and self.max_count)
            else []
        )
        if self.cluster.dashboard:
            self.cluster.dashboard.add_widgets(
                _cloudwatch.GraphWidget(
                    title=f"{self.id} - CPU",
                    left=[
                        _cloudwatch.Metric(
                            metric_name="CpuUtilized",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster.cluster_name,
                                "ServiceName": self.service.service_name,
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                        ),
                        _cloudwatch.Metric(
                            metric_name="CpuReserved",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster.cluster_name,
                                "ServiceName": self.service.service_name,
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                        ),
                    ],
                ),
                _cloudwatch.GraphWidget(
                    title=f"{self.id} - Memory",
                    left=[
                        _cloudwatch.Metric(
                            metric_name="MemoryUtilized",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster.cluster_name,
                                "ServiceName": self.service.service_name,
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                        ),
                        _cloudwatch.Metric(
                            metric_name="MemoryReserved",
                            namespace="ECS/ContainerInsights",
                            dimensions_map={
                                "ClusterName": self.cluster.cluster.cluster_name,
                                "ServiceName": self.service.service_name,
                            },
                            period=Duration.minutes(5),
                            statistic="Average",
                        ),
                    ],
                ),
                _cloudwatch.GraphWidget(
                    title=f"{self.id} - Running containers",
                    left=[running_container_count, desired_container_count],
                    left_annotations=left_annotations,
                ),
            )