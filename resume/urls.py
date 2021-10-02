from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path("hr/(?P<info_id>\w+)", views.DisplayHackerResume.as_view(), name="new_resume"),
    re_path("st/(?P<info_id>\w+)", views.DisplayResume.as_view(), name="resume"),
    re_path(
        "(?P<info_id>\w+)/print/$",
        views.DisplayPrintResume.as_view(),
        name="print_resume",
    ),
]
