from . import views
from django.urls import path

app_name ='web'

urlpatterns = [
    path('',views.homepage,name='home'),
    path('allcourse',views.allcourses,name='allcourse'),
    path('ttccourse',views.course_ttc,name='ttccourse'),
    path('fashioncourse',views.course_fashion,name='fashioncourse'),
    path('onlineapplication',views.online_application,name='onlineapplication'),
    path('about',views.about_us,name='about'),
    path('tour',views.tourtocollege,name='tours'),
]