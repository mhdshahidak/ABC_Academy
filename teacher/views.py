from django.shortcuts import redirect, render

from adminapp.models import Teacher

# Create your views here.

def homepage(request):
    teacher=request.user.teacher
    context = {
        "is_homepage": True,
        "teacher":teacher,
        }
    return render(request,'teacher/teacher_home.html',context)

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

def edit_profile(request,id):
    
    teacher=request.user.teacher
    if 'form1' in request.method == "POST":
        name=request.POST['name']
        teacher_id=request.POST['id']
        gender=request.POST['gender']
        dob=request.POST['dob']
        email=request.POST['email']
        phone=request.POST['phone']
        Teacher.objects.filter(id=id).update(name=name,gender=gender,dob=dob,phone=phone,email=email,teacher_id=teacher_id)
        return redirect('teacher:profile')
    elif 'form2' in request.method == "POST":
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        zipcode=request.POST['zipcode']
        Teacher.objects.filter(id=cid).update(city=city,address=address,state=state,country=country,pin=zipcode)
        return redirect('teacher:profile')
    else:
        print('*10'*10)
        edit_teacher=Teacher.objects.get(id=id)
        context = {
            "is_editprofile": True,
            "teacher":teacher,
            "edit_teacher":edit_teacher,
            }
    return render(request,'teacher/edit_teacher.html',context)

def edit_contact(request,cid):
    teacher=request.user.teacher
    if 'form2' in request.method == "POST":
        print('%'*10)
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        zipcode=request.POST['zipcode']
        Teacher.objects.filter(id=cid).update(city=city,address=address,state=state,country=country,pin=zipcode)
        return redirect('teacher:profile')
    else:
        edit_teachercontact=Teacher.objects.get(id=cid)
        context = {
            "is_editprofile": True,
            "teacher":teacher,
            "edit_teacher":edit_teachercontact,
            }
    return render(request,'teacher/edit_teacher.html',context)


def edit_prof(request,pid):
    teacher=request.user.teacher
    if 'form3' in request.method == "POST":
        print('#'*10)
        id=request.POST['id']
        joiningdate=request.POST['joiningdate']
        # course=request.POST['course']
        qualification=request.POST['qualification']
        zipcode=request.POST['zipcode']
        Teacher.objects.filter(id=pid).update(teacher_id=id,joining_date=joiningdate,qualification=qualification,pin=zipcode)
        return redirect('teacher:profile')
    else:
        edit_teachercontact=Teacher.objects.get(id=pid)
        context = {
            "is_editprofile": True,
            "teacher":teacher,
            "edit_teacher":edit_teachercontact,
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

def result(request):
    context = {
        "is_result": True,
        }
    return render(request,'teacher/result.html',context)

def calander(request):
    context = {
        "is_calander": True,
        }
    return render(request,'teacher/calender.html',context)

