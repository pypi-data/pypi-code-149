from django.shortcuts import redirect
from django.urls import reverse
from django_rq import get_queue


def add_project(request):
    try:
        get_queue("default").enqueue("ocp-project-plugin.worker.pull_repository", git_dir='/repo/project_repo')
        return redirect(reverse('plugins:ocp-project-plugin:appenvironment_list'))
    except Exception as e:
        message = e
        return redirect(reverse('plugins:ocp-project-plugin:appenvironment_list'))