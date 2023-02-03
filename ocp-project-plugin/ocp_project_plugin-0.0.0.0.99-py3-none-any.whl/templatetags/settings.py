from django import template
from django.conf import settings

register = template.Library()

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get('ocp_project_plugin', dict())
GITLAB_PROJECT_URL = PLUGIN_SETTINGS.get('gitlab_project_url', '')
JIRA_BROWSE_URL = PLUGIN_SETTINGS.get('jira_browse_url', '')
CPU_COST = PLUGIN_SETTINGS.get('cpu_cost', '')
MEMORY_COST = PLUGIN_SETTINGS.get('memory_cost', '')
STORAGE_COST = PLUGIN_SETTINGS.get('storage_cost', '')
OCP_TST_URL = PLUGIN_SETTINGS.get('ocp_tst_url', '')
OCP_DEV_URL = PLUGIN_SETTINGS.get('ocp_dev_url', '')
OCP_INT_URL = PLUGIN_SETTINGS.get('ocp_int_url', '')
OCP_PRD_URL = PLUGIN_SETTINGS.get('ocp_prd_url', '')


# settings value
@register.simple_tag
def jira_browse_url(ticket_id):
    return f"{JIRA_BROWSE_URL}{ticket_id}"


@register.simple_tag
def get_cpu_cost(amount):
    if amount is '':
        return '-'
    else:
        return int(CPU_COST) * int(amount)


@register.simple_tag
def get_memory_cost(amount):
    if amount is '':
        return '-'
    else:
        return int(MEMORY_COST) * float(str(amount)[:-2])


@register.simple_tag
def get_storage_cost(amount):
    if amount is '':
        return '-'
    else:
        return int(STORAGE_COST) * int(amount)


@register.simple_tag
def get_total_cost(cpu_amount, memory_amount, storage_amount):
    if cpu_amount is '' or memory_amount is '':
        return '-'
    else:
        return int(CPU_COST) * int(cpu_amount) + int(MEMORY_COST) * float(str(memory_amount)[:-2]) + int(STORAGE_COST) \
            * int(storage_amount)


@register.simple_tag
def get_ocp_resource_quota_url(cluster_env, app_env, name):
    suffix = '/k8s/ns/' + name + '-' + app_env + '/resourcequotas'
    if cluster_env is 'TST':
        return OCP_TST_URL + suffix
    if cluster_env is 'DEV':
        return OCP_DEV_URL + suffix
    if cluster_env is 'INT':
        return OCP_INT_URL + suffix
    if cluster_env is 'PRD':
        return OCP_PRD_URL + suffix
