import os
from django.db import models
from resume.models import BasicInfo
from core.models import OrderedModel


class Type(models.Model):
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    items = models.ManyToManyField("Item")

    def __str__(self):
        return self.name


class Item(OrderedModel):
    name = models.CharField(max_length=35)
    # description = models.TextField(blank=True)
    images = models.ManyToManyField("Image")
    position = models.IntegerField()

    @property
    def get_primary_image(self):
        return self.images.filter(primary=True).first()

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="galery")
    name = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    text_color = models.CharField(max_length=25, default="white")
    primary = models.BooleanField(blank=True, default=True)

    @property
    def str_name(self):
        """ This property is created for the Admin """
        return self.__str__()

    def __str__(self):
        return "image: {}".format(
            self.name or os.path.splitext(os.path.basename(self.image.name))[0]
        )
