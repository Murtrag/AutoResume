from django.contrib import admin

from .models import Type, Item, Image


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("user", "name")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "position")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("str_name", "text_color", "primary")
