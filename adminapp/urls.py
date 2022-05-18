from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('',views.admindashbord,name="admindash"),
    path('branch',views.branch_list,name='branch'),
    # path('adminhome',views.admindashbord,name='admindash'),
    # path('branches',views.branch_list,name="branches"),
    # path('addbranch',views.add_branch,name="addbranch"),
    # path('teachers',views.teachers,name="teachers"),
    # path('teacherslist',views.teachers_list,name="teacherslist"),
    # path('addteacher',views.add_teachers,name="addteacher"),
    # path('exams',views.exams,name="exams"),
    # path('students',views.students,name="students"),
    # path('coursestudents',views.students_by_courses,name="coursestudents"),
    # path('studentslist',views.students_list,name="studentslist"),
    # path('addstudent',views.add_student,name="addstudent"),




]