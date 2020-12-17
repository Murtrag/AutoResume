from django.urls import re_path
from briefcase import views

urlpatterns = [
    re_path(
        "documents/(?P<info_id>\w+)/(?P<type>\w+)/$",
        views.DocumentListView.as_view(),
        name="briefcase",
    ),
    re_path("zoom/(?P<img_path>\w+\.\w{2,3})$", views.zoom_image),
]
