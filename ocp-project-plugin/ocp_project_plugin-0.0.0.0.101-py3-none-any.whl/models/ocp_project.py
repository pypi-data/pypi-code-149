from django.db.models import CharField, ForeignKey, PROTECT
from django.urls import reverse

from netbox.models import NetBoxModel


class OCPProject(NetBoxModel):
    name = CharField(
        max_length=255,
    )
    description = CharField(
        max_length=255,
    )
    display_name = CharField(
        max_length=255,
    )
    owner = ForeignKey(
        to='tenancy.Contact',
        on_delete=PROTECT,
        related_name='ocp_project_owner',
    )
    contact = ForeignKey(
        to='tenancy.Contact',
        on_delete=PROTECT,
        related_name='ocp_project_contact',
    )
    customer = ForeignKey(
        to='tenancy.Tenant',
        on_delete=PROTECT,
        related_name='ocp_project_tenant',
    )
    docu_url = CharField(
        max_length=255,
    )
    workload = CharField(
        max_length=255,
    )
    request = CharField(
        max_length=255,
    )

    clone_fields = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload",
                    "request"]

    class Meta:
        ordering = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload",
                    "request"]

    def __str__(self):
        return f"{self.name} ({self.display_name}-{self.customer})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:ocpproject", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/OCPProject/'

    def export_yaml_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'displayName': self.display_name,
            'customer': self.customer,
            'owner': self.owner,
            'contact': self.contact,
            'workloads': self.workload,
            'request': self.request,
            'url': self.docu_url
        }
