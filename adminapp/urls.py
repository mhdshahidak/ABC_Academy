from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('',views.admindashbord,name="admindash"),
    path('branch',views.branch_list,name='branch'),
    path('addbranch',views.add_branch,name="addbranch"),
    path('branchcourse',views.branch_course,name="branchcourse"),
    path('teachers',views.teachers,name="teachers"),
    path('teachers_list',views.teachers_list,name="teachers_list"),
    path('add_teacher',views.add_teacher,name="addteacher"),
    path('students',views.students,name="students"),
    path('coursestudents',views.students_by_courses,name="coursestudents"),
    path('studentslist',views.students_list,name="studentslist"),
    path('addstudent',views.add_student,name="addstudent"),

    # exams

    path('exams',views.exam,name="exams"),
    path('examsadd',views.exam_add_list,name="examsadd"),
    path('examsaddone',views.exam_add_one,name="examsaddone"),


    #fees admin

    path('feesadding',views.fees_adding,name="feesadding"),





    # login
    
    path('login', views.login,name="adminlogin"),
   




]