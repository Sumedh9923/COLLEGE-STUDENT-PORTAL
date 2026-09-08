# 🎓 College Student Portal

A web-based **College Student Portal** developed using **Python and Django** for managing student records efficiently. The application provides a clean and modern interface for performing CRUD operations such as adding, viewing, searching, editing, and deleting student records.

---

## 📌 Project Overview

The College Student Portal is designed to simplify the management of student information in a college environment.

The system stores important student details such as:

- Student Name
- Marks
- Department

Users can manage student records through an easy-to-use web interface. The project also includes a **High Scorers** section that displays students who have achieved **80 marks or above**.

The project demonstrates the practical implementation of **Django web development, database management, CRUD operations, Django ORM, authentication through Django Admin, testing, Git, and GitHub**.

---

## 🎯 Objectives

The main objectives of this project are:

1. To develop a web-based student management system.
2. To implement CRUD operations using Django.
3. To store and manage student information in a database.
4. To provide search functionality for student records.
5. To display high-performing students.
6. To integrate Django Admin for database management.
7. To implement CSRF protection for secure form submissions.
8. To perform automated testing using Django's testing framework.
9. To use Git and GitHub for version control and project management.
10. To create a responsive and user-friendly interface.

---

## ✨ Features

### 👨‍🎓 Student Management

- Add new student records
- View all students
- Edit existing student information
- Delete student records
- Search students by name or department

### 🏆 High Scorers

The application includes a dedicated **High Scorers** section that displays students who have scored **80 marks or above**.

### 🛠️ Django Admin

Django Admin is integrated to provide an administrative interface for managing student records.

Admin features include:

- Student record management
- Search functionality
- Department filtering
- Marks-based ordering

### 🔐 Security

The project uses Django's built-in **CSRF protection** for POST form submissions.

### 🧪 Testing

Automated tests are included using Django's built-in testing framework to verify student record creation.

### 🎨 Modern UI

The project includes:

- Responsive layout
- Modern navigation bar
- Dashboard-style cards
- Student table
- Search interface
- High-scorer cards
- Edit and delete actions
- Mobile-friendly design

---

## 💻 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| SQLite | Database |
| Django ORM | Database operations |
| Django Admin | Administrative management |
| Django Test Framework | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| Visual Studio Code | Development environment |

---

## 📂 Project Structure

```text
college_portal/
│
├── manage.py
│
├── college_portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── static/
│   │   └── students/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── students/
│   │       ├── home.html
│   │       ├── student_list.html
│   │       ├── add_student.html
│   │       ├── search.html
│   │       ├── high_scorers.html
│   │       └── edit_student.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
└── README.md
````

> **Note:** `db.sqlite3` may be excluded from GitHub using `.gitignore` depending on the project configuration.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sumedh9923/COLLEGE-STUDENT-PORTAL.git
```

### 2. Navigate to the Project

```bash
cd COLLEGE-STUDENT-PORTAL
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create the administrator account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🌐 Application URLs

| URL              | Function          |
| ---------------- | ----------------- |
| `/`              | Home page         |
| `/students/`     | View all students |
| `/add/`          | Add a student     |
| `/search/`       | Search students   |
| `/high-scorers/` | View high scorers |
| `/admin/`        | Django Admin      |
| `/edit/<id>/`    | Edit student      |
| `/delete/<id>/`  | Delete student    |

---

## 🗄️ Student Model

The main `Student` model contains the following fields:

| Field        | Description                   |
| ------------ | ----------------------------- |
| `name`       | Name of the student           |
| `marks`      | Marks obtained by the student |
| `department` | Student's department          |

---

## 🔄 CRUD Operations

The project implements all four major CRUD operations.

### Create

Users can add new student records through the **Add Student** page.

### Read

Users can view all available student records through the **Students** page.

### Update

Existing student information can be modified using the **Edit** option.

### Delete

Student records can be removed using the **Delete** option.

---

## 🔎 Search Functionality

The search feature allows users to search student records using a search query.

Students can be searched based on information such as:

* Name
* Department

---

## 🏆 High Scorers

The High Scorers page filters students based on their marks.

Students with:

```text
Marks >= 80
```

are displayed in the High Scorers section.

---

## 🧪 Testing

The project includes automated testing using Django's built-in testing framework.

Run the tests using:

```bash
python manage.py test
```

The test verifies that a student record can be successfully created and that its information is stored correctly.

---

## 🔍 System Check

Django's system check can be performed using:

```bash
python manage.py check
```

This verifies that the project configuration does not contain any major Django configuration issues.

---

## 🌿 Git & Version Control

Git was used to manage the development history of the project.

Important Git commands used during development include:

```bash
git status
git add .
git commit -m "Commit message"
git branch
git switch -c feature/student-crud
git merge feature/student-crud
git remote -v
git push -u origin main
```

The project was developed using a feature branch for student CRUD functionality and subsequently merged into the `main` branch.

---

## 📸 Project Screens

The application contains the following main sections:

* 🏠 Home Dashboard
* 👨‍🎓 Student List
* ➕ Add Student
* 🔎 Search Student
* 🏆 High Scorers
* ✏️ Edit Student
* 🛠️ Django Admin

Screenshots can be added to this README to demonstrate the user interface.

---

## 🚀 Future Enhancements

The project can be further improved by adding:

* Student login and registration
* Faculty login
* Role-based access control
* Student profile pages
* Attendance management
* Subject-wise marks
* Grade calculation
* Result generation
* PDF report generation
* PostgreSQL/MySQL database support
* REST API
* Cloud deployment
* Student profile photographs
* Advanced dashboard analytics

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented and practiced:

* Python programming
* Django framework
* Django project and app structure
* Models and databases
* Django ORM
* URL routing
* Views
* Templates
* HTML and CSS
* CRUD operations
* Django Admin
* Form handling
* CSRF protection
* Automated testing
* Git branching
* Git merging
* GitHub repository management

---

## 👨‍💻 Developer

**Sumedh Patil**

### Project

**College Student Portal**

### Repository

[GitHub Repository](https://github.com/Sumedh9923/COLLEGE-STUDENT-PORTAL)

---

## 📄 License

This project was developed for educational and academic purposes.

---

⭐ **If you find this project useful, consider giving the repository a star!**

````

### ⚠️ One small correction before you add it

Because your `.gitignore` contains:

```text
db.sqlite3
````

your GitHub repository **should not contain `db.sqlite3`** unless it was already committed before the `.gitignore` rule was added. That's actually fine for a Django project—when someone clones it, they can run:

```powershell
python manage.py migrate
```

to create a fresh database.