from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def admindashbord(request):
    context={
        "is_admindash":True
    }
    return render(request,'adminapps/home.html', context)

def branch_list(request):
    context={
        "is_branch":True
    }
    return render(request,'adminapps/branch.html', context)


def add_branch(request):
    context={
        "is_addbranch":True
    }
    return render(request,'adminapps/addbranch.html', context)

def branch_course(request):
    context={
        "is_branch_course":True
    }
    return render(request,'adminapps/branch_course.html', context)

def teachers(request):
    context={
        "is_teachers":True
    }
    return render(request,'adminapps/teachers.html', context)

def teachers_list(request):
    context={
        "is_teacherslist":True
    }
    return render(request,'adminapps/teachers_list.html', context)

def add_teacher(request):
    context={
        "is_addteacher":True
    }
    return render(request,'adminapps/addteacher.html', context)

def students(request):
    context={
        "is_students":True
    }
    return render(request,'adminapps/students.html', context)


def students_by_courses(request):
    context={
        "is_students_by_courses":True
    }
    return render(request,'adminapps/students_by_branch.html', context)

def students_list(request):
    context={
        "is_students_list":True
    }
    return render(request,'adminapps/students_list.html', context)

def add_student(request):
    context={
        "is_add_student":True
    }
    return render(request,'adminapps/addstudent.html', context)


# login

def login(request):
    return render(request,'adminapps/login.html')