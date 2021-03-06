from django.contrib import admin
from resume import models
from django.shortcuts import redirect
from django.utils.html import format_html


@admin.register(models.BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    def link_resume_url(self, obj):
        return format_html(
            "<a target='_blank' href='{0}'>{1}</a>",
            redirect("resume", info_id=obj.info_id).url,
            obj.resume_url,
        )

    list_display = ("name", "email", "info_id", "link_resume_url")


@admin.register(models.UrlButton)
class UrlButtonAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "url")


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ("user",)
    list_display = ("user", "name", "section_type", "position")


@admin.register(models.ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ("headline", "year", "position")


@admin.register(models.GraphItem)
class GraphItemAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = ("category", "name", "level", "position")


@admin.register(models.SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ("name",)
