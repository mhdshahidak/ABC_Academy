from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from adminapp.models import Branch, Teacher


# Create your views here.
def admindashbord(request):
    context={
        "is_admindash":True
    }
    return render(request,'adminapps/home.html', context)

def branch_list(request):
    branches = Branch.objects.all()
    context={
        "is_branch":True,
        "branch":branches,
    }
    return render(request,'adminapps/branch.html', context)


# add branch

def add_branch(request):
    if Branch.objects.exists():
        branch = Branch.objects.last().id
        branch_id = 'ABC'+str(1000+branch)
    else:
        est=0
        branch_id = 'ABC'+str(1000+est)
    if request.method == 'POST':
        branch_name = request.POST['branchname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        city = request.POST['city']
        state = request.POST['state']
        address = request.POST['address']
        district = request.POST['district']
        pincode = request.POST['pincode']
        btanch_id = branch_id

        if password == cpassword:
            new_branch = Branch(branch_id=btanch_id,branch_name=branch_name,email=email,phone_number=phone,city=city,district=district,state=state,pin=pincode,address=address,password=password)
            new_branch.save()
            User = get_user_model()
            User.objects.create_user(email=email, password=password,branch=new_branch)

        else:
            return HttpResponse('re enter correct password')


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
    branches = Branch.objects.all()
    context={
        "is_teachers":True,
        "branch":branches,
    }
    return render(request,'adminapps/teachers.html', context)

def teachers_list(request,id):
    branch = Branch.objects.get(id=id)
    teachers = Teacher.objects.filter(branch=branch)
    context={
        "is_teacherslist":True,
        "teacher":teachers,
    }
    return render(request,'adminapps/teachers_list.html', context)

def add_teacher(request):
    if Teacher.objects.exists():
        branch = Teacher.objects.last().id
        techer_id = 'TEC'+str(1000+branch)
    else:
        est=0
        techer_id = 'TEC'+str(1000+est)
    if request.method=='POST':
        name = request.POST['name']
        gender = request.POST['gender']
        Dob = request.POST['Dob']
        mobile = request.POST['mobile']
        JoiningDate = request.POST['Joining Date']
        Qualification = request.POST['Qualification']
        Experience = request.POST['Experience']
        email = request.POST['email']
        Password = request.POST['Password']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        techerfk= request.POST['branch']
        rpassword = request.POST['rPassword']
        branch = Branch.objects.get(id=techerfk)
        if Password == rpassword:
            techer = Teacher(branch=branch,teacher_id=techer_id,Password=Password,name=name,gender=gender,dob=Dob ,phone=mobile, email=email, joining_date=JoiningDate, qualification=Qualification, experience=Experience, address=address,pin=zipcode,country=country,state=state,city=city)
            techer.save()
            User = get_user_model()
            User.objects.create_user(email=email, password=Password,teacher=techer)
        else:
            return HttpResponse ('Repeat correct password')
    branches = Branch.objects.all()
    context={
        "is_addteacher":True,
        "branch":branches,
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


#courses 

def courses(request):
    context={
        "is_courses":True
    }
    return render(request,'adminapps/courses.html', context)

def add_courses(request):
    context={
        "is_add_courses":True
    }
    return render(request,'adminapps/addcourses.html', context)

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

def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    # User = get_user_model()

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect('admins:admindash')
            elif user.branch != None:
                return redirect('branch:master')
            elif user.teacher != None:
                return redirect('teacher:homepage')
        else:
            return HttpResponse('not valid')
    return render(request,'adminapps/login.html')