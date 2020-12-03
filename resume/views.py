from django.shortcuts import render
from django.http import HttpResponse
from . import models
from briefcase.models import Type


def display_resume(request, info_id):
    basic_info = models.BasicInfo.objects.get(info_id=info_id)
    return render(
        request,
        "resume/resume.html",
        {
            "basic_info": basic_info,
            "sections": models.Section.objects.filter(user=basic_info).order_by(
                "position"
            ),
            "section_types": {key: value for value, key in models.section_types},
        },
    )
