from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    department = models.CharField(max_length=50)
    attendance = models.FloatField(default=75)

    @property
    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B+"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def __str__(self):
        return self.name

    @property
    def attendance_status(self):
        if self.attendance >= 90:
            return "Excellent"
        elif self.attendance >= 75:
            return "Good"
        elif self.attendance >= 60:
            return "Average"
        else:
            return "Low"