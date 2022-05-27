from django.urls import path
from . import views

app_name = 'branch'

urlpatterns = [
    path('',views.master,name="master"),
    path('students',views.students,name="branchstudents"),
    path('studentslist',views.studentslist,name="branchstudentslist"),
    path('allstudentslist',views.all_students_list,name="allbranchstudentslist"),
    path('addstudent',views.add_students_branch,name="addstudent"),
    path('editstudent/<str:id>',views.editstudent,name="editstudent"),
    path('teacherslist',views.teachers,name="teacherslist"),
    path('addteacher',views.add_teachers,name="addteacherbranch"),
    path('editteacher/<str:id>',views.editteacher,name="editteacher"),
    path('courses',views.courses,name="courses"),
    path('addcourses',views.add_courses,name="addcourses"),
    path('fees',views.fees,name="fees"),
    path('addfees',views.add_fees,name="addfees"),

    # Exams

    path('examlist', views.exam_list, name="examlist"),
    path('examaddbone', views.exam_add_b_one, name="examaddbone"),
    path('examaddbtwo', views.exam_add_b_two, name="examaddbtwo"),
    path('examaddbthree', views.exam_add_b_Three, name="examaddbthree"),




    # profile

    path('branchprofile',views.profile_branch, name="branchprofile")



]