from . import views
from django.urls import path

app_name ='student'

urlpatterns = [
    path('home',views.student_home,name='home')
]