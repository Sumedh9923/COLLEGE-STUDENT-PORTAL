
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student


class StudentTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="Test Student",
            marks=90,
            department="Computer",
            attendance=85,
        )

        self.assertEqual(student.name, "Test Student")
        self.assertEqual(student.marks, 90)
        self.assertEqual(student.department, "Computer")
        self.assertEqual(student.attendance, 85)
        self.assertEqual(student.grade, "A+")

    def test_attendance_status(self):
        student = Student.objects.create(
            name="Attendance Test",
            marks=75,
            department="IT",
            attendance=95,
        )

        self.assertEqual(student.attendance_status, "Excellent")

    def test_login_required_for_student_list(self):
        response = self.client.get(reverse("student_list"))

        self.assertEqual(response.status_code, 302)

    def test_login_required_for_add_student(self):
        response = self.client.get(reverse("add_student"))

        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_can_open_student_list(self):
        User.objects.create_user(
            username="testuser",
            password="TestPass123!",
        )
        self.client.login(
            username="testuser",
            password="TestPass123!",
        )

        response = self.client.get(reverse("student_list"))

        self.assertEqual(response.status_code, 200)

    def test_analytics_page_requires_login(self):
        response = self.client.get(reverse("analytics"))

        self.assertEqual(response.status_code, 302)
