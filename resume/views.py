from django.shortcuts import render
from django.http import HttpResponse
from . import models
from briefcase.models import Type
from django.db.models import Prefetch
from django.views import View


class DisplayResume(View):
    template = "resume/resume.html"

    def _get_context(self, request, info_id):
        basic_info = models.BasicInfo.objects.get(info_id=info_id)
        return {
            "basic_info": basic_info,
            "sections": models.Section.objects.filter(user=basic_info)
            .order_by("position")
            .prefetch_related(
                Prefetch(
                    "content__list_item",
                    queryset=models.ListItem.objects.all().order_by(
                        "position", "-year"
                    ),
                )
            ),
            "section_types": {key: value for value, key in models.section_types},
        }

    def get(self, request, info_id):
        return render(request, self.template, self._get_context(request, info_id))


class DisplayPrintResume(DisplayResume):
    template = "resume/print.html"
