from . import views
from django.urls import path

app_name ='student'

urlpatterns = [
    path('',views.student_home,name='home'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.edit_profile,name='editprofile'),
]