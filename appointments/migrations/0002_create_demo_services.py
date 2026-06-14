from django.db import migrations


def create_demo_services(apps, schema_editor):
    from decimal import Decimal

    Service = apps.get_model("appointments", "Service")

    demo_services = [
        {
            "name": "Photography",
            "slug": "photography",
            "description": "High-quality event and studio photography for all occasions.",
            "price": Decimal("150.00"),
            "duration_minutes": 120,
            "is_active": True,
        },
        {
            "name": "Videography",
            "slug": "videography",
            "description": "Professional video shooting and editing for events and ads.",
            "price": Decimal("200.00"),
            "duration_minutes": 180,
            "is_active": True,
        },
        {
            "name": "Music Production",
            "slug": "music-production",
            "description": "Studio recording, mixing, and mastering with industry-standard tools.",
            "price": Decimal("120.00"),
            "duration_minutes": 90,
            "is_active": True,
        },
        {
            "name": "Live Streaming",
            "slug": "live-streaming",
            "description": "Creative live streaming and live event coverage services.",
            "price": Decimal("180.00"),
            "duration_minutes": 180,
            "is_active": True,
        },
    ]

    for svc in demo_services:
        Service.objects.update_or_create(slug=svc["slug"], defaults=svc)


class Migration(migrations.Migration):

    dependencies = [("appointments", "0001_initial")]

    operations = [migrations.RunPython(create_demo_services, reverse_code=migrations.RunPython.noop)]
