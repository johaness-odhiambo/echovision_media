from django.db import models


class GalleryItem(models.Model):
    MEDIA_IMAGE = "image"
    MEDIA_VIDEO = "video"

    MEDIA_CHOICES = [
        (MEDIA_IMAGE, "Image"),
        (MEDIA_VIDEO, "Video"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)
    file = models.FileField(upload_to="gallery/")
    poster_image = models.ImageField(upload_to="gallery/posters/", blank=True, null=True)
    service = models.ForeignKey(
        "appointments.Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gallery_items",
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
