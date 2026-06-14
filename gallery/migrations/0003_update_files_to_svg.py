from django.db import migrations


def update_files_to_svg(apps, schema_editor):
    GalleryItem = apps.get_model("gallery", "GalleryItem")

    mapping = {
        "Studio Portraits": "gallery/studio_portraits.svg",
        "Event Highlights": "gallery/event_highlights.svg",
        "Studio Session": "gallery/studio_session.svg",
        "Live Stream Sample": "gallery/live_stream.svg",
    }

    for title, path in mapping.items():
        try:
            item = GalleryItem.objects.filter(title=title).first()
            if item:
                item.file = path
                item.save(update_fields=["file"])
        except Exception:
            # ignore errors during data migration
            pass


class Migration(migrations.Migration):

    dependencies = [("gallery", "0002_create_demo_items")]

    operations = [migrations.RunPython(update_files_to_svg, reverse_code=migrations.RunPython.noop)]
