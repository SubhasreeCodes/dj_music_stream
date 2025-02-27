from django.contrib import admin
from django.utils.html import format_html

from backend.models import Genre, Brand

# Register your models here.
admin.site.register(Genre)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'image_tag', 'description')

    search_fields = ('name', 'status')

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.image_path.url))

    image_tag.short_description = 'Image'

admin.site.register(Brand,BrandAdmin)