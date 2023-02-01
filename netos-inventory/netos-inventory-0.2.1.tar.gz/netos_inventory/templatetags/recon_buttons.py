from django import template
from django.contrib.contenttypes.models import ContentType
from django.urls import NoReverseMatch, reverse

from extras.models import ExportTemplate
from utilities.utils import get_viewname, prepare_cloned_fields

register = template.Library()

@register.inclusion_tag('netos_inventory/bulk_recon_button.html')
def bulk_recon_button(model, action='recon', query_params=None):
    try:
        url = reverse(get_viewname(model, action))
        if query_params:
            url = f'{url}?{query_params.urlencode()}'
    except NoReverseMatch:
        url = None

    return {
        'url': url,
    }


@register.inclusion_tag('netos_inventory/lan_utilization_graph.html')
def lan_utilization_graph(utilization, danger_threshold=30):
    """
    Display a horizontal bar graph indicating a percentage of utilization.
    """
    if utilization <= danger_threshold:
        bar_class = 'red' 
    else:
        bar_class = 'green'
    return {
        'utilization': utilization,
        'bar_class': bar_class,
    }
