import logging

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
import git
import os
import yaml
from yaml import SafeLoader
from collections import namedtuple

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get("config_officer", dict())
CF_NAME_COLLECTION_STATUS = PLUGIN_SETTINGS.get("CF_NAME_COLLECTION_STATUS", "collection_status")
NETBOX_DEVICES_CONFIGS_DIR = PLUGIN_SETTINGS.get("NETBOX_DEVICES_CONFIGS_DIR", "/device_configs")
GLOBAL_TASK_INIT_MESSAGE = 'global_collection_task'

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get('ocp_project_plugin', dict())
GITLAB_PROJECT_URL = PLUGIN_SETTINGS.get('gitlab_project_url', '')
VALUES_PATH = PLUGIN_SETTINGS.get('values_path', '')

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
def pull_repository():
    g = git.cmd.Git('/repo/project_repo')
    result = g.pull()
    print(f'{g.working_dir}-{result}')


@job("default")
def clone_repository():
    logger = logging.getLogger('netbox.ocp_project_plugin')
    logger.warning(f'Started cloning')
    logger.warning(f'{GITLAB_PROJECT_URL}')
    git.Git('/repo/project_repo').clone(GITLAB_PROJECT_URL)
    logger.warning(f'cloning finished')
