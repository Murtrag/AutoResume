from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from itertools import groupby
from numpy import array_split
from hashlib import md5
from string import ascii_letters, digits
from random import choice
from re import sub

# md5(b'test').hexdigest()


section_types = [
    (0, "Text"),
    (1, "List"),
    (2, "Graph"),
]


class BasicInfo(models.Model):
    info_id = models.CharField(max_length=32, blank=True, null=True, editable=False)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=45)

    def save(self, *args, **kwargs):
        if self.info_id is None:
            salt = "".join(
                [choice(list(list(ascii_letters) + list(digits))) for _ in range(10)]
            )
            self.info_id = md5(
                bytes(f"{self.name} {self.address} {self.phone_number} {salt}", "utf-8")
            ).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.email} | {self.info_id}"


class Section(models.Model):
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    section_type = models.IntegerField(choices=section_types)
    content = models.OneToOneField("SectionContent", on_delete=models.CASCADE)
    position = models.IntegerField(
        help_text="Determines position on resume, section with the smallest number will be on  the top",
        default=0,
    )

    @property
    def section_class_name(self):
        return sub(r"\W", "", sub(r"\s", "_", self.name)).lower()

    def __str__(self):
        return f"{self.user} | {self.name}"


class ListItem(models.Model):
    headline = models.CharField(max_length=50)
    description = models.TextField(
        help_text="This field supports bbcode https://en.wikipedia.org/wiki/BBCode"
    )
    year = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.headline} | {self.year}"


class GraphItem(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.category} | {self.name} - {self.level}"


class SectionContent(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="this field does not have anny effect on resume it is just a human readable name for an object",
    )  # TODO make it automatic in admin.py

    text = models.TextField(
        blank=True,
        help_text="This field supports bbcode https://en.wikipedia.org/wiki/BBCode",
    )
    list_item = models.ManyToManyField("ListItem", blank=True)
    graph_item = models.ManyToManyField("GraphItem", blank=True)

    def get_graph_grouped(self):
        return array_split(
            list(
                {
                    key: list(value)
                    for key, value in groupby(
                        self.graph_item.all().order_by("category"),
                        key=lambda x: x.category,
                    )
                }.items()
            ),
            2,
        )

    def __str__(self):
        return f"{self.name}"


class GitHubButton(models.Model):
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    url = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.user.name} | {self.url}"
