from datetime import timedelta
from django import forms
from django.utils import timezone

from .models import Appointment

BUSINESS_START_HOUR = 8
BUSINESS_END_HOUR = 18

class AppointmentCreateForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", 'class': 'form-control'}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Appointment
        fields = ["scheduled_at", "notes"]

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop('service', None)
        super().__init__(*args, **kwargs)
        self.fields['notes'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 4})

    def clean_scheduled_at(self):
        scheduled_at = self.cleaned_data["scheduled_at"]
        
        if scheduled_at < timezone.now():
            raise forms.ValidationError("Please choose a future time.")
            
        local_time = timezone.localtime(scheduled_at)
        if not (BUSINESS_START_HOUR <= local_time.hour < BUSINESS_END_HOUR):
            raise forms.ValidationError(f"Please select a time within business hours ({BUSINESS_START_HOUR}:00 - {BUSINESS_END_HOUR}:00).")

        if self.service:
            end_time = scheduled_at + timedelta(minutes=self.service.duration_minutes)
            start_buffer = scheduled_at - timedelta(minutes=self.service.duration_minutes)
            
            conflicts = Appointment.objects.filter(
                service=self.service,
                status=Appointment.STATUS_CONFIRMED,
                scheduled_at__lt=end_time,
                scheduled_at__gt=start_buffer
            )
            if conflicts.exists():
                raise forms.ValidationError("This time slot overlaps with an existing booking. Please select another time.")

        return scheduled_at
