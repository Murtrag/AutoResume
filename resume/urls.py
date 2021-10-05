from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index_view, name="homepage"),
    re_path("resume/hr/(?P<info_id>\w+)", views.DisplayHackerResume.as_view(), name="hacker_resume"),
    re_path("resume/st/(?P<info_id>\w+)", views.DisplayResume.as_view(), name="resume"),
    re_path(
        "resume/(?P<info_id>\w+)/print/$",
        views.DisplayPrintResume.as_view(),
        name="print_resume",
    ),
]
