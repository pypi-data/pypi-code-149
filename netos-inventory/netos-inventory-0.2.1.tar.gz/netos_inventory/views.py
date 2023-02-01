from collections import defaultdict
from extras.models.models import JournalEntry, JournalEntryKindChoices
from ipam.models.fhrp import FHRPGroup
from ipam.models.ip import ASN, IPAddress, Prefix
from ipam.models.vlans import VLAN
from ipam.models.vrfs import VRF
from dcim.models.cables import Cable
from dcim.models.device_components import Interface
from dcim.models.devices import Device, Module
from netbox.views.generic.base import BaseMultiObjectView
from wireless.models import WirelessLAN
from utilities.views import GetReturnURLMixin
from netbox.views import generic
from . import forms, models, tables, filtersets
from django.db.models import F, Q, Case, When, FloatField
from django.db.models.lookups import GreaterThan
from django.db.models.functions import Cast, Round
from django.db.models.functions import JSONObject
import logging
from django.contrib import messages
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import transaction
from django.db.models import ManyToManyField, Count

from django.db.models.fields.reverse_related import ManyToManyRel
from django.shortcuts import redirect, render

from extras.signals import clear_webhooks
from utilities.exceptions import AbortRequest, PermissionsViolation
from utilities.forms import restrict_form_fields

from utilities.permissions import get_permission_for_model
from utilities.views import GetReturnURLMixin
from netbox.views.generic.base import BaseMultiObjectView

from django.conf import settings
from django.db.models import BooleanField, ExpressionWrapper, Q
import datetime as dt


config = settings.PLUGINS_CONFIG["netos_inventory"]

EXCLUDE_Q = {
    "custom_field_data__Netos_Last_Polled": None
}

INTERFACE_UP_Q = Count('interfaces', filter=Q(interfaces__enabled=True))
INTERFACE_DOWN_Q = Count('interfaces', filter=Q(interfaces__enabled=False))


