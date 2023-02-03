from django.db.models import CharField, BooleanField, ForeignKey, CASCADE
from django.urls import reverse

from netbox.models import NetBoxModel
from ocp_project_plugin.choices import AppEnvironmentClusterEnvChoices, AppEnvironmentDeploymentKindChoices
from ocp_project_plugin.fields import MemoryResourceField
from ocp_project_plugin.models import OCPProject
from ocp_project_plugin.utils.gitlab import clone_repo


class AppEnvironment(NetBoxModel):
    cluster_env = CharField(
        max_length=3,
        choices=AppEnvironmentClusterEnvChoices,
        default=AppEnvironmentClusterEnvChoices.CHOICE_TST,
        verbose_name="Cluster ENV",
        help_text="The Cluster Environment",
    )
    app_env = CharField(
        max_length=20,
        verbose_name="App ENV",
        help_text="The app Env String used for creating the namespace e.g. tst",
    )
    deployment_kind = CharField(
        max_length=20,
        choices=AppEnvironmentDeploymentKindChoices,
        default=AppEnvironmentDeploymentKindChoices.DEPLOYMENT_KIND_NORMAL,
        verbose_name="Deployment Kind",
        help_text="Choose the way how the deployment should work",
    )
    mtls = BooleanField(
        default=False,
        blank=False,
        verbose_name="MTLS",
        help_text="Enable if mtls should be used",
    )
    repo = CharField(
        max_length=255,
        verbose_name="Git Repository",
        help_text="Path of git Repository, don't forget the .git at the end e.g. "
                  "https://gitlab.com/example/example-deployment-manifests.git",
    )
    branch = CharField(
        max_length=20,
        verbose_name="Git Branch",
        help_text="The git Branch of the Repository e.g. main"
    )
    access_token = CharField(
        blank=True,
        max_length=100,
        verbose_name="Git Access Token",
        help_text="The access token of the tst git repo, int & prd are automatically provided"
    )
    path = CharField(
        max_length=100,
        verbose_name="Git Path",
        help_text="Path of the deployment files e.g. overlays/tst"
    )
    egress_ip = CharField(
        max_length=20,
    )
    monitoring = BooleanField(
        default=True,
        verbose_name="Monitoring",
        help_text="Enable if monitoring should be used",
    )
    postgres_monitoring = BooleanField(
        default=False,
        verbose_name="Postgres Monitoring",
        help_text="Enable if postgres monitoring should be used",
    )
    requests_cpu = CharField(
        max_length=5,
        blank=True,
        verbose_name="CPU request",
        help_text="The CPU request value e.g. 1",
    )
    requests_memory = MemoryResourceField(
        #max_length=5,
        blank=True,
        verbose_name="Memory request",
        help_text="The memory value e.g. 200Mi",
    )
    limits_cpu = CharField(
        max_length=5,
        blank=True,
        verbose_name="CPU Limit",
        help_text="The CPU request value e.g. 2",
    )
    limits_memory = MemoryResourceField(
        #max_length=5,
        blank=True,
        verbose_name="Memory Limit",
        help_text="The CPU memory value e.g. 400Mi",
    )
    ocp_project = ForeignKey(OCPProject, on_delete=CASCADE, related_name="app_env_ocp_project")

    clone_fields = ["access_token", "cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "deployment_kind",
                    "monitoring", "postgres_monitoring", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    class Meta:
        ordering = ["access_token", "cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "deployment_kind",
                    "monitoring", "postgres_monitoring", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    def __str__(self):
        return f"{self.cluster_env}-{self.app_env} ({self.repo}-{self.branch})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:appenvironment", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/AppEnvironment/'

    def save(self, *args, **kwargs):
        clone_repo()
        super(AppEnvironment, self).save(*args, **kwargs)
