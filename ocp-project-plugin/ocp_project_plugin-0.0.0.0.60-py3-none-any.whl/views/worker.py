from django.shortcuts import redirect
from django.urls import reverse
from django_rq import get_queue


def add_project(request):
    try:
        get_queue("default").enqueue("ocp_project_plugin.worker.pull_repository")
        return redirect(reverse('plugins:ocp_project-plugin:appenvironment_list'))
    except Exception as e:
        message = e
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))


def clone_repo(request):
    try:
        get_queue("default").enqueue("ocp_project_plugin.worker.clone_repository")
        return redirect(reverse('plugins:ocp_project-plugin:appenvironment_list'))
    except Exception as e:
        message = e
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))