class BulkReconView(GetReturnURLMixin, BaseMultiObjectView):
    """
    Reconcile objects in bulk.

    Attributes:
        filterset: FilterSet to apply when deleting by QuerySet
        table: The table used to display devices being deleted
        recon_fields: The mapping of detected to standard fields
    """
    template_name = 'netos_inventory/bulk_recon.html'
    filterset = None
    table = None
    recon_fields = {}
    status_field_name = None
    queryset = models.ReconDevice.objects.all()

    def get_required_permission(self):
        return get_permission_for_model(self.queryset.model, 'delete')

    def _update_objects(self, form, request):
        logger = logging.getLogger('netos_inventory.views.BulkReconView')
        custom_fields = getattr(form, 'custom_fields', [])
        standard_fields = [
            field for field in form.fields if field not in list(custom_fields) + ['pk']
        ]
        nullified_fields = request.POST.getlist('_nullify')
        updated_objects = []

        for obj in self.queryset.filter(pk__in=form.cleaned_data['pk']):
            journal_data = []
            # Take a snapshot of change-logged models
            if hasattr(obj, 'snapshot'):
                obj.snapshot()

            # Update standard fields. If a field is listed in _nullify, delete its value.
            for name in standard_fields:

                try:
                    model_field = self.queryset.model._meta.get_field(name)
                except FieldDoesNotExist:
                    # This form field is used to modify a field rather than set its value directly
                    model_field = None

                # Handle nullification
                if name in form.nullable_fields and name in nullified_fields:
                    if isinstance(model_field, ManyToManyField):
                        getattr(obj, name).set([])
                    else:
                        setattr(obj, name, None if model_field.null else '')

                # ManyToManyFields
                elif isinstance(model_field, (ManyToManyField, ManyToManyRel)):
                    if form.cleaned_data[name]:
                        getattr(obj, name).set(form.cleaned_data[name])
                # Normal fields
                elif name in form.changed_data:
                    setattr(obj, name, form.cleaned_data[name])

                # Copy data from recon custom fields to model
                elif name in self.recon_fields and self.recon_fields[name]:
                    logger.info(f"Processing {name} field in recon view")
                    recon_field = self.recon_fields[name]
                    recon_custom_fields = list(obj.get_custom_fields().keys())
                    recon_field_name = [
                        el for el in recon_custom_fields if el.name.lower() == recon_field.lower()]
                    # Update only when detected field has value
                    if recon_field_name:
                        recon_field_key = recon_field_name[0]
                        recon_field_val = obj.get_custom_fields()[
                            recon_field_key]
                        current_value = getattr(obj, name)
                        # Don't update if value didn't change and is empty
                        if recon_field_val != current_value and current_value:
                            journal_data.append(
                                f"Changed {name} from {current_value} to {recon_field_val}")
                            setattr(obj, name, recon_field_val)
                        elif not current_value:
                            messages.warning(request, f"Skipped {name} because it's empty")

            # Update custom fields
            for name in custom_fields:

                assert name.startswith('cf_')
                cf_name = name[3:]  # Strip cf_ prefix

                if name in form.nullable_fields and name in nullified_fields:
                    obj.custom_field_data[cf_name] = None
                elif name in form.changed_data:
                    obj.custom_field_data[cf_name] = form.fields[name].prepare_value(
                        form.cleaned_data[name])

                elif cf_name in self.recon_fields and self.recon_fields[cf_name]:
                    # Copy custom detected field
                    logger.info(
                        f"Processing {cf_name} custom field in recon view")
                    recon_field = self.recon_fields[cf_name]
                    recon_custom_fields = list(obj.get_custom_fields().keys())
                    recon_det_field_name = [
                        el for el in recon_custom_fields if el.name.lower() == recon_field.lower()]
                    recon_field_name = [
                        el for el in recon_custom_fields if el.name.lower() == cf_name.lower()
                    ]
                    if recon_det_field_name and recon_field_name:
                        recon_det_field_name = recon_det_field_name[0]
                        recon_field_name = recon_field_name[0]

                        recon_field_val = obj.get_custom_fields()[
                            recon_det_field_name]

                        current_value = obj.get_custom_fields()[
                            recon_field_name]
                        # Don't update if value didn't change and is empty
                        if recon_field_val != current_value and current_value:
                            journal_data.append(
                                f"Changed {cf_name} from {current_value} to {recon_field_val}")
                            obj.custom_field_data[cf_name] = recon_field_val
                        elif not current_value:
                            messages.warning(request, f"Skipped {cf_name} because it's empty")

            obj.full_clean()
            obj.save()
            updated_objects.append(obj)

            # Add/remove tags
            if form.cleaned_data.get('add_tags', None):
                obj.tags.add(*form.cleaned_data['add_tags'])
            if form.cleaned_data.get('remove_tags', None):
                obj.tags.remove(*form.cleaned_data['remove_tags'])

            # Add journal entry
            entries = (JournalEntry(
                created_by=request.user,
                assigned_object=obj,
                kind=JournalEntryKindChoices.KIND_INFO,
                comments="<br>".join(journal_data)
            ),)
            JournalEntry.objects.bulk_create(entries)
        return updated_objects

    #
    # Request handlers
    #
    def get(self, request):
        return redirect(self.get_return_url(request))

    def post(self, request, **kwargs):
        logger = logging.getLogger('netbox.views.BulkEditView')
        model = self.queryset.model

        # If we are editing *all* objects in the queryset, replace the PK list with all matched objects.
        if request.POST.get('_all') and self.filterset is not None:
            pk_list = self.filterset(
                request.GET, self.queryset.values_list('pk', flat=True)).qs
        else:
            pk_list = request.POST.getlist('pk')

        # Include the PK list as initial data for the form
        initial_data = {'pk': pk_list}

        # Check for other contextual data needed for the form. We avoid passing all of request.GET because the
        # filter values will conflict with the bulk edit form fields.
        # TODO: Find a better way to accomplish this
        if 'device' in request.GET:
            initial_data['device'] = request.GET.get('device')
        elif 'device_type' in request.GET:
            initial_data['device_type'] = request.GET.get('device_type')
        elif 'virtual_machine' in request.GET:
            initial_data['virtual_machine'] = request.GET.get(
                'virtual_machine')

        if '_confirm' in request.POST:
            form = self.form(request.POST, initial=initial_data)
            restrict_form_fields(form, request.user)

            if form.is_valid():
                logger.debug("Form validation was successful")

                try:

                    with transaction.atomic():
                        updated_objects = self._update_objects(form, request)

                        # Enforce object-level permissions
                        object_count = self.queryset.filter(
                            pk__in=[obj.pk for obj in updated_objects]).count()
                        if object_count != len(updated_objects):
                            raise PermissionsViolation

                    if updated_objects:
                        msg = f'Updated {len(updated_objects)} {model._meta.verbose_name_plural}'
                        logger.info(msg)
                        messages.success(self.request, msg)

                    return redirect(self.get_return_url(request))

                except ValidationError as e:
                    messages.error(self.request, ", ".join(e.messages))
                    clear_webhooks.send(sender=self)

                except (AbortRequest, PermissionsViolation) as e:
                    logger.debug(e.message)
                    form.add_error(None, e.message)
                    clear_webhooks.send(sender=self)

            else:
                logger.debug("Form validation failed")

        else:
            form = self.form(initial=initial_data)
            restrict_form_fields(form, request.user)

        # Retrieve objects being edited
        table = self.table(self.queryset.filter(
            pk__in=pk_list), orderable=False)
        if not table.rows:
            messages.warning(request, "No {} were selected.".format(
                model._meta.verbose_name_plural))
            return redirect(self.get_return_url(request))

        return render(request, self.template_name, {
            'model': model,
            'form': form,
            'table': table,
            'return_url': self.get_return_url(request),
            **self.get_extra_context(request),
        })


