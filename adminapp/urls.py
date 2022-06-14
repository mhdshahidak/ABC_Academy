from django.urls import path
from . import views

app_name='admins'

urlpatterns = [
    path('', views.admindashbord, name="admindash"),
    path('branch', views.branch_list, name='branch'),

    # add branch 
    path('addbranch', views.add_branch, name="addbranch"),
    path('branchcourse/<int:id>', views.branch_course, name="branchcourse"),

    # teacher 
    path('teachers', views.teachers, name="teachers"),
    path('teachers_list/<int:id>', views.teachers_list, name="teachers_list"),
    path('add_teacher', views.add_teacher, name="addteacher"),
    path('deleteteacher/<int:id>',views.delete_teacher,name="deleteteacher"),

    # student

    path('students', views.students,name="students"),
    path('coursestudents/<int:id>',  views.students_by_courses, name="coursestudents"),
    path('studentslist', views.students_list, name="studentslist"),
    path('addstudent', views.add_student, name="addstudent"),
    path('editstudent/<int:id>', views.edit_student_by_admin, name="editstudentadmin"),
    path('studentbatchlish/<int:id>/<int:bid>', views.studentbatchlish, name="studentbatchlish"),
    # path('deletestudent/<int:id>',views.delete_student,name="deletestudent"),

    

    # courses
    path('courses',views.courses,name="courses"),
    path('addcourses',views.add_courses,name="addcourses"),
    path('editcourse/<int:id>',views.edit_course,name="editcourse"),

    # batch
    path('batch', views.batch, name="batch"),
    path('addbatch', views.add_batch, name="addbatch"),
    path('editbatch/<int:id>',views.edit_batch,name="editbatch"),
    # exams

    path('exams', views.exam, name="exams"),
    path('examsadd/<int:id>', views.exam_add_list, name="examsadd"),
    path('examsaddfirst/<int:id>', views.exam_add_first, name="examsaddfirst"),
    path('examsaddone/<str:id>', views.exam_add_one, name="examsaddone"),
    path('examsaddtwo/<str:id>', views.exam_add_two, name="examsaddtwo"),
    path('savedata/', views.savedata, name="savedata"),
    path('updateQuestion/', views.updateQuestion, name="updateQuestion"),
    path('editQuestiontdata/<int:id>',views.editQuestiontdata,name="editQuestiontdata"),
    path('editexamdata/<int:id>',views.editExam,name="editexamdata"),


    # result

    path('resultbatch', views.result_batch,name="resultbatch"),
    path('resultexam/<int:id>', views.result_exam,name="resultexam"),
    path('result/<int:id>/<int:bid>', views.result,name="result"),
    path('checkresult/<int:eid>/<int:sid>', views.checkresult,name="checkresult"),

    # Exam rechedule

    path('reschedule', views.reschedule, name="reschedule"),
    path('reschedulelist/<int:id>', views.reschedule_list, name="reschedulelist"),
    path('reschedulelistdelete/<int:id>', views.delete_schedule_status, name="reschedulelistdelete"),


   # profile

   path('profile', views.admin_profile, name="adminprofile"),

    # fees admin

    path('feesadding', views.fees_adding,name="feesadding"),
    path('getdatapayment', views.getdatapayment,name="getdatapayment"),



    # login
    
    path('login', views.log_in,name="adminlogin"),
    path('logout_view', views.logout_view,name="logout_view"),
   

    # registration list

    path('checkregistration', views.check_registration,name="checkregistration"),
    path('deletereg/<int:id>',views.delete_registration,name="deletereg"),
   

]