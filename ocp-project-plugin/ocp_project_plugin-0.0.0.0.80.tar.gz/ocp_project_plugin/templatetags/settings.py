from django import template
from django.conf import settings

register = template.Library()

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get('ocp_project_plugin', dict())
GITLAB_PROJECT_URL = PLUGIN_SETTINGS.get('gitlab_project_url', '')
JIRA_BROWSE_URL = PLUGIN_SETTINGS.get('jira_browse_url', '')


# settings value
@register.simple_tag
def jira_browse_url(ticket_id):
    return f"{JIRA_BROWSE_URL}{ticket_id}"
