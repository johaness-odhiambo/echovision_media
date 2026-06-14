from django.contrib import admin

from .models import GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("thumbnail_tag", "title", "media_type", "service", "is_featured", "created_at")
    list_filter = ("media_type", "is_featured")
    search_fields = ("title", "description")
    readonly_fields = ("thumbnail_tag",)

    def thumbnail_tag(self, obj):
        if obj.poster_image and hasattr(obj.poster_image, 'url'):
            return f"<img src=\"{obj.poster_image.url}\" style=\"width:120px;height:auto;border-radius:6px;\" />"
        if obj.file and hasattr(obj.file, 'url') and obj.media_type == 'image':
            return f"<img src=\"{obj.file.url}\" style=\"width:120px;height:auto;border-radius:6px;\" />"
        return ""

    thumbnail_tag.short_description = "Thumbnail"
    thumbnail_tag.allow_tags = True
