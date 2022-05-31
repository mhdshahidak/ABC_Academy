from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
# from abc_academy.decorators import auth_admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from adminapp.models import Batch, Branch, Courses, Exam, Instructions, Questions, Teacher




# Create your views here.
# @auth_admin
@login_required(login_url='/login/')
def admindashbord(request):
    print(request.user)
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
@login_required(login_url='/adminapp/login')
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

@login_required(login_url='/adminapp/login')
def branch_course(request):
    context={
        "is_branch_course":True
    }
    return render(request,'adminapps/branch_course.html', context)


@login_required(login_url='/adminapp/login')
def teachers(request):
    branches = Branch.objects.all()
    context={
        "is_teachers":True,
        "branch":branches,
    }
    return render(request,'adminapps/teachers.html', context)


@login_required(login_url='/adminapp/login')
def teachers_list(request,id):
    branch = Branch.objects.get(id=id)
    teachers = Teacher.objects.filter(branch=branch)
    context={
        "is_teacherslist":True,
        "teacher":teachers,
    }
    return render(request,'adminapps/teachers_list.html', context)


@login_required(login_url='/adminapp/login')
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
        batch = request.POST['course']

        branch = Branch.objects.get(id=techerfk)
        batch = Batch.objects.get(id=batch)
        if Password == rpassword:
            techer = Teacher(branch=branch,course=batch,teacher_id=techer_id,Password=Password,name=name,gender=gender,dob=Dob ,phone=mobile, email=email, joining_date=JoiningDate, qualification=Qualification, experience=Experience, address=address,pin=zipcode,country=country,state=state,city=city)
            techer.save()
            User = get_user_model()
            User.objects.create_user(email=email, password=Password,teacher=techer)
        else:
            return HttpResponse ('Repeat correct password')
    branches = Branch.objects.all()
    course=Batch.objects.all()
    context={
        "is_addteacher":True,
        "branch":branches,
        "course":course,
    }
    return render(request,'adminapps/addteacher.html', context)


@login_required(login_url='/adminapp/login')
def students(request):
    context={
        "is_students":True
    }
    return render(request,'adminapps/students.html', context)



@login_required(login_url='/adminapp/login')
def students_by_courses(request):
    context={
        "is_students_by_courses":True
    }
    return render(request,'adminapps/students_by_branch.html', context)


@login_required(login_url='/adminapp/login')
def students_list(request):
    context={
        "is_students_list":True
    }
    return render(request,'adminapps/students_list.html', context)


@login_required(login_url='/adminapp/login')
def add_student(request):
    context={
        "is_add_student":True
    }
    return render(request,'adminapps/addstudent.html', context)


@login_required(login_url='/adminapp/login')
def edit_student_by_admin(request):
    return render(request,'adminapps/students_edit_admin.html')


#courses 


@login_required(login_url='/adminapp/login')
def courses(request):
    course = Courses.objects.all()
    context={
        "is_courses":True,
        "course":course,
    }
    return render(request,'adminapps/courses.html', context)


@login_required(login_url='/adminapp/login')
def add_courses(request):
    if Courses.objects.exists():
        course = Courses.objects.last().id
        course_id = 'ACA'+str(1000+course)
    else:
        est=0
        course_id = 'ACA'+str(1000+est)
    if request.method == 'POST':
        c_name = request.POST['name']
        duration = request.POST['duration']
        fees = request.POST['fees']
        maxstudent = request.POST['maxstudent']

        new_course = Courses(course_id=course_id,couse_name=c_name,Duration=duration,total_fees=fees,max_students=maxstudent)
        new_course.save()
        return redirect('admins:courses')

    context={
        "is_add_courses":True
    }
    return render(request,'adminapps/addcourses.html', context)

# batch 


@login_required(login_url='/adminapp/login')
def batch(request):
    courses = Courses.objects.all()
    batches = Batch.objects.all()
    context={
        "is_batch":True,
        "course":courses,
        "batch":batches,
    }
    return render(request,'adminapps/batch_list.html', context)


