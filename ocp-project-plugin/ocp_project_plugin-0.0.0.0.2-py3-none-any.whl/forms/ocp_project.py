from django.core.validators import MinValueValidator
from django.forms import (
    CharField,
    FloatField, BooleanField,
)

from netbox.forms import (
    NetBoxModelBulkEditForm,
    NetBoxModelFilterSetForm,
    NetBoxModelImportForm,
    NetBoxModelForm,
)
from utilities.forms import (
    CSVModelChoiceField,
    DynamicModelChoiceField,
)

from ocp_project_plugin.models import AppEnvironment, OCPProject


class OCPProjectForm(NetBoxModelForm):
    """Form for creating a new App Environment object."""
    name = CharField(
        label="OCP Project Name",
        help_text="The ocp project name e.g. web-shop",
    )
    description = BooleanField(
        label="Description",
        help_text="The description of the project e.g. A web shop software",
    )
    display_name = CharField(
        label="Display name",
        help_text="Display Name of the project e.g. Web Shop Shopify"
    )
    owner = CharField(
        label="Owner",
        help_text="Choose the tenant"
    )
    contact = CharField(
        label="Contact E-Mail",
        help_text="Write the e-mail of the contact e.g. ana.meier@domain.com"
    )
    customer = CharField(
        label="Customer name",
        help_text="Choose the tenant"
    )
    url = BooleanField(
        label="URL",
        help_text="The url of the project documentation",
    )
    workload = BooleanField(
        label="Workload",
        help_text="The workload contents e.g. Postgres DB, nginx",
    )
    request = BooleanField(
        label="Jira Request",
        help_text="The jira request id e.g. TICKET1234",
    )

    class Meta:
        model = OCPProject

        fields = ["name", "description", "display_name", "owner", "contact", "customer", "url", "workload", "request"]


class OCPProjectFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering App Environment instances."""

    model = AppEnvironment

    name = CharField(
        required=False,
        label="OCP Project Name",
        help_text="The ocp project name e.g. web-shop",
    )
    description = BooleanField(
        required=False,
        label="Description",
        help_text="The description of the project e.g. A web shop software",
    )
    display_name = CharField(
        required=False,
        label="Display name",
        help_text="Display Name of the project e.g. Web Shop Shopify"
    )
    owner = CharField(
        required=False,
        label="Owner",
        help_text="Choose the tenant"
    )
    contact = CharField(
        required=False,
        label="Contact E-Mail",
        help_text="Write the e-mail of the contact e.g. ana.meier@domain.com"
    )
    customer = CharField(
        required=False,
        label="Customer name",
        help_text="Choose the tenant"
    )
    url = BooleanField(
        required=False,
        label="URL",
        help_text="The url of the project documentation",
    )
    workload = BooleanField(
        required=False,
        label="Workload",
        help_text="The workload contents e.g. Postgres DB, nginx",
    )
    request = BooleanField(
        required=False,
        label="Jira Request",
        help_text="The jira request id e.g. TICKET1234",
    )


class OCPProjectImportForm(NetBoxModelImportForm):
    name = CharField(
        label="OCP Project Name",
        help_text="The ocp project name e.g. web-shop",
    )
    description = BooleanField(
        label="Description",
        help_text="The description of the project e.g. A web shop software",
    )
    display_name = CharField(
        label="Display name",
        help_text="Display Name of the project e.g. Web Shop Shopify"
    )
    owner = CharField(
        label="Owner",
        help_text="Choose the tenant"
    )
    contact = CharField(
        label="Contact E-Mail",
        help_text="Write the e-mail of the contact e.g. ana.meier@domain.com"
    )
    customer = CharField(
        label="Customer name",
        help_text="Choose the tenant"
    )
    url = BooleanField(
        label="URL",
        help_text="The url of the project documentation",
    )
    workload = BooleanField(
        label="Workload",
        help_text="The workload contents e.g. Postgres DB, nginx",
    )
    request = BooleanField(
        label="Jira Request",
        help_text="The jira request id e.g. TICKET1234",
    )

    class Meta:
        model = AppEnvironment

        fields = ["name", "description", "display_name", "owner", "contact", "customer", "url", "workload", "request"]


class OCPProjectBulkEditForm(NetBoxModelBulkEditForm):
    model = AppEnvironment

    name = CharField(
        required=False,
        label="OCP Project Name",
        help_text="The ocp project name e.g. web-shop",
    )
    description = BooleanField(
        required=False,
        label="Description",
        help_text="The description of the project e.g. A web shop software",
    )
    display_name = CharField(
        required=False,
        label="Display name",
        help_text="Display Name of the project e.g. Web Shop Shopify"
    )
    owner = CharField(
        required=False,
        label="Owner",
        help_text="Choose the tenant"
    )
    contact = CharField(
        required=False,
        label="Contact E-Mail",
        help_text="Write the e-mail of the contact e.g. ana.meier@domain.com"
    )
    customer = CharField(
        required=False,
        label="Customer name",
        help_text="Choose the tenant"
    )
    url = BooleanField(
        required=False,
        label="URL",
        help_text="The url of the project documentation",
    )
    workload = BooleanField(
        required=False,
        label="Workload",
        help_text="The workload contents e.g. Postgres DB, nginx",
    )
    request = BooleanField(
        required=False,
        label="Jira Request",
        help_text="The jira request id e.g. TICKET1234",
    )