class ReconObjectListView(generic.ObjectListView):
    def get_extra_context(self, request):
        # Device.objects.filter(name='device 3').values('site').annotate(scount=Count('site'))
        recon = {}
        model = self.queryset.model
        all_count = model.objects.count()
        recon["all"] = all_count
        for k, v in self.recon_fields.items():
            if "Netos" in k:
                json_k = f"custom_field_data__{k}"
            else:
                json_k = k
            count = model.objects.filter(
                custom_field_data__contains=JSONObject(**{v: F(json_k)})).count()
            recon[k] = count

        all_fields = {wrap_custom_field(
            k): v for k, v in self.recon_fields.items()}

        detected_fields = [f for f in list(all_fields.values())]
        detected_keys = [f for f in list(all_fields.keys())]

        all_eq_q = {k: F(v) for k, v in zip(detected_fields, detected_keys)}
        # NOTE: this can be splited to separete views to imporove performance
        # TODO: works only for device
        # Query site
        site_field = 'site'
        site_name_field = "site__name"
        region_field = 'site__region'
        region_name_field = "site__region__name"

        if hasattr(model, 'device'):
            site_field = f"device__{site_field}"
            site_name_field = f"device__{site_name_field}"
            region_field = f"device__{region_field}"
            region_name_field = f"device__{region_name_field}"

        all_site_groups = model.objects.values(
            site_field, site_name_field).annotate(site_count=Count('*'))
        site_groups = model.objects.filter(custom_field_data__contains=JSONObject(
            **all_eq_q)).values(site_field).annotate(site_count=Count('*'))
        # Query region
        all_region_groups = model.objects.values(
            region_field, region_name_field).annotate(region_count=Count('*'))
        region_groups = model.objects.filter(custom_field_data__contains=JSONObject(
            **all_eq_q)).values(region_field).annotate(region_count=Count('*'))

        logger = logging.getLogger(__name__)

        sites = {}
        for r in all_site_groups:
            sites[r[site_field] or ""] = [
                r[site_name_field], r["site_count"], 0]
        # fill reconciled items in sites
        for r in site_groups:
            cur_site = sites[r[site_field] or ""]
            cur_site[2] = r["site_count"]
            sites[r[site_field] or ""] = cur_site

        regions = {}
        for r in all_region_groups:
            regions[r[region_field] or ""] = [
                r[region_name_field] or "", r["region_count"], 0]
        for r in region_groups:
            cur_region = regions[r[region_field] or ""]
            cur_region[2] = r["region_count"]
            regions[r[region_field] or ""] = cur_region

        return {"recon_report": recon, "regions": regions, "sites": sites}


