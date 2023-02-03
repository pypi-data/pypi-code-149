from django.shortcuts import redirect
from django.urls import reverse
from django_rq import get_queue

import logging


def add_project(request):
    logger = logging.getLogger('netbox.ocp_project_plugin')

    try:
        get_queue("default").enqueue("ocp_project_plugin.worker.pull_repository")
        logger.debug(f'Evaluating job started')
        return redirect(reverse('plugins:ocp_project_plugin:appenvironment_list'))
    except Exception as e:
        message = e
        logger.debug(f'{message}')
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))


def clone_repo(request):
    logger = logging.getLogger('netbox.ocp_project_plugin')

    try:
        get_queue("default").enqueue("ocp_project_plugin.worker.clone_repository")
        logger.debug(f'Evaluating job started')
        return redirect(reverse('plugins:ocp_project_plugin:appenvironment_list'))
    except Exception as e:
        message = e
        logger.debug(f'{message}')
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))





