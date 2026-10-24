import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg, Max, Min, Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student

def home(request):
    total_students = Student.objects.count()
    high_scorers_count = Student.objects.filter(marks__gte=80).count()

    average_marks = Student.objects.aggregate(
        average=Avg("marks")
    )["average"]

    total_departments = Student.objects.values(
        "department"
    ).distinct().count()

    context = {
        "total_students": total_students,
        "high_scorers_count": high_scorers_count,
        "average_marks": round(average_marks, 2) if average_marks else 0,
        "total_departments": total_departments,
    }

    return render(
        request,
        "students/home.html",
        context
    )


def student_list(request):
    students = Student.objects.all().order_by("-marks")

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )



@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        department = request.POST.get("department", "").strip()

        try:
            marks = float(request.POST.get("marks", ""))
            attendance = float(request.POST.get("attendance", ""))
        except (ValueError, TypeError):
            return render(
                request,
                "students/add_student.html",
                {"error": "Marks and attendance must be valid numbers."},
            )

        if not name or not department:
            return render(
                request,
                "students/add_student.html",
                {"error": "Name and department are required."},
            )

        if not 0 <= marks <= 100:
            return render(
                request,
                "students/add_student.html",
                {"error": "Marks must be between 0 and 100."},
            )

        if not 0 <= attendance <= 100:
            return render(
                request,
                "students/add_student.html",
                {"error": "Attendance must be between 0 and 100."},
            )

        Student.objects.create(
            name=name,
            marks=marks,
            department=department,
            attendance=attendance,
        )

        return redirect("student_list")

    return render(request, "students/add_student.html")


@login_required
def search_student(request):
    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    min_marks = request.GET.get("min_marks", "")
    max_marks = request.GET.get("max_marks", "")
    sort = request.GET.get("sort", "marks_desc")

    students = Student.objects.all()

    if query:
        students = students.filter(
            name__icontains=query
        )

    if department:
        students = students.filter(
            department__iexact=department
        )

    if min_marks:
        students = students.filter(
            marks__gte=min_marks
        )

    if max_marks:
        students = students.filter(
            marks__lte=max_marks
        )

    if sort == "marks_asc":
        students = students.order_by("marks")
    elif sort == "name_asc":
        students = students.order_by("name")
    elif sort == "name_desc":
        students = students.order_by("-name")
    else:
        students = students.order_by("-marks")

    departments = (
        Student.objects
        .values_list("department", flat=True)
        .distinct()
        .order_by("department")
    )

    context = {
        "students": students,
        "query": query,
        "department": department,
        "min_marks": min_marks,
        "max_marks": max_marks,
        "departments": departments,
        "sort": sort,
    }

    return render(
        request,
        "students/search.html",
        context
    )


def high_scorers(request):
    students = Student.objects.filter(
        marks__gte=80
    ).order_by("-marks")

    return render(
        request,
        "students/high_scorers.html",
        {"students": students}
    )


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        department = request.POST.get("department", "").strip()

        try:
            marks = float(request.POST.get("marks", ""))
            attendance = float(request.POST.get("attendance", ""))
        except (ValueError, TypeError):
            return render(
                request,
                "students/edit_student.html",
                {
                    "student": student,
                    "error": "Marks and attendance must be valid numbers.",
                },
            )

        if not name or not department:
            return render(
                request,
                "students/edit_student.html",
                {
                    "student": student,
                    "error": "Name and department are required.",
                },
            )

        if not 0 <= marks <= 100:
            return render(
                request,
                "students/edit_student.html",
                {
                    "student": student,
                    "error": "Marks must be between 0 and 100.",
                },
            )

        if not 0 <= attendance <= 100:
            return render(
                request,
                "students/edit_student.html",
                {
                    "student": student,
                    "error": "Attendance must be between 0 and 100.",
                },
            )

        student.name = name
        student.marks = marks
        student.department = department
        student.attendance = attendance
        student.save()

        return redirect("student_list")

    return render(
        request,
        "students/edit_student.html",
        {"student": student},
    )


