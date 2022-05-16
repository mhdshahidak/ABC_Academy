from django.shortcuts import render

# Create your views here.
def admindashbord(request):
    return render(request,'adminapps/home.html')

def branch_list(request):
    return render(request,'adminapps/branch.html')

# def branch_list(request):
#     return render(request,'adminapps/branchlist.html')

# def add_branch(request):
#     return render(request,'adminapp/addbranch.html')

# def teachers(request):
#     return render(request,'adminapp/teachers.html')

# def teachers_list(request):
#     return render(request,'adminapp/teachers_list.html')

# def add_teachers(request):
#     return render(request,'adminapp/add_teacher.html')

# def exams(request):
#     return render(request,'adminapp/exams.html')

# def students(request):
#     return render(request,'adminapp/students.html')

# def students_by_courses(request):
#     return render(request,'adminapp/students_by_branch.html')

# def students_list(request):
#     return render(request,'adminapp/student_list.html')

# def add_student(request):
#     return render(request,'adminapp/addstudent.html')