DEVICE_MATCH_Q = models.ReconDevice.objects.annotate(
    serial_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
            **{'Netos_Detected_Serial_Number': F('serial')})),
        output_field=BooleanField()
    )).annotate(device_type_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
                **{'Netos_Detected_Type': F('device_type')})),
        output_field=BooleanField()
    )).annotate(netos_software_kickstart_version_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
                **{'Netos_Software_Kickstart_Version': F('custom_field_data__Netos_Detected_Software_Kickstart_Version')})),
        output_field=BooleanField()
    )).annotate(netos_software_version_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
                **{'Netos_Detected_Software_Version': F('custom_field_data__Netos_Software_Version')})),
        output_field=BooleanField()
    )).annotate(netos_hostname_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
                **{'Netos_Hostname': F('custom_field_data__Netos_Detected_Hostname')})),
        output_field=BooleanField()
    )).all()


class ReconDeviceView(generic.ObjectView):
    queryset = DEVICE_MATCH_Q


class ReconDeviceBulkReconView(BulkReconView):
    recon_fields = config["device_recon_fields"].copy()

    queryset = DEVICE_MATCH_Q
    filterset = filtersets.ReconDeviceFilterSet
    table = tables.ReconDeviceTable
    form = forms.ReconDeviceBulkEditForm
    default_return_url = 'plugins:netos_inventory:recondevice_list'


def wrap_custom_field(field):
    if "Netos" in field:
        return f"custom_field_data__{field}"
    return field


class ReconDeviceListView(ReconObjectListView):
    recon_fields = config["device_recon_fields"].copy()

    template_name = 'netos_inventory/object_list_recon.html'

    all_fields = [(wrap_custom_field(k), v) for k, v in recon_fields.items()]

    detected_fields = [k for k, _ in all_fields]
    detected_keys = [v for _, v in all_fields]

    # remove empty fields, all should be update so check first one
    recon_field_none = f"custom_field_data__{recon_fields['device_type']}"
    filter_dict = {recon_field_none: None}

    # remove recon fields with equal values, comapre it in dict
    conditions = JSONObject(**{v: F(k)
                            for k, v in zip(detected_fields, detected_keys)})

    queryset = DEVICE_MATCH_Q

    table = tables.ReconDeviceTable
    filterset = filtersets.ReconDeviceFilterSet
    filterset_form = forms.ReconDeviceFilterForm
    actions = ('import', 'export', 'bulk_recon')


class ReconDeviceEditView(generic.ObjectEditView):
    queryset = models.ReconDevice.objects.all()
    form = forms.ReconDeviceEditForm


class ReconDeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.ReconDevice.objects.all()

##
# Module Recon
##


MODULE_MATCH_Q = models.ReconModule.objects.annotate(
    serial_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
            **{'Netos_Detected_Serial_Number': F('serial')})),
        output_field=BooleanField()
    )).all()


class ReconModuleView(generic.ObjectView):
    queryset = MODULE_MATCH_Q


class ReconModuleBulkReconView(BulkReconView):
    recon_fields = config["module_recon_fields"].copy()

    queryset = MODULE_MATCH_Q
    filterset = filtersets.ReconModuleFilterSet
    table = tables.ReconModuleTable
    form = forms.ReconModuleBulkEditForm
    default_return_url = 'plugins:netos_inventory:reconmodule_list'


class ReconModuleListView(ReconObjectListView):
    recon_fields = config["module_recon_fields"].copy()

    template_name = 'netos_inventory/object_list_recon.html'
    detected_fields = [f for f in list(recon_fields.values())]
    detected_keys = [f for f in list(recon_fields.keys())]
    recon_field_none = f"custom_field_data__{detected_fields[0]}"
    filter_dict = {recon_field_none: None}

    json_query = {k: F(v) for k, v in zip(detected_fields, detected_keys)}
    queryset = MODULE_MATCH_Q
    # .exclude(custom_field_data__contains=JSONObject(**json_query))
    table = tables.ReconModuleTable
    filterset = filtersets.ReconModuleFilterSet
    filterset_form = forms.ReconModuleFilterForm
    actions = ('import', 'export', 'bulk_recon')


