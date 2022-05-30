from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('', views.admindashbord, name="admindash"),
    path('branch', views.branch_list, name='branch'),

    # add branch 
    path('addbranch', views.add_branch, name="addbranch"),
    path('branchcourse', views.branch_course, name="branchcourse"),

    # teacher 
    path('teachers', views.teachers, name="teachers"),
    path('teachers_list/<int:id>', views.teachers_list, name="teachers_list"),
    path('add_teacher', views.add_teacher, name="addteacher"),
    path('students', views.students,name="students"),
    path('coursestudents',  views.students_by_courses, name="coursestudents"),
    path('studentslist', views.students_list, name="studentslist"),
    path('addstudent', views.add_student, name="addstudent"),
    path('editstudent', views.edit_student_by_admin, name="editstudentadmin"),

    # courses
    path('courses',views.courses,name="courses"),
    path('addcourses',views.add_courses,name="addcourses"),

    # batch
    path('batch', views.batch, name="batch"),
    path('addbatch', views.add_batch, name="addbatch"),
    # exams

    path('exams', views.exam, name="exams"),
    path('examsadd/<int:id>', views.exam_add_list, name="examsadd"),
    path('examsaddfirst/<int:id>', views.exam_add_first, name="examsaddfirst"),
    path('examsaddone/<str:id>', views.exam_add_one, name="examsaddone"),
    path('examsaddtwo/<str:id>', views.exam_add_two, name="examsaddtwo"),
    path('savedata/', views.savedata, name="savedata"),

   # profile

   path('profile', views.admin_profile, name="adminprofile"),

    # fees admin

    path('feesadding', views.fees_adding,name="feesadding"),



    # login
    
    path('login', views.log_in,name="adminlogin"),
    path('logout_view', views.logout_view,name="logout_view"),
   

]