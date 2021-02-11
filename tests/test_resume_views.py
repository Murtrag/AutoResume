import pytest

from django.urls import reverse
from mixer.backend.django import mixer


def test_dcoument_list_view(client):
    basic_info = mixer.blend("resume.BasicInfo")
    type = mixer.blend("briefcase.Type", user=basic_info, name="test")

    request = client.get(
        reverse("briefcase", kwargs={"info_id": basic_info.info_id, "type": type.name})
    )
    assert request.status_code == 200
