from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from . import models
from briefcase.models import Type
from django.db.models import Prefetch
from django.utils import translation
from django.views import View
from django.urls import reverse

class DisplayResume(View):
    template = "resume/resume.html"

    def _get_context(self, request, info_id):
        basic_info = models.BasicInfo.objects.get(info_id=info_id)
        languages = models.BasicInfo.objects.filter(name=basic_info.name, email=basic_info.email)
        return {
            "languages": languages,
            "basic_info": basic_info,
            "sections": models.Section.objects.filter(user=basic_info)
            .order_by("position")
            .prefetch_related(
                Prefetch(
                    "content__list_item",
                    queryset=models.ListItem.objects.all().order_by(
                        "position", "-period"
                    ),
                )
            ),
            "section_types": {key: value for value, key in models.section_types},
        }

    def get(self, request, info_id):
        context = self._get_context(request, info_id)
        mobile_version = context['basic_info'].mobile_version
        if request.user_agent.is_pc is False and mobile_version:
            return redirect('resume',info_id=mobile_version.info_id)

        return render(request, self.template, context)


class DisplayPrintResume(DisplayResume):
    template = "resume/print.html"

class DisplayHackerResume(View):
    template = "hacker_template/template.html"

    def _get_context(self, request, info_id):


        basic_info = models.BasicInfo.objects.get(info_id=info_id)
        translation.activate(basic_info.language.code)
        languages = models.BasicInfo.objects.filter(name=basic_info.name, email=basic_info.email, cv_style=basic_info.cv_style)
        # images from briefcase
        # briefcase = Type.objects.get(user__in=[basic_info])
        # breakpoint()
        # return model.items.all().order_by("position")
        return {
        "languages": languages,
        'basic_info': basic_info,
        "sections": models.Section.objects.filter(user=basic_info).order_by('position'),
        "section_types": {key: value for value, key in models.section_types},
    }
    def get(self, request, info_id):
        print(request.user_agent.is_pc)
        context = self._get_context(request, info_id)
        mobile_version = context['basic_info'].mobile_version
        if request.user_agent.is_pc is False and mobile_version:
            return redirect('resume',info_id=mobile_version.info_id)

        return render(request, self.template, context)

def index_view(request):
    basic_info = get_object_or_404(models.BasicInfo, is_homepage=True)
    if (basic_info.cv_style == 'hr'):
        return DisplayHackerResume.as_view()(request, basic_info.info_id)
    elif (basic_info.cv_style == 'st'):
        return DisplayResume.as_view()(request, basic_info.info_id)
    else:
        return HttpResponse("Could not find CV set as homepage ")
        

# def new_layout(request):
#     basic_info = models.BasicInfo.objects.get(info_id=info_id)
#     languages = models.BasicInfo.objects.filter(name=basic_info.name, email=basic_info.email)
#     return render(request, 'hacker_template/template.html', {
#         "languages": languages,
#         'basic_info': basic_info,
#         "sections": models.Section.objects.all().order_by('position'),
#         "section_types": {key: value for value, key in models.section_types},
#     })
