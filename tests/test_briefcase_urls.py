import pytest

from django.urls import reverse
from mixer.backend.django import mixer


def test_url_briefcase():
    basic_info = mixer.blend("resume.BasicInfo")
    type = mixer.blend("briefcase.Type", user=basic_info, name="test")

    path = reverse(
        "briefcase", kwargs={"info_id": basic_info.info_id, "type": type.name}
    )
    components = ("/briefcase/documents/", basic_info.info_id, type.name)
    assert all(c in path for c in components)
