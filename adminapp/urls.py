from . import views
from django.urls import path

app_name ='adminapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('branch',views.branch,name="branch"),
    path('addbranch',views.add_branch,name="addbranch"),
    path('teachers',views.teachers,name="teachers"),
    path('teacherslist',views.teachers_list,name="teacherslist"),
    path('addteacher',views.add_teachers,name="addteacher"),
    path('exams',views.exams,name="exams"),
    path('students',views.students,name="students"),
    path('coursestudents',views.students_by_courses,name="coursestudents"),
    path('studentslist',views.students_list,name="studentslist"),
    path('addstudent',views.add_student,name="addstudent"),




]