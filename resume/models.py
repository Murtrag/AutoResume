from re import sub
from hashlib import md5
from random import choice
from numpy import array_split
from itertools import groupby
from string import ascii_letters, digits

from django.db import models
from django.urls import reverse
from core.models import OrderedModel
from django.contrib.sites.models import Site
from django.core.validators import MaxValueValidator, MinValueValidator


# md5(b'test').hexdigest()


section_types = [
    (0, "Text"),
    (1, "List"),
    (2, "Graph"),
]


class Language(models.Model):
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=8, help_text="Use emoji icons https://emojipedia.org/")

    def __str__(self):
        return self.name

class BasicInfo(models.Model):
    style_choices = {
        'st' : 'standard',
        'hr': 'hacker',
        }

    info_id = models.CharField(max_length=32, blank=True, null=True, editable=False)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=45)
    website = models.CharField(max_length=245)
    extra_header = models.TextField(blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    cv_style = models.CharField(max_length=2, choices=style_choices.items())
    is_homepage = models.BooleanField()

    

    def save(self, *args, **kwargs):
        if self.info_id is None:
            salt = "".join(
                [choice(list(list(ascii_letters) + list(digits))) for _ in range(10)]
            )
            self.info_id = md5(
                bytes(f"{self.name} {self.address} {self.phone_number} {salt}", "utf-8")
            ).hexdigest()
        super().save(*args, **kwargs)

    @property
    def resume_url(self):
        if self.is_homepage:
            return reverse('homepage')
        return f"{Site.objects.get_current().domain}/resume/{self.cv_style}/{self.info_id}"

    def __str__(self):
        return f"{self.id}:{self.name} - {self.language} [{self.style_choices[self.cv_style]}]"


class Section(OrderedModel):
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    section_type = models.IntegerField(choices=section_types)
    content = models.ForeignKey("SectionContent", on_delete=models.CASCADE)
    position = models.IntegerField(
        help_text="Determines position on resume, section with the smallest number will be on  the top",
        default=0,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs, user=self.user)

    @property
    def section_class_name(self):
        return sub(r"\W", "", sub(r"\s", "_", self.name)).lower()

    def __str__(self):
        return f"{self.user} | {self.name}"


class ListItem(OrderedModel):
    headline = models.CharField(max_length=90)
    short_description = models.TextField(
        help_text="This field supports bbcode https://en.wikipedia.org/wiki/BBCode",
        blank=True,
    )
    description = models.TextField(
        help_text="This field supports bbcode https://en.wikipedia.org/wiki/BBCode",
        blank=True,
    )
    # tutaj podpiąc pod itemki z bsreafcase
    images = models.ForeignKey('briefcase.Item',blank=True, null=True, on_delete=models.CASCADE)
    period = models.CharField(max_length=25, blank=True)
    position = models.IntegerField(default=0)
    weight = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(900)], default=400
    )

    def __str__(self):
        return f"{self.headline} | {self.period}"


class GraphItem(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    has_level = models.BooleanField(default=False)
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0
    )
    level_desc = models.CharField(max_length=25, help_text="This is a text description of the proficiency level", blank=True)
    position = models.IntegerField(default=0)
    weight = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(900)], default=400
    )

    def __str__(self):
        return f"{self.category} | {self.name} - {self.level}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        different_categories = GraphItem.objects.filter(position=self.position).exclude(
            category=self.category
        )

        # set all same categories graph items to the same possiton
        GraphItem.objects.filter(category=self.category).update(position=self.position)

        # set all different categories graph items with same position to a different one
        reserved_postions = GraphItem.objects.values_list(
            "position", flat=True
        ).distinct()
        reserved_max = max(reserved_postions)
        unreserved_position = min(
            [i for i in range(0, reserved_max) if i not in reserved_postions]
            or [reserved_max + 1]
        )
        different_categories.update(position=unreserved_position)


class SectionContent(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="this field does not have anny effect on resume it is just a human readable name for an object",
    )

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
                        self.graph_item.all().order_by("position", "category"),
                        key=lambda x: x.category,
                    )
                }.items()
            ),
            2,
        )

    def __str__(self):
        return f"{self.name}"


class UrlButton(models.Model):
    name = models.CharField(max_length=20)
    user = models.ManyToManyField(BasicInfo)
    url = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.user.name} - f{self.name} | {self.url}"
