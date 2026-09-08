from django.test import TestCase
from .models import Student


class StudentTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="Test Student",
            marks=90,
            department="Computer"
        )

        self.assertEqual(student.name, "Test Student")
        self.assertEqual(student.marks, 90)
        self.assertEqual(student.department, "Computer")