class ReconModuleEditView(generic.ObjectEditView):
    queryset = models.ReconModule.objects.all()
    form = forms.ReconModuleEditForm


class ReconModuleDeleteView(generic.ObjectDeleteView):
    queryset = models.ReconModule.objects.all()


##
# Inventory Item Recon
##
INVENTORY_MATCH_Q = models.ReconInventoryItem.objects.annotate(
    serial_match=ExpressionWrapper(
        Q(custom_field_data__contains=JSONObject(
            **{'Netos_Detected_Serial_Number': F('serial')})),
        output_field=BooleanField()
    )).all()


class ReconInventoryItemView(generic.ObjectView):
    queryset = INVENTORY_MATCH_Q


class ReconInventoryItemBulkReconView(BulkReconView):
    recon_fields = config["inventory_recon_fields"].copy()

    queryset = INVENTORY_MATCH_Q
    filterset = filtersets.ReconInventoryItemFilterSet
    table = tables.ReconInventoryItemTable
    form = forms.ReconInventoryItemBulkEditForm
    default_return_url = 'plugins:netos_inventory:reconinventoryitem_list'


class ReconInventoryItemListView(ReconObjectListView):
    recon_fields = config["inventory_recon_fields"].copy()

    template_name = 'netos_inventory/object_list_recon.html'
    detected_fields = [f for f in list(recon_fields.values())]
    detected_keys = [f for f in list(recon_fields.keys())]
    recon_field_none = f"custom_field_data__{detected_fields[0]}"
    filter_dict = {recon_field_none: None}

    json_query = {k: F(v) for k, v in zip(detected_fields, detected_keys)}
    queryset = INVENTORY_MATCH_Q

    table = tables.ReconInventoryItemTable
    filterset = filtersets.ReconInventoryItemFilterSet
    filterset_form = forms.ReconInventoryItemFilterForm
    actions = ('import', 'export', 'bulk_recon')


class ReconInventoryItemEditView(generic.ObjectEditView):
    queryset = models.ReconInventoryItem.objects.all()
    form = forms.ReconInventoryItemEditForm


class ReconInventoryItemDeleteView(generic.ObjectDeleteView):
    queryset = models.ReconInventoryItem.objects.all()

##
# Logical Last Detected
##


class LogicalObjectListView(generic.ObjectListView):
    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        weeks = (4, 3, 2, 1, 0)

        models = [
            VRF,
            VLAN,
            FHRPGroup,
            ASN,
            IPAddress,
            Prefix,
            WirelessLAN,
        ]
        model_stats = {}
        for model in models:
            last_polled = []
            for week in weeks:
                curr_date = dt.datetime.now()
                date_diff = dt.timedelta(days=week * 7)
                curr_date = curr_date - date_diff

                last_polled.append(Count('custom_field_data__Netos_Last_Polled',
                                         filter=Q(custom_field_data__Netos_Last_Polled__gt="") & Q(custom_field_data__Netos_Last_Polled__lte=curr_date.strftime("%Y-%m-%d"))))

            query = (model.objects.aggregate(
                four_weeks=last_polled[0],
                three_weeks=last_polled[1],
                two_weeks=last_polled[2],
                one_weeks=last_polled[3],
                zero_weeks=last_polled[4]
            ))
            model_stats[model.__name__] = ";".join(map(str, [query["four_weeks"],
                                                             query["three_weeks"] -
                                                             query["four_weeks"],
                                                             query["two_weeks"] -
                                                             query["three_weeks"],
                                                             query["one_weeks"] -
                                                             query["two_weeks"],
                                                             query["zero_weeks"] - query["one_weeks"]]))
        extra_content["last_polled"] = model_stats

        return extra_content


class VRFDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.VRFDetectedTable
    queryset = models.VRFDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.VRFDetectedFilterSet
    filterset_form = forms.VRFDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'vrf-detected'
        return extra_content


class VRFDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VRFDetected.objects.all()
    filterset = filtersets.VRFDetectedFilterSet
    table = tables.VRFDetectedTable


class VRFDetectedBulkEditView(generic.BulkEditView):
    queryset = models.VRFDetected.objects.all()
    filterset = filtersets.VRFDetectedFilterSet
    table = tables.VRFDetectedTable
    form = forms.VRFDetectedBulkEditForm


class VLANDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.VLANDetectedTable
    queryset = models.VLANDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.VLANDetectedFilterSet
    filterset_form = forms.VLANDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'vlan-detected'
        return extra_content


class VLANDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VLANDetected.objects.all()
    filterset = filtersets.VLANDetectedFilterSet
    table = tables.VLANDetectedTable


class VLANDetectedBulkEditView(generic.BulkEditView):
    queryset = models.VLANDetected.objects.all()
    filterset = filtersets.VLANDetectedFilterSet
    table = tables.VLANDetectedTable
    form = forms.VLANDetectedBulkEditForm


class FHRPGroupDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.FHRPGroupDetectedTable
    queryset = models.FHRPGroupDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.FHRPGroupDetectedFilterSet
    filterset_form = forms.FHRPGroupDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'fhrp-group-detected'
        return extra_content


class FHRPGroupDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.FHRPGroupDetected.objects.all()
    filterset = filtersets.FHRPGroupDetectedFilterSet
    table = tables.FHRPGroupDetectedTable


class FHRPGroupDetectedBulkEditView(generic.BulkEditView):
    queryset = models.FHRPGroupDetected.objects.all()
    filterset = filtersets.FHRPGroupDetectedFilterSet
    table = tables.FHRPGroupDetectedTable
    form = forms.FHRPGroupDetectedBulkEditForm


class ASNDetectedListView(LogicalObjectListView):
    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.ASNDetectedTable
    queryset = models.ASNDetected.objects.all()
    filterset = filtersets.ASNDetectedFilterSet
    filterset_form = forms.ASNDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'asn-detected'
        return extra_content


