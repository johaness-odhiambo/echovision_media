from django.db import migrations


def set_posters(apps, schema_editor):
    GalleryItem = apps.get_model("gallery", "GalleryItem")

    poster_map = {
        "Studio Portraits": "gallery/posters/studio_portraits_poster.svg",
        "Event Highlights": "gallery/posters/event_highlights_poster.svg",
        "Studio Session": "gallery/posters/studio_session_poster.svg",
        "Live Stream Sample": "gallery/posters/live_stream_poster.svg",
    }

    for title, poster_path in poster_map.items():
        try:
            item = GalleryItem.objects.filter(title=title).first()
            if item:
                item.poster_image = poster_path
                item.save(update_fields=["poster_image"])
        except Exception:
            pass


class Migration(migrations.Migration):

    dependencies = [("gallery", "0003_update_files_to_svg")]

    operations = [migrations.RunPython(set_posters, reverse_code=migrations.RunPython.noop)]
