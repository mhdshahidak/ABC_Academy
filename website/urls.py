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
    path('contact',views.contact,name='contact'),
    path('tour',views.tourtocollege,name='tours'),
    path('blog',views.blog,name='blog'),
    path('blogpost',views.blog_post,name='blogpost'),
    path('news',views.news,name='news'),
    path('newspage',views.newspages,name='newspage'),
    path('events',views.events,name='events'),
    path('eventpage',views.eventpages,name='eventpage'),
    path('gallery',views.gallery,name='gallery'),
    path('franchise',views.franchise,name='franchise')
]