from django.shortcuts import render

from adminapp.models import Teacher

# Create your views here.

def homepage(request):
    context = {
        "is_homepage": True,
        }
    return render(request,'teacher/teacher_home.html',context)

def profile(request):
    teacher=request.user.teacher
    branch_teacher=Teacher.objects.get(id=request.user.teacher)
    print(branch_teacher)
    context = {
        "is_profile": True,
        "teacher":teacher,
        "branch_teacher":branch_teacher,
        }
    return render(request,'teacher/profile.html',context)

def edit_profile(request):
    context = {
        "is_editprofile": True,
        }
    return render(request,'teacher/edit_teacher.html',context)

def courses(request):
    context = {
        "is_courses": True,
        }
    return render(request,'teacher/courses.html',context)

def studentlist(request):
    context = {
        "is_studentlist": True,
        }
    return render(request,'teacher/studentlist.html',context)

def coursewise_studentlist(request):
    context = {
        "is_coursewisestudentlist": True,
        }
    return render(request,'teacher/coursewise_studentlist.html',context)

def calander(request):
    context = {
        "is_calander": True,
        }
    return render(request,'teacher/calender.html',context)

