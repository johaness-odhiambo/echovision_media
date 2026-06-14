from django.contrib import admin

from .models import Appointment, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ("name", "price", "duration_minutes", "is_active", "created_at")
	list_filter = ("is_active",)
	prepopulated_fields = {"slug": ("name",)}
	search_fields = ("name", "description")
	ordering = ("name",)
	list_editable = ("price", "is_active")
	list_display_links = ("name",)
	date_hierarchy = "created_at"

	def make_active(self, request, queryset):
		queryset.update(is_active=True)
	make_active.short_description = "Mark selected services as active"

	def make_inactive(self, request, queryset):
		queryset.update(is_active=False)
	make_inactive.short_description = "Mark selected services as inactive"

	actions = ("make_active", "make_inactive")

	# show related appointments inline for quick context
	class AppointmentInline(admin.TabularInline):
		model = Appointment
		extra = 0
		fields = ("user", "scheduled_at", "status")
		readonly_fields = ("user", "scheduled_at", "status")

	inlines = (AppointmentInline,)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ("service", "user", "scheduled_at", "status")
	list_filter = ("status", "service")
	search_fields = ("user__username", "user__email", "service__name")
	date_hierarchy = "scheduled_at"
	list_editable = ("status",)
	list_display_links = ("service", "user")
