from django.db import migrations


def create_demo_gallery(apps, schema_editor):
    GalleryItem = apps.get_model("gallery", "GalleryItem")
    Service = apps.get_model("appointments", "Service")

    mapping = [
        {
            "title": "Studio Portraits",
            "description": "A selection of our best studio portrait work.",
            "media_type": "image",
            "file": "gallery/studio_portraits.jpg",
            "service_slug": "photography",
            "is_featured": True,
        },
        {
            "title": "Event Highlights",
            "description": "Clips and stills from recent events and weddings.",
            "media_type": "image",
            "file": "gallery/event_highlights.jpg",
            "service_slug": "videography",
            "is_featured": True,
        },
        {
            "title": "Studio Session",
            "description": "Behind the scenes from a music production session.",
            "media_type": "image",
            "file": "gallery/studio_session.jpg",
            "service_slug": "music-production",
            "is_featured": False,
        },
        {
            "title": "Live Stream Sample",
            "description": "Screenshot from a live streaming event.",
            "media_type": "image",
            "file": "gallery/live_stream.jpg",
            "service_slug": "live-streaming",
            "is_featured": False,
        },
    ]

    for item in mapping:
        service = None
        try:
            service = Service.objects.filter(slug=item["service_slug"]).first()
        except Exception:
            service = None

        GalleryItem.objects.update_or_create(
            title=item["title"],
            defaults={
                "description": item["description"],
                "media_type": item["media_type"],
                "file": item["file"],
                "service_id": service.id if service else None,
                "is_featured": item["is_featured"],
            },
        )


class Migration(migrations.Migration):

    dependencies = [("gallery", "0001_initial"), ("appointments", "0001_initial")]

    operations = [migrations.RunPython(create_demo_gallery, reverse_code=migrations.RunPython.noop)]
