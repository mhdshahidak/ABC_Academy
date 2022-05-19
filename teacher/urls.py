from . import views
from django.urls import path

app_name ='teacher'

urlpatterns = [
    path('home',views.homepage,name='homepage'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.edit_profile,name='editprofile'),
    path('courses',views.courses,name='courses'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('coursewisestudentlist',views.coursewise_studentlist,name='coursewisestudentlist'),
]
