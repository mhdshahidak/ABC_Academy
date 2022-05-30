from . import views
from django.urls import path

app_name ='teacher'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('profile',views.profile,name='profile'),
    path('editprofile/<int:id>',views.edit_profile,name='editprofile'),
    path('courses',views.courses,name='courses'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('coursewisestudentlist',views.coursewise_studentlist,name='coursewisestudentlist'),
    path('result',views.result,name='result'),
    path('calander',views.calander,name='calander'),
    path('logout',views.logout,name='logout'),
]
