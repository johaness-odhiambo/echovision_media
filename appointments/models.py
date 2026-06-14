from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=220, unique=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	duration_minutes = models.PositiveIntegerField(default=60)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["name"]

	def __str__(self) -> str:
		return self.name


class Appointment(models.Model):
	STATUS_PENDING = "pending"
	STATUS_CONFIRMED = "confirmed"
	STATUS_CANCELLED = "cancelled"
	STATUS_COMPLETED = "completed"

	STATUS_CHOICES = [
		(STATUS_PENDING, "Pending"),
		(STATUS_CONFIRMED, "Confirmed"),
		(STATUS_CANCELLED, "Cancelled"),
		(STATUS_COMPLETED, "Completed"),
	]

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.PROTECT)
	scheduled_at = models.DateTimeField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-scheduled_at"]

	def __str__(self) -> str:
		return f"{self.service} - {self.scheduled_at:%Y-%m-%d %H:%M}"

	@property
	def is_past(self) -> bool:
		return self.scheduled_at < timezone.now()
