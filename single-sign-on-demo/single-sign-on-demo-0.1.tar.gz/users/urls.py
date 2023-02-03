from django.urls import path

from . import views

urlpatterns = [
    path('ping', views.ping, name="ping"),
    path('signin', views.signin, name="signin"),
    path('callback', views.signin_callback, name="callback")
]