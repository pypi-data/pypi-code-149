# -*- coding: utf-8 -*-

from django_six import re_path

from django_onerror import views as err_views


app_name = 'django_onerror'


urlpatterns = [
    re_path(r'^report', err_views.err_report, name='err_report'),
]
