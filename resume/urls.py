from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('(?P<info_id>\w+)$', views.display_resume, name="resume")
]
