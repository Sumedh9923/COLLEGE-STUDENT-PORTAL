# College Student Portal

A Django-based web application for managing student records, academic performance, and attendance.

## Features

- Student dashboard with summary statistics
- Add, view, edit, and delete student records
- Student search, filtering, and sorting
- Automatic grade calculation based on marks
- Attendance tracking and attendance status
- Analytics for grades, departments, and attendance
- Login protection for student-management pages
- CSV export with academic and attendance details
- Django Admin integration
- Automated tests

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
college_portal/
├── manage.py
├── requirements.txt
├── college_portal/
└── students/
    ├── migrations/
    ├── templates/
    ├── static/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── tests.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sumedh9923/COLLEGE-STUDENT-PORTAL.git
cd COLLEGE-STUDENT-PORTAL
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

### 6. Run the application

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

The Django Admin panel is available at http://127.0.0.1:8000/admin/.

## Run Tests

```bash
python manage.py test students
```

## Academic Project

This project demonstrates Django web development, database operations, authentication, data validation, reporting, and automated testing.

## Author

**Sumedh Narayan Patil**

- GitHub: https://github.com/Sumedh9923
- LinkedIn: https://www.linkedin.com/in/sumedh-patil-16b637275/
