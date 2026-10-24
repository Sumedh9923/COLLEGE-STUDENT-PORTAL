from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "marks",
        "grade",
        "department",
        "attendance",
        "attendance_status",
    )

    search_fields = ("name", "department")

    list_filter = ("department",)

    ordering = ("-marks",)

    list_per_page = 20
