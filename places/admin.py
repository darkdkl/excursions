from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin
from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from places.models import Image, Place

admin.site.unregister(FlatPage)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ["img", ]

    def img(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width=200 height=200 />')


class PlaceAdminForm(forms.ModelForm):
    long_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Place
        fields = ["title", "lat", "lng", "short_description",
                  "long_description"]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm
    inlines = (ImageInline,)
