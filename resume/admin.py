from django.contrib import admin
from resume import models

admin.site.register(models.BasicInfo)
admin.site.register(models.Section)
admin.site.register(models.ListItem)
admin.site.register(models.GraphItem)
admin.site.register(models.SectionContent)

# Register your models here.
