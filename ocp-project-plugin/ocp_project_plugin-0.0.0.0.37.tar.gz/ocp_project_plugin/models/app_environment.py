from django.db.models import CharField, BooleanField, ForeignKey, CASCADE
from django.urls import reverse

from netbox.models import NetBoxModel
from ocp_project_plugin.choices import AppEnvironmentClusterEnvChoices
from ocp_project_plugin.models import OCPProject


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
    mtls = BooleanField()
    repo = CharField(
        max_length=255,
    )
    branch = CharField(
        max_length=20,
    )
    path = CharField(
        max_length=100,
    )
    egress_ip = CharField(
        max_length=20,
    )
    helm = BooleanField(
        default=False,
        blank=False,
        verbose_name="HELM",
        help_text="Enable if helm should be used",
    )
    monitoring = BooleanField(
        default=False
    )
    postgres_monitoring = BooleanField(
        default=False
    )
    kustomize = BooleanField(
        default=False
    )
    requests_cpu = CharField(
        max_length=5,
        blank=False
    )
    requests_memory = CharField(
        max_length=5,
        blank=False
    )
    limits_cpu = CharField(
        max_length=5,
        blank=False
    )
    limits_memory = CharField(
        max_length=5,
        blank=False
    )
    ocp_project = ForeignKey(OCPProject, on_delete=CASCADE, related_name="app_env_ocp_project")

    clone_fields = ["cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                    "postgres_monitoring", "kustomize", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    class Meta:
        ordering = ["cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                    "postgres_monitoring", "kustomize", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    def __str__(self):
        return f"{self.cluster_env}-{self.app_env} ({self.repo}-{self.branch})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:appenvironment", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/AppEnvironment/'

