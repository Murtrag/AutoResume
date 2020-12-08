from django.contrib import admin
from resume import models


class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "info_id")


admin.site.register(models.BasicInfo, BasicInfoAdmin)


class GitHubButtonAdmin(admin.ModelAdmin):
    list_display = ("user", "url")


admin.site.register(models.GitHubButton, GitHubButtonAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_filter = ("user",)
    list_display = ("user", "name", "section_type", "position")


admin.site.register(models.Section, SectionAdmin)


class ListItemAdmin(admin.ModelAdmin):
    list_display = ("headline", "year")


admin.site.register(models.ListItem, ListItemAdmin)


class GraphItemAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = ("category", "name", "level")


admin.site.register(models.GraphItem, GraphItemAdmin)


class SectionContentAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.SectionContent, SectionContentAdmin)
