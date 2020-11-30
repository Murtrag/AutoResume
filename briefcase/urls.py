from django.urls import re_path
from briefcase import views


urlpatterns = [
    re_path('documents/(?P<info_id>\w+)/(?P<type>\w+)/$', views.DocumentListView.as_view(), name="briefcase"),

]
