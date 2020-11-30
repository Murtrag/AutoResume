from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.conf import settings

from .models import Type
from resume.models import BasicInfo

class DocumentListView(ListView):
    paginate_by = 10
    template_name = "briefcase/index.html"
    def get_context_data(self, **kwargs):
                 context = super().get_context_data(**kwargs)
                 context.update({
                     'title': self.kwargs['type'],
                     'basic_info': BasicInfo.objects.get(info_id=self.kwargs["info_id"]),
                     'briefcase': Type.objects.all(), #@TODO filter info_id
                     'url_button': settings.URL_BUTTON 
                     })
                 print(context)
                 return context

    def get_queryset(self):
        model = Type.objects.get(name=self.kwargs['type'])
        return model.items.all()
    
