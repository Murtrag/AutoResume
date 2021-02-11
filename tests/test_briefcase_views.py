import pytest

from django.urls import reverse
from mixer.backend.django import mixer


def test_display_resume(client):
    basic_info = mixer.blend("resume.BasicInfo")
    request = client.get(reverse("resume", kwargs={"info_id": basic_info.info_id}))
    assert request.status_code == 200
