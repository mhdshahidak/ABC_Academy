from django.shortcuts import redirect, render

from adminapp.models import Courses, Teacher
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required(login_url='/adminapp/login')
def homepage(request):
    teacher=request.user.teacher
    context = {
        "is_homepage": True,
        "teacher":teacher,
        }
    return render(request,'teacher/teacher_home.html',context)

@login_required(login_url='/adminapp/login')
def profile(request):
    teacher=request.user.teacher
    branch_teacher=Teacher.objects.get(id=request.user.teacher.id)
    print(branch_teacher)
    context = {
        "is_profile": True,
        "teacher":teacher,
        "branch_teacher":branch_teacher,
        }
    return render(request,'teacher/profile.html',context)

@login_required(login_url='/adminapp/login')
def edit_profile(request,id):
    teacher=request.user.teacher
    if request.method == 'POST':
        print(request.POST)
        if 'name' in request.POST:
            name=request.POST['name']
            teacher_id=request.POST['id']
            gender=request.POST['gender']
            dob=request.POST['dob']
            email=request.POST['email']
            phone=request.POST['phone']
            Teacher.objects.filter(id=id).update(name=name,gender=gender,dob=dob,phone=phone,email=email,teacher_id=teacher_id)
            return redirect('teacher:profile')
        elif 'address' in request.POST:
            print(request.POST)
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            country=request.POST['country']
            zipcode=request.POST['zipcode']
            Teacher.objects.filter(id=id).update(city=city,address=address,state=state,country=country,pin=zipcode)
            return redirect('teacher:profile')
        elif 'joiningdate' in request.POST:
            id=request.POST['id']
            joiningdate=request.POST['joiningdate']
            qualification=request.POST['qualification']
            zipcode=request.POST['zipcode']
            Teacher.objects.filter(id=id).update(teacher_id=id,joining_date=joiningdate,qualification=qualification,pin=zipcode)
            return redirect('teacher:profile')
    edit_teacher=Teacher.objects.get(id=id)
    context = {
        "is_editprofile": True,
        "teacher":teacher,
        "edit_teacher":edit_teacher,
        }

    
    return render(request,'teacher/edit_teacher.html',context)



def courses(request):
    teacher=request.user.teacher
    context = {
        "is_courses": True,
        "teacher":teacher,
        }
    return render(request,'teacher/courses.html',context)


def studentlist(request):
    teacher=request.user.teacher
    context = {
        "is_studentlist": True,
        "teacher":teacher
        }
    return render(request,'teacher/studentlist.html',context)

def coursewise_studentlist(request):
    teacher=request.user.teacher
    context = {
        "is_coursewisestudentlist": True,
        "teacher":teacher
        }
    return render(request,'teacher/coursewise_studentlist.html',context)

def result(request):
    teacher=request.user.teacher
    context = {
        "is_result": True,
        "teacher":teacher
        }
    return render(request,'teacher/result.html',context)

def calander(request):
    teacher=request.user.teacher
    context = {
        "is_calander": True,
        "teacher":teacher
        }
    return render(request,'teacher/calender.html',context)


def logout_view(request):
    logout(request)
    return redirect('/adminapp/login')

