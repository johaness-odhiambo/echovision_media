from django.shortcuts import render


def index(request):
    """Simple services index page."""
    return render(request, "services/index.html")
