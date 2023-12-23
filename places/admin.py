from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place
from .models import Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview', ]

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height:100px;">')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
