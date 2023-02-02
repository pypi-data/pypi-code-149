from django.db import migrations, models
import utilities.json


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name="OCPProject",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("display_name", models.CharField(max_length=255)),
                ("owner", models.CharField(max_length=255)),
                ("contact", models.CharField(max_length=255)),
                ("customer", models.CharField(max_length=255)),
                ("url", models.CharField(max_length=255)),
                ("workload", models.CharField(max_length=255)),
                ("request", models.CharField(max_length=255))
            ],
            options={
                "ordering": ("name", "description", "display_name", "owner", "contact", "customer", "url", "workload",
                             "request"),
            },
        ),
        migrations.CreateModel(
            name="AppEnvironment",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app_env", models.CharField(max_length=20)),
                ("mtls", models.BooleanField()),
                ("repo", models.CharField(max_length=255)),
                ("branch", models.CharField(max_length=20)),
                ("path", models.CharField(max_length=20)),
                ("egress_ip", models.CharField(max_length=20)),
                ("helm", models.BooleanField()),
                ("monitoring", models.BooleanField()),
                ("postgres_monitoring", models.BooleanField()),
                ("kustomize", models.BooleanField()),
                ("ocp_project",
                 models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="app_env_ocp_project",
                                   to="ocp_project_plugin.OCPProject")),
            ],
            options={
                "ordering": ("app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                             "postgres_monitoring", "kustomize", "ocp_project"),
            },
        ),
        migrations.CreateModel(
            name="ResourceQuota",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("requests_cpu", models.CharField(max_length=5)),
                ("requests_memory", models.CharField(max_length=5)),
                ("limits_cpu", models.CharField(max_length=5)),
                ("limits_memory", models.CharField(max_length=5)),
                ("app_environment",
                 models.OneToOneField(on_delete=models.deletion.CASCADE, to="ocp_project_plugin.AppEnvironment")),
            ],
            options={
                "ordering": ("requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"),
            },
        ),
    ]
