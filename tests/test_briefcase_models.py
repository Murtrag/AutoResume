import os
import pytest

from mixer.backend.django import mixer


def test_type_str():
    type = mixer.blend("briefcase.Type", name="test")
    assert str(type) == type.name


class TestItem:
    def setup_method(self):
        images = mixer.cycle(2).blend("briefcase.Image", primary=False)
        self.image_primary = mixer.blend(
            "briefcase.Image", primary=True, name="Primary"
        )
        self.item = mixer.blend(
            "briefcase.Item", name="test", images=[*images, self.image_primary]
        )

    def test_get_primary_image(self):
        assert self.item.get_primary_image.name == self.image_primary.name

    def test_str(self):
        assert str(self.item) == self.item.name


class TestImage:
    def setup_method(self):
        self.image = mixer.blend("briefcase.Image")
        self.image_no_name = mixer.blend("briefcase.Image", name="")

    def test_str_name(self):
        assert self.image.str_name == str(self.image)

    def test_str_with_name(self):
        assert self.image.name in str(self.image)

    def test_str_without_name(self):
        name = os.path.splitext(os.path.basename(self.image_no_name.image.name))[0]
        assert name in str(self.image_no_name)
