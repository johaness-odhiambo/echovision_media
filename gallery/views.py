from django.shortcuts import render

from .models import GalleryItem


def gallery_list(request):
    items = GalleryItem.objects.select_related("service").all()
    return render(request, "gallery/gallery_list.html", {"items": items})
