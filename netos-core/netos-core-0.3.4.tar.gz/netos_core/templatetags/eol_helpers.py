import logging
from django.conf import settings
from django import template

register = template.Library()


config = settings.PLUGINS_CONFIG["netos_core"]


@register.inclusion_tag('netos_core/eol_threshold.html')
def eol_threshold(daysleft, warning_threshold=244, danger_threshold=154):
    """
    Display a horizontal bar graph indicating a percentage of utilization.
    """
    logger = logging.getLogger(__name__)
    try:
        warning_threshold = int(config.get("warning_threshold", warning_threshold))
        danger_threshold = int(config.get("danger_threshold", danger_threshold))
    except ValueError:
        logger.error("Invalid warning_threshold or danger_threshold falling back to default")

    if daysleft >= warning_threshold:
        bar_class = 'bg-success'
    elif danger_threshold and daysleft <= danger_threshold:
        bar_class = 'bg-danger'
    elif warning_threshold and daysleft <= warning_threshold:
        bar_class = 'bg-warning'
    else:
        bar_class = 'bg-gray'
    return {
        'daysleft': daysleft,
        'bar_class': bar_class,
    }
