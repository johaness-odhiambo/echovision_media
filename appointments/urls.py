from django.urls import path

from .views import (
    appointment_create,
    appointment_detail,
    appointment_list,
    service_detail,
    service_list,
)

urlpatterns = [
    path("", service_list, name="services"),
    path("services/<slug:slug>/", service_detail, name="service_detail"),
    path("book/<slug:slug>/", appointment_create, name="appointment_create"),
    path("appointments/", appointment_list, name="appointment_list"),
    path("appointments/<int:appointment_id>/", appointment_detail, name="appointment_detail"),
]
