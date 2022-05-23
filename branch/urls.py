from django.urls import path
from . import views

app_name = 'branch'

urlpatterns = [
    path('',views.master,name="master"),
    path('students',views.students,name="branchstudents"),
    path('studentslist',views.studentslist,name="branchstudentslist"),
    path('allstudentslist',views.all_students_list,name="allbranchstudentslist"),
    path('addstudent',views.add_students_branch,name="addstudent"),
    path('teacherslist',views.teachers,name="teacherslist"),
    path('addteacher',views.add_teachers,name="addteacherbranch"),
    path('courses',views.courses,name="courses"),
    path('addcourses',views.add_courses,name="addcourses"),


]