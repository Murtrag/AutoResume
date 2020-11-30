from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=25)
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    url = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to="galery")

    def __str__(self):
        return self.name