@login_required(login_url='/adminapp/login')
def add_batch(request):
    if request.method == 'POST':
        course_id = request.POST['course']
        start_date = request.POST['startdate']
        end_date = request.POST['endingdate']

        course = Courses.objects.get(id=course_id)
        new_batch = Batch(course=course,starting_date=start_date,ending_date=end_date)
        new_batch.save()

    courses = Courses.objects.all()
    context={
        "is_batch":True,
        "course":courses
    }
    return render(request,'adminapps/batch.html', context)

# profile


@login_required(login_url='/adminapp/login')
def admin_profile(request):
    return render(request,'adminapps/profile_admin.html')


# exams


@login_required(login_url='/adminapp/login')
def exam(request):
    batches = Batch.objects.all()
    context={
        "is_exam":True,
        "batches":batches
    }
    return render(request,'adminapps/exams.html', context)


@login_required(login_url='/adminapp/login')
def exam_add_list(request,id):
    batch = Batch.objects.get(id=id)
    print(batch)
    context={
        "is_exam_add_list":True,
        "batch":batch,
    }
    return render(request,'adminapps/exam_add_lists.html', context)


@login_required(login_url='/adminapp/login')
def exam_add_first(request,id):
    if request.method == 'POST':
    
        batch = request.POST['batch']
        name = request.POST['examname']
        date = request.POST['examdate']
        start_time = request.POST['starttime']
        end_time = request.POST['endtime']
        duration = request.POST['duration']
        mark = request.POST['totalmark']
        batch = Batch.objects.get(id=batch)

        new_exam = Exam(batch=batch,exam_name=name,exam_date=date,start_time=start_time,end_time=end_time,duration=duration,total_mark=mark)
        new_exam.save()
        # print(new_exam.id)
        return redirect('/adminapp/examsaddone/'+str(new_exam.id))

    batch = Batch.objects.get(id=id)
    context={
        "is_exam_add_one":True,
        "batch":batch,
    }
    return render(request,'adminapps/exam_add1.html', context)


@login_required(login_url='/adminapp/login')
def exam_add_one(request,id):
    if request.method == 'POST':
        # print("aa")
        # print(request.POST)
        instructions = request.POST['instruction']
        exam = Exam.objects.get(id=id)

        new_insructions = Instructions(exam_id=exam,instructions=instructions)
        new_insructions.save()
        return redirect('/adminapp/examsaddtwo/'+str(exam.id))
    context={
        "is_exam_add_one":True
    }
    return render(request,'adminapps/exam_add_trial.html', context)


@login_required(login_url='/adminapp/login')
def exam_add_two(request,id):
    exam = Exam.objects.get(id=id)
    context={
        "is_exam_add_two":True,
        "exam":exam,
    }
    return render(request,'adminapps/exam_add2.html', context)


def savedata(request):
    print(request.POST)
    question = request.POST['question']
    type = request.POST['radio']
    exam_id = request.POST['exam_id']
    options = request.POST['options']
    mark = request.POST['mark']
    print(question,type,exam_id,options,mark)

    exam_pk = Exam.objects.get(id=exam_id)
    print()
    new_question = Questions(exam_id=exam_pk,question=question,type=type,option=options,mark=mark)
    new_question.save()
    data={
        'no':new_question.id,
        'question':new_question.question,
        'type':new_question.type,
        'mark':new_question.mark,
    }
    return JsonResponse(data)



# fees adding 

@login_required(login_url='/adminapp/login')
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

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect('admins:admindash')
            elif user.branch != None:
                return redirect('branch:master')
            elif user.teacher != None:
                return redirect('teacher:homepage')
            elif user.Student !=None:
                return redirect('student:home')
        else:
            return redirect('admins:adminlogin')
    return render(request,'adminapps/login.html')



def logout_view(request):
    logout(request)
    return redirect('/adminapp/login')