class ASNDetectedBulkDeleteView(generic.BulkDeleteView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    queryset = models.ASNDetected.objects.all()
    filterset = filtersets.ASNDetectedFilterSet
    table = tables.ASNDetectedTable


class ASNDetectedBulkEditView(generic.BulkEditView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    queryset = models.ASNDetected.objects.all()
    filterset = filtersets.ASNDetectedFilterSet
    table = tables.ASNDetectedTable
    form = forms.ASNDetectedBulkEditForm


class IPAddressDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.IPAddressDetectedTable
    queryset = models.IPAddressDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.IPAddressDetectedFilterSet
    filterset_form = forms.IPAddressDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'ip-address-detected'
        return extra_content


class IPAddressDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.IPAddressDetected.objects.all()
    filterset = filtersets.IPAddressDetectedFilterSet
    table = tables.IPAddressDetectedTable


class IPAddressDetectedBulkEditView(generic.BulkEditView):
    queryset = models.IPAddressDetected.objects.all()
    filterset = filtersets.IPAddressDetectedFilterSet
    table = tables.IPAddressDetectedTable
    form = forms.IPAddressDetectedBulkEditForm


class PrefixDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.PrefixDetectedTable
    queryset = models.PrefixDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.PrefixDetectedFilterSet
    filterset_form = forms.PrefixDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'prefix-detected'
        return extra_content


class PrefixDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.PrefixDetected.objects.all()
    filterset = filtersets.PrefixDetectedFilterSet
    table = tables.PrefixDetectedTable


class PrefixDetectedBulkEditView(generic.BulkEditView):
    queryset = models.PrefixDetected.objects.all()
    filterset = filtersets.PrefixDetectedFilterSet
    table = tables.PrefixDetectedTable
    form = forms.PrefixDetectedBulkEditForm


class WirelessLANDetectedListView(LogicalObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/logical_last_detected.html'
    table = tables.WirelessLANDetectedTable
    queryset = models.WirelessLANDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.WirelessLANDetectedFilterSet
    filterset_form = forms.WirelessLANDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'wireless-lan-detected'
        return extra_content


class WirelessLANDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.WirelessLANDetected.objects.all()
    filterset = filtersets.WirelessLANDetectedFilterSet
    table = tables.WirelessLANDetectedTable


class WirelessLANDetectedBulkEditView(generic.BulkEditView):
    queryset = models.WirelessLANDetected.objects.all()
    filterset = filtersets.WirelessLANDetectedFilterSet
    table = tables.WirelessLANDetectedTable
    form = forms.WirelessLANDetectedBulkEditForm


##
# Hardware Last Detected
##
class HardwareObjectListView(generic.ObjectListView):
    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        weeks = (4, 3, 2, 1, 0)

        models = [
            Device,
            Interface,
            # InventoryItem,
            Module,
            Cable,
        ]
        model_stats = {}
        for model in models:
            last_polled = []
            for week in weeks:
                curr_date = dt.datetime.now()
                date_diff = dt.timedelta(days=week * 7)
                curr_date = curr_date - date_diff

                last_polled.append(Count('custom_field_data__Netos_Last_Polled',
                                         filter=Q(custom_field_data__Netos_Last_Polled__gt="") & Q(custom_field_data__Netos_Last_Polled__lte=curr_date.strftime("%Y-%m-%d"))))

            query = (model.objects.aggregate(
                four_weeks=last_polled[0],
                three_weeks=last_polled[1],
                two_weeks=last_polled[2],
                one_weeks=last_polled[3],
                zero_weeks=last_polled[4]
            ))
            model_stats[model.__name__] = ";".join(map(str, [query["four_weeks"],
                                                             query["three_weeks"] -
                                                             query["four_weeks"],
                                                             query["two_weeks"] -
                                                             query["three_weeks"],
                                                             query["one_weeks"] -
                                                             query["two_weeks"],
                                                             query["zero_weeks"] - query["one_weeks"]]))
        extra_content["last_polled"] = model_stats

        return extra_content


class DeviceDetectedListView(HardwareObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/hardware_last_detected.html'
    table = tables.DeviceDetectedTable

    queryset = models.DeviceDetected.objects.exclude(**EXCLUDE_Q)

    filterset = filtersets.DeviceDetectedFilterSet
    filterset_form = forms.DeviceDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'device-detected'
        return extra_content


class DeviceDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.DeviceDetected.objects.all()
    filterset = filtersets.DeviceDetectedFilterSet
    table = tables.DeviceDetectedTable


class DeviceDetectedBulkEditView(generic.BulkEditView):
    queryset = models.DeviceDetected.objects.all()
    filterset = filtersets.DeviceDetectedFilterSet
    table = tables.DeviceDetectedTable
    form = forms.DeviceDetectedBulkEditForm


class InterfaceDetectedListView(HardwareObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/hardware_last_detected.html'
    table = tables.InterfaceDetectedTable
    queryset = models.InterfaceDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.InterfaceDetectedFilterSet
    filterset_form = forms.InterfaceDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'interface-detected'
        return extra_content


class InterfaceDetectedBulkDeleteView(generic.BulkDeleteView):

    queryset = models.InterfaceDetected.objects.all()
    filterset = filtersets.InterfaceDetectedFilterSet
    table = tables.InterfaceDetectedTable


class InterfaceDetectedBulkEditView(generic.BulkEditView):

    queryset = models.InterfaceDetected.objects.all()
    filterset = filtersets.InterfaceDetectedFilterSet
    table = tables.InterfaceDetectedTable
    form = forms.InterfaceDetectedBulkEditForm


class ModuleDetectedListView(HardwareObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/hardware_last_detected.html'
    table = tables.ModuleDetectedTable
    queryset = models.ModuleDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.ModuleDetectedFilterSet
    filterset_form = forms.ModuleDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'module-detected'
        return extra_content


class ModuleDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ModuleDetected.objects.all()
    filterset = filtersets.ModuleDetectedFilterSet
    table = tables.ModuleDetectedTable


class ModuleDetectedBulkEditView(generic.BulkEditView):
    queryset = models.ModuleDetected.objects.all()
    filterset = filtersets.ModuleDetectedFilterSet
    table = tables.ModuleDetectedTable
    form = forms.ModuleDetectedBulkEditForm


class CableDetectedListView(HardwareObjectListView):
    actions = ('export', 'bulk_edit', 'bulk_delete')

    template_name = 'netos_inventory/hardware_last_detected.html'
    table = tables.CableDetectedTable
    queryset = models.CableDetected.objects.exclude(**EXCLUDE_Q)
    filterset = filtersets.CableDetectedFilterSet
    filterset_form = forms.CableDetectedFilterForm

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        extra_content["active_tab"] = 'cable-detected'
        return extra_content


class CableDetectedBulkDeleteView(generic.BulkDeleteView):
    queryset = models.CableDetected.objects.all()
    filterset = filtersets.CableDetectedFilterSet
    table = tables.CableDetectedTable


class CableDetectedBulkEditView(generic.BulkEditView):
    queryset = models.CableDetected.objects.all()
    filterset = filtersets.CableDetectedFilterSet
    table = tables.CableDetectedTable
    form = forms.CableDetectedBulkEditForm

# LAN Consolidation Report


class LANConsolidationReportListView(generic.ObjectListView):
    table = tables.LANConsolidationReportTable

    queryset = (models.LANConsolidationReport.objects
                .annotate(interface_down=INTERFACE_DOWN_Q)
                .annotate(interface_up=INTERFACE_UP_Q)
                .annotate(utilization=Round(Cast(Case(
                    When(GreaterThan(F('interface_down'), 0) | GreaterThan(F('interface_up'), 0),
                         then=(Cast(F('interface_up'), FloatField()) / (Cast(F('interface_up') + F('interface_down'), FloatField())) * 100.0)),
                    default=0.0), FloatField()),  precision=2))
                )

    # Vendor, Device Type, Device Role, Site and Region.

    filterset = filtersets.LANConsolidationReportFilterSet
    filterset_form = forms.LANConsolidationReportFilterForm
    template_name = "netos_inventory/lan_object_list.html"

    def get_extra_context(self, request):
        ranges = ((0, 25), (25, 50), (50, 75), (75, 101))

        queryset = (models.LANConsolidationReport.objects
                    .annotate(interface_down=INTERFACE_DOWN_Q)
                    .annotate(interface_up=INTERFACE_UP_Q)
                    .annotate(utilization=Round(Cast(Case(
                        When(GreaterThan(F('interface_down'), 0) | GreaterThan(F('interface_up'), 0),
                             then=(Cast(F('interface_up'), FloatField()) / (Cast(F('interface_up') + F('interface_down'), FloatField())) * 100.0)),
                        default=0.0), FloatField()),  precision=2))
                    )
        # NOTE: this can be splited to separete views to imporove performance
        categories = [
            ('device_type', 'device_type'),
            ('site', 'sites'),
            ('site.region', 'region'),
            ('device_type.manufacturer', 'vendor'),
            ('device_role', 'device_role'),
        ]
        extra_data = {}
        for category, html_rep in categories:
            group = defaultdict(list)
            for obj in queryset:
                # get nested fields
                fields = category.split('.')[::-1]
                val = obj
                while fields:
                    field = fields.pop()
                    val = getattr(val, field)
                group[val].append(obj.utilization)

            range_group = {}
            for k, v in group.items():
                count = [0 for _ in range(len(ranges))]
                for e in v:
                    for i, r in enumerate(ranges):
                        beg, end = r
                        if beg <= e < end:
                            count[i] += 1
                # put category name and id in string for js to parse it
                k_rep = ";" if k is None else f"{k.pk};{str(k)}"
                range_group[k_rep] = ";".join(map(str, count))
            extra_data[html_rep] = range_group
        return extra_data


class LANConsolidationReportEditView(generic.ObjectEditView):
    queryset = models.LANConsolidationReport.objects.all()
    form = forms.LANConsolidationReportEditForm


class LANConsolidationReportDeleteView(generic.ObjectDeleteView):
    queryset = models.LANConsolidationReport.objects.all()
