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

def edit_student_by_admin(request):
    return render(request,'adminapps/students_edit_admin.html')

# profile

def admin_profile(request):
    return render(request,'adminapps/profile_admin.html')


# exams

def exam(request):
    context={
        "is_exam":True
    }
    return render(request,'adminapps/exams.html', context)

def exam_add_list(request):
    context={
        "is_exam_add_list":True
    }
    return render(request,'adminapps/exam_add_lists.html', context)

def exam_add_first(request):
    context={
        "is_exam_add_one":True
    }
    return render(request,'adminapps/exam_add1.html', context)

def exam_add_one(request):
    context={
        "is_exam_add_one":True
    }
    return render(request,'adminapps/exam_add_trial.html', context)


def exam_add_two(request):
    context={
        "is_exam_add_two":True
    }
    return render(request,'adminapps/exam_add2.html', context)




# fees adding 

def fees_adding(request):
    context={
        "is_fees_adding":True
    }
    return render(request,'adminapps/fees_by_admin.html', context)


# login

def login(request):
    return render(request,'adminapps/login.html')