from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "marks", "department")
    search_fields = ("name", "department")
    list_filter = ("department",)
    ordering = ("-marks",)