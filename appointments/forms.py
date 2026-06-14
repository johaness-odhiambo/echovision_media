from django import forms
from django.utils import timezone

from .models import Appointment


class AppointmentCreateForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", 'class': 'form-control'}),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Appointment
        fields = ["service", "scheduled_at", "notes"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 4})

    def clean_scheduled_at(self):
        scheduled_at = self.cleaned_data["scheduled_at"]
        if scheduled_at < timezone.now():
            raise forms.ValidationError("Please choose a future time.")
        return scheduled_at
