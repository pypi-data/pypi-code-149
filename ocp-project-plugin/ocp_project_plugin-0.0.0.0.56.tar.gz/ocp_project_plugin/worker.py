from django_rq import job, get_queue
from dcim.models import Device
#from ocp_project_plugin.models import AppEnvironment, OCPProject, Collection, Compliance, ServiceMapping
from datetime import datetime
import time
#from ocp_project_plugin.choices import CollectFailChoices, CollectStatusChoices
import ipaddress
#from .ocp_project_plugincollect import CollectDeviceData
#from .ocp_project_plugincustom_exceptions import CollectionException
from django.db.models import Q
from git import Repo
#from ocp_project_plugin.choices import ServiceComplianceChoices
#from ocp_project_plugin.git_manager import get_device_config, get_days_after_update
#from ocp_project_plugin.config_manager import get_config_diff
from django.conf import settings

from .utils.gitlab import pull_repo
from git import Repo, Git
import os
import yaml
from yaml import SafeLoader
from collections import namedtuple

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get("config_officer", dict())
CF_NAME_COLLECTION_STATUS = PLUGIN_SETTINGS.get("CF_NAME_COLLECTION_STATUS", "collection_status")
NETBOX_DEVICES_CONFIGS_DIR = PLUGIN_SETTINGS.get("NETBOX_DEVICES_CONFIGS_DIR", "/device_configs")
GLOBAL_TASK_INIT_MESSAGE = 'global_collection_task'


def get_active_collect_task_count():
    """ Get count of pending collection tasks."""
    #return Collection.objects.filter((Q(status__iexact=CollectStatusChoices.STATUS_PENDING)
    #                                  | Q(status__iexact=CollectStatusChoices.STATUS_RUNNING)) & Q(
    #    message__iexact=GLOBAL_TASK_INIT_MESSAGE)).count()


"""
1. Git Repo pullen
2. Überprüfen ob es einen Branch mit dem Ticket Namen schon gibt
3. Neuer Branch erstellen mit dem Ticket Namen
4. Secrets entschlüsseln
5. OCPPRoject/AppEnvironment Model Daten in yaml konvertieren
6. YAML Daten dem values.yaml anfügen
7. Secrets der Secrets Datei anfügen
8. Secret verschlüsseln
9. Mergen
"""


@job("default")
def pull_repository_2(hostname):
    """Collect device configuration by name. Task started with hostname param.

    device = Device.objects.get(name__iexact=hostname)
    collect_task = Collection.objects.create(device=device, message="device collection task")
    collect_task.save()
"""
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    commit_msg = f"device_{hostname}_{now}"
    #get_queue("default").enqueue("ocp_project_plugin.worker.pull_repository", collect_task.pk, commit_msg)


@job("default")
def pull_repository(repo_dir):
    repo_instance = Git(repo_dir)
    result = repo_instance.pull()
    print(f'{result}')
