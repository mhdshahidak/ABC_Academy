from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'teacher/teacher_home.html')

def profile(request):
    return render(request,'teacher/profile.html')

def edit_profile(request):
    return render(request,'teacher/edit_teacher.html')

def courses(request):
    return render(request,'teacher/courses.html')

def studentlist(request):
    return render(request,'teacher/studentlist.html')

def coursewise_studentlist(request):
    return render(request,'teacher/coursewise_studentlist.html')

