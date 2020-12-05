from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Type
from resume.models import BasicInfo


class DocumentListView(ListView):
    paginate_by = 4
    template_name = "briefcase/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": self.kwargs["type"],
                "basic_info": BasicInfo.objects.get(info_id=self.kwargs["info_id"]),
            }
        )
        return context

    def get_queryset(self):
        model = Type.objects.get(name=self.kwargs["type"])
        return model.items.all()
