from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import AppointmentCreateForm
from .models import Appointment, Service

def _send_booking_email(appointment: Appointment):
    if not settings.EMAIL_HOST:
        return

    recipients = []
    if appointment.user.email:
        recipients.append(appointment.user.email)
    if settings.BOOKING_NOTIFICATION_EMAIL:
        recipients.append(settings.BOOKING_NOTIFICATION_EMAIL)
    if not recipients:
        return

    subject = f"Booking {appointment.status.title()} - {appointment.service.name}"
    message = (
        f"Your booking for {appointment.service.name} on "
        f"{timezone.localtime(appointment.scheduled_at):%Y-%m-%d %H:%M} is "
        f"{appointment.status}."
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)


def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "appointments/service_list.html", {"services": services})


def service_detail(request, slug: str):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    return render(request, "appointments/service_detail.html", {"service": service})


@login_required
def appointment_create(request, slug: str):
    service = get_object_or_404(Service, slug=slug, is_active=True)

    if request.method == "POST":
        form = AppointmentCreateForm(request.POST, service=service)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.service = service
            appointment.status = Appointment.STATUS_CONFIRMED

            appointment.save()
            _send_booking_email(appointment)

            messages.success(request, "Booking created and confirmed.")
            return redirect("appointment_detail", appointment_id=appointment.id)
    else:
        form = AppointmentCreateForm(service=service)

    return render(
        request,
        "appointments/appointment_form.html",
        {"form": form, "service": service},
    )


@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user).select_related("service")
    return render(
        request,
        "appointments/appointment_list.html",
        {"appointments": appointments},
    )


@login_required
def appointment_detail(request, appointment_id: int):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        user=request.user,
    )
    return render(
        request,
        "appointments/appointment_detail.html",
        {"appointment": appointment},
    )