@login_required
def delete_student(request, id):
    if request.method != "POST":
        return redirect("student_list")

    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect("student_list")

@login_required
def analytics(request):
    total_students = Student.objects.count()

    average_marks = Student.objects.aggregate(
        average=Avg("marks")
    )["average"]

    highest_marks = Student.objects.aggregate(
        highest=Max("marks")
    )["highest"]

    lowest_marks = Student.objects.aggregate(
        lowest=Min("marks")
    )["lowest"]

    high_scorers_count = Student.objects.filter(
        marks__gte=80
    ).count()

    average_attendance = Student.objects.aggregate(
        average=Avg("attendance")
    )["average"]

    excellent_attendance_count = Student.objects.filter(
        attendance__gte=90
    ).count()

    low_attendance_count = Student.objects.filter(
        attendance__lt=60
    ).count()

    departments = (
        Student.objects
        .values("department")
        .annotate(
            student_count=Count("id"),
            average_marks=Avg("marks")
        )
        .order_by("-average_marks")
    )

    grade_distribution = {
        "A+": Student.objects.filter(marks__gte=90).count(),
        "A": Student.objects.filter(marks__gte=80, marks__lt=90).count(),
        "B+": Student.objects.filter(marks__gte=70, marks__lt=80).count(),
        "B": Student.objects.filter(marks__gte=60, marks__lt=70).count(),
        "C": Student.objects.filter(marks__gte=50, marks__lt=60).count(),
        "D": Student.objects.filter(marks__gte=40, marks__lt=50).count(),
        "F": Student.objects.filter(marks__lt=40).count(),
    }

    grade_chart = [
        {
            "grade": grade,
            "count": count,
            "percentage": round(count / total_students * 100)
            if total_students else 0,
        }
        for grade, count in grade_distribution.items()
    ]

    for department in departments:
        department["percentage"] = (
            round(department["student_count"] / total_students * 100)
            if total_students else 0
        )
            
    context = {
        "total_students": total_students,
        "average_marks": round(average_marks, 2) if average_marks else 0,
        "highest_marks": highest_marks if highest_marks is not None else 0,
        "lowest_marks": lowest_marks if lowest_marks is not None else 0,
        "high_scorers_count": high_scorers_count,
        "departments": departments,
        "grade_distribution": grade_distribution,
        "average_attendance": round(average_attendance, 2) if average_attendance else 0,
        "excellent_attendance_count": excellent_attendance_count,
        "low_attendance_count": low_attendance_count,
        "grade_chart": grade_chart,
    }

    return render(
        request,
        "students/analytics.html",
        context
    )

def student_profile(request, id):
    student = get_object_or_404(Student, id=id)

    return render(
        request,
        "students/student_profile.html",
        {"student": student}
    )

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(
            request,
            "students/login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "students/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def export_students(request):
    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    min_marks = request.GET.get("min_marks", "")
    max_marks = request.GET.get("max_marks", "")
    sort = request.GET.get("sort", "marks_desc")

    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    if department:
        students = students.filter(department__iexact=department)

    if min_marks:
        students = students.filter(marks__gte=min_marks)

    if max_marks:
        students = students.filter(marks__lte=max_marks)

    if sort == "marks_asc":
        students = students.order_by("marks")
    elif sort == "name_asc":
        students = students.order_by("name")
    elif sort == "name_desc":
        students = students.order_by("-name")
    else:
        students = students.order_by("-marks")

    response = HttpResponse(
        content_type="text/csv"
    )

    response["Content-Disposition"] = (
        'attachment; filename="student_data.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        "ID",
        "Name",
        "Marks",
        "Grade",
        "Department"
    ])

    for student in students:
        writer.writerow([
            student.id,
            student.name,
            student.marks,
            student.grade,
            student.department
        ])

    return response