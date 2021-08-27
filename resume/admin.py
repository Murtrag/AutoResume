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

    list_display = ("name", "email", "info_id", "link_resume_url", "language")


@admin.register(models.UrlButton)
class UrlButtonAdmin(admin.ModelAdmin):
    list_filter = ("user", )
    list_display = ("name", "users", "url")
    def users(self, obj):
        return ", ".join(u.name for u in obj.user.all())
    


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ("user", "section_type")
    list_display = ("user", "name", "section_type", "position")


@admin.register(models.ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = ("headline", "year", "position")


@admin.register(models.GraphItem)
class GraphItemAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = ("category", "name", "level", "position")



@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "image")

class SectionContentUserFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('user')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'userek'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list = models.BasicInfo.objects.all().values_list('name', 'language', 'pk')
        formated = [(x[2], (f'{x[0]} - {x[1]}')) for x in list]
        return formated

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.

        if self.value() is None:
            return None
        queryset = models.SectionContent.objects.filter(section__user__pk=self.value())
        if len(queryset) == 0:
            return models.Section.objects.none()
            return None
        return queryset 

@admin.register(models.SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    def section(self, obj):
        section = models.Section.objects.filter(content=obj).first()
        return section

    def user(self, obj):
        section = models.Section.objects.filter(content=obj).first()
        return section.user
    list_filter = (SectionContentUserFilter,)
    list_display = ("name", "section", "user")

