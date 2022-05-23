from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'branch/home.html')

def students(request):
    return render(request,'branch/students.html')

def studentslist(request):
    return render(request,'branch/students_list.html')

def all_students_list(request):
    return render(request,'branch/allstudents_list.html')

def add_students_branch(request):
    return render(request,'branch/studentsaddbranch.html')

def teachers(request):
    return render(request,'branch/teacherslist.html')

def add_teachers(request):
    return render(request,'branch/addteacher.html')

def courses(request):
    return render(request,'branch/courses.html')

def add_courses(request):
    return render(request,'branch/addcourses.html')