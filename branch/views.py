from django.shortcuts import render

# Create your views here.
def master(request):
    context={
        "is_master":True
    }
    return render(request,'branch/home.html', context)

def students(request):
    context={
        "is_students":True
    }
    return render(request,'branch/students.html', context)

def studentslist(request):
    context={
        "is_studentslist":True
    }
    return render(request,'branch/students_list.html', context)

def all_students_list(request):
    context={
        "is_all_students_list":True
    }
    return render(request,'branch/allstudents_list.html', context)

def add_students_branch(request):
    context={
        "is_add_students_branch":True
    }
    return render(request,'branch/studentsaddbranch.html', context)

def teachers(request):
    context={
        "is_teachers":True
    }
    return render(request,'branch/teacherslist.html', context)

def add_teachers(request):
    context={
        "is_add_teachers":True
    }
    return render(request,'branch/addteacher.html', context)

def courses(request):
    context={
        "is_courses":True
    }
    return render(request,'branch/courses.html', context)

def add_courses(request):
    context={
        "is_add_courses":True
    }
    return render(request,'branch/addcourses.html', context)

def fees(request):
    context={
        "is_fees":True
    }
    return render(request,'branch/fees.html', context)

def add_fees(request):
    context={
        "is_add_fees":True
    }
    return render(request,'branch/add_fees.html', context)


# profile

def profile_branch(request):
    return render(request,'branch/profile_branch.html')

# exam 

def exam_list(request):
    context={
        "is_exam_list":True
    }
    return render(request,'branch/exam_list.html', context)

def exam_add_b_one(request):
    context={
        "is_exam_add_b_one":True
    }
    return render(request,'branch/exam_addb1.html', context)

def exam_add_b_two(request):
    context={
        "is_exam_add_b_two":True
    }
    return render(request,'branch/exam_addb2.html', context)

def exam_add_b_Three(request):
    context={
        "is_exam_add_b_three":True
    }
    return render(request,'branch/exam_addb3.html', context)