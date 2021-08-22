from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Type
from resume.models import BasicInfo 



class DocumentListView(ListView):
    paginate_by = 4
    template_name = "briefcase/index.html"

    def get_context_data(self, **kwargs):
        basic_info = BasicInfo.objects.get(info_id=self.kwargs["info_id"])
        languages = BasicInfo.objects.filter(name=basic_info.name, email=basic_info.email)
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": self.kwargs["type"],
                "basic_info": basic_info, 
                "languages": languages,
            }
        )
        return context

    def get_queryset(self):
        model = Type.objects.get(name=self.kwargs["type"])
        return model.items.all().order_by("position")
