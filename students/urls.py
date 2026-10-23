from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.student_list, name="student_list"),
    path("add/", views.add_student, name="add_student"),
    path("search/", views.search_student, name="search_student"),
    path("high-scorers/", views.high_scorers, name="high_scorers"),
    path("edit/<int:id>/", views.edit_student, name="edit_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    path("analytics/", views.analytics, name="analytics"),
    path("student/<int:id>/", views.student_profile, name="student_profile"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("export/", views.export_students, name="export_students"),
]