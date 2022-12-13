from . import views
from django.urls import path

app_name ='student'

urlpatterns = [
    path('',views.student_home,name='home'),
    path('profile',views.profile,name='profile'),
    path('editprofile/<int:id>',views.edit_profile,name='editprofile'),
    path('examlist',views.exam_list,name='examlist'),
    path('examinst/<int:id>',views.exam_instructions,name='examinst'),
    path('exam/<int:id>',views.exam,name='exam'),
    path('examq',views.examq,name='examq'),
    path('result',views.result,name='result'),
    path('show-result/<int:id>', views.showResult, name='showresult'),
    path('fee',views.fee,name='fee'),
    path('calendar',views.calendar,name='calendar'),                                                            
    path('questions/',views.questions,name='questions'),                                                            
    path('datasave/',views.datasave,name='datasave'),                                                            
]
