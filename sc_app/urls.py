from django.urls import path

from sc_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login_page", views.login_page, name="login_page"),
    path("logout_view", views.logout_view, name="logout_view"),
    ######ADMIN######
    path("admin_base", views.admin_base, name="admin_base"),
    path("students_data", views.students_data, name="students_data"),
    path("add_notification", views.add_notification, name="add_notification"),
    path("view_notification_admin", views.view_notification_admin, name="view_notification_admin"),
    path("view_complaint_admin", views.view_complaint_admin, name="view_complaint_admin"),
    path("reply_complaint/<int:id>/", views.reply_complaint, name="reply_complaint"),

    ########STUDENT#####
    path("student_base", views.student_base, name="student_base"),
    path("student_registration", views.student_registration, name="student_registration"),
    path("add_complaint_student", views.add_complaint_student, name="add_complaint_student"),
    path("view_complaint", views.view_complaint, name="view_complaint"),
    path("view_notification_student", views.view_notification_student, name="view_notification_student"),
    path("students_dataview_student", views.students_dataview_student, name="students_dataview_student"),

]