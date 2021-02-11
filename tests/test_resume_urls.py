import pytest

from django.urls import reverse
from mixer.backend.django import mixer


def test_url_resume():
    basic_info = mixer.blend("resume.BasicInfo")

    path = reverse(
        "resume",
        kwargs={
            "info_id": basic_info.info_id,
        },
    )
    components = (
        "/resume/",
        basic_info.info_id,
    )
    assert all(c in path for c in components)
