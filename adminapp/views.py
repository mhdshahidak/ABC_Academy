from django.shortcuts import render

# Create your views here.
def admindashbord(request):
    return render(request,'adminapps/home.html')

def branch_list(request):
    return render(request,'adminapps/branch.html')


def add_branch(request):
    return render(request,'adminapps/addbranch.html')

def teachers(request):
    return render(request,'adminapps/teachers.html')

def teachers_list(request):
    return render(request,'adminapps/teachers_list.html')

def add_teacher(request):
    return render(request,'adminapps/addteacher.html')

def students(request):
    return render(request,'adminapps/students.html')


# def exams(request):
#     return render(request,'adminapp/exams.html')


def students_by_courses(request):
    return render(request,'adminapps/students_by_branch.html')

def students_list(request):
    return render(request,'adminapps/students_list.html')

def add_student(request):
    return render(request,'adminapps/addstudent.html')
