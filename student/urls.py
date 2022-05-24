from . import views
from django.urls import path

app_name ='student'

urlpatterns = [
    path('',views.student_home,name='home'),
    path('profile',views.profile,name='profile'),
    path('editprofile',views.edit_profile,name='editprofile'),
    path('examlist',views.exam_list,name='examlist'),
    path('examinst',views.exam_instructions,name='examinst'),
]
