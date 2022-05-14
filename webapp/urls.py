from . import views
from django.urls import path

app_name ='webapp'

urlpatterns = [
    path('',views.home,name="home"),

]