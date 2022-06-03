from django.shortcuts import render,redirect
from adminapp.models import Teacher,Student,Batch,Branch
from . models import Payment
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.


@login_required(login_url='/adminapp/login')
def master(request):
    print(request.user.branch.branch_name)
    details = request.user.branch
    print(details.branch_name)
    student = Student.objects.filter(branch=request.user.branch).count()
    teacher = Teacher.objects.filter(branch=request.user.branch).count()
    branch = Branch.objects.all()
    print(branch)
    # viewstudent = Student.objects.filter(course=id).all()

    context = {
        "is_master": True,
        "student": student,
        "teacher": teacher,
        "details": details,
        "branch": branch

    }
    return render(request, 'branch/home.html', context)

# Student listing, adding , editing,  deleting
@login_required(login_url='/adminapp/login')
def students(request):
    details = request.user.branch
    batch = Batch.objects.all()
    print(batch)
    context = {
        "is_students": True,
        "batch": batch,
        "details": details,
        }
    return render(request, 'branch/students.html', context)


@login_required(login_url='/adminapp/login')
def studentslist(request, id):
    # print(id)
    details = request.user.branch
    viewstudent = Student.objects.filter(course=id).all()
    # print(viewstudent)
    context = {
        "is_studentslist": True,
        "viewstudent": viewstudent,
        "details": details,
        }
    return render(request, 'branch/students_list.html', context)


@login_required(login_url='/adminapp/login')
def all_students_list(request):
    details = request.user.branch
    student = Student.objects.filter(branch=request.user.branch)
    # print(student)
    context = {
        "is_all_students_list": True,
        "student": student,
        "details": details,
    }
    return render(request, 'branch/allstudents_list.html', context)


@login_required(login_url='/adminapp/login')
def add_students_branch(request):
    details = request.user.branch
    studentFk = request.user.branch.id
    course = Batch.objects.all()
    # print(course)
    # print(studentFk)
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        studentid = request.POST['studentid']
        gender = request.POST['gender']
        courseid = request.POST['course']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        fathername = request.POST['fathername']
        fatherphone = request.POST['fatherphone']
        address = request.POST['address']
        print(courseid)
        studentFk = request.user.branch
        course_id = Batch.objects.get(id=courseid)
        print(studentFk)
        std = Student(course=course_id, branch=studentFk, student_id=studentid, first_name=name, last_name=lastname, gender=gender,dob=dob, phone=phone, email=email, password=password, fatherphone=fatherphone, fathername=fathername, address=address)
        std.save()
        User = get_user_model()
        User.objects.create_user(email=email, password=password, Student=std)
        context = {
            "is_add_students_branch": True,
            "course": course,
            "details": details,
            "status": 1,
            }
    else:
        context = {
            "is_add_students_branch": True,
            "course": course,
            "details": details,
            "status": 0,
        }
    return render(request, 'branch/studentsaddbranch.html', context)


@login_required(login_url='/adminapp/login')
def editstudent(request, id):
    detail = request.user.branch
    editdetails = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        fathername = request.POST['fathername']
        fatherphone = request.POST['fatherphone']
        Student.objects.filter(id=id).update(first_name=name, last_name=lastname, gender=gender,
                                             phone=phone, email=email, password=password, fatherphone=fatherphone, fathername=fathername)
        return redirect('/branch/allstudentslist')
    context = {
        "is_add_students_branch": True,
        "editdetails": editdetails,
        "details": detail
        }
    return render(request, 'branch/editstudent.html', context)

def delete_student(request,id):
    Student.objects.get(id=id).delete()
    # print(student)
    # student.delete()
    return redirect('branch:allbranchstudentslist')


# Teacher listing, adding , editing,  deleting
@login_required(login_url='/adminapp/login')
def teachers(request):
    details = request.user.branch
    techerlist = Teacher.objects.all()
    context = {
        "is_teachers": True,
        "techerlist": techerlist,
        "details": details,
    }
    return render(request, 'branch/teacherslist.html', context)


@login_required(login_url='/adminapp/login')
def add_teachers(request):
    details = request.user.branch
    course = Batch.objects.all()
    if Teacher.objects.exists():
        branch = Teacher.objects.last().id
        techer_id = 'TEC'+str(1000+branch)
    else:
        est = 0
        techer_id = 'TEC'+str(1000+est)
    if request.method == 'POST':
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
        courseid = request.POST['course']
        techerfk = request.user.branch

        course_id = Batch.objects.get(id=courseid)

        techer = Teacher(course=course_id, branch=techerfk, teacher_id=techer_id, Password=Password, name=name, gender=gender, dob=Dob, phone=mobile, email=email,
                         joining_date=JoiningDate, qualification=Qualification, experience=Experience, address=address, pin=zipcode, country=country, state=state, city=city)
        techer.save()
        User = get_user_model()
        User.objects.create_user(email=email, password=Password, teacher=techer)
        context = {
        "is_add_teachers": True,
        "course": course,
        "details": details,
        "status":1
    }
    else:
        context = {
        "is_add_teachers": True,
        "course": course,
        "details": details,
        "status":0
    }
    return render(request, 'branch/addteacher.html', context)


@login_required(login_url='/adminapp/login')
def editteacher(request, id):
    details = request.user.branch
    editdetails = Teacher.objects.get(id=id)
    if request.method == 'POST':
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
        Teacher.objects.filter(id=id).update(Password=Password, name=name, gender=gender, dob=Dob, phone=mobile, email=email, joining_date=JoiningDate,qualification=Qualification, experience=Experience, address=address, pin=zipcode, country=country, state=state, city=city)
        return redirect('/branch/teacherslist')
    context = {
        "is_teachers": True,
        "details": details,
        "editdetails": editdetails,
    }
    return render(request, 'branch/editteacher.html', context)

def delete_teacher(request,id):
    Teacher.objects.get(id=id).delete()
    # print(student)
    # student.delete()
    return redirect('branch:allbranchstudentslist')



@login_required(login_url='/adminapp/login')
def fees(request):
    details = request.user.branch
    paymentdets = Payment.objects.all()
    context = {
        "is_fees": True,
        "paymentdets": paymentdets,
        "details": details,
    }
    return render(request, 'branch/fees.html', context)


@login_required(login_url='/adminapp/login')
def add_fees(request):
    details = request.user.branch
    if request.method == 'POST':
        studentid = request.POST['studentid']
        paidamount = request.POST['paidamount']
        paiddate = request.POST['paiddate']
        totalprice = request.POST['totalprice']
        student_id = Student.objects.get(student_id=studentid)
        # print(paidamount,paiddate,studentid,totalprice)
        payment = Payment(student=student_id, paidamount=paidamount, paiddate=paiddate)
        payment.save()
        context = {
            "is_add_fees": True,
            "details": details,
            "status":1
        }
    else:
        context = {
            "is_add_fees": True,
            "details": details,
        }
    return render(request, 'branch/add_fees.html', context)


# profile
@login_required(login_url='/adminapp/login')
def profile_branch(request):
    details = request.user.branch
    context = {
        "is_exam_list": True,
        "details": details,
    }
    return render(request, 'branch/profile_branch.html', context)

@login_required(login_url='/adminapp/login')
def logout_view(request):
    logout(request)
    return redirect('/adminapp/login')


@csrf_exempt
def getdata(request):
    studentid = request.POST['studentid']
    course = request.POST['course']
    print(course)
    viewpro = Student.objects.get(student_id=studentid)
    print(viewpro.first_name)
    print(viewpro.course.course.couse_name)
    total = viewpro.course.course.total_fees
    balanceamount = total
    # batch = Student.objects.get(course=)
    if Payment.objects.filter(student=viewpro.id).exists():
        recivedamount = Payment.objects.filter(
            student=viewpro.id).aggregate(Sum('paidamount'))
        print(recivedamount['paidamount__sum'])
        balanceamount = total - recivedamount['paidamount__sum']
        print(total)
        print(balanceamount)
    data = {
        "name": viewpro.first_name,
        "coursename": viewpro.course.course.couse_name,
        "price": viewpro.course.course.total_fees,
        "balanceamount": balanceamount
    }
    return JsonResponse({'details': data})



# @login_required(login_url='/adminapp/login')
# def courses(request):
#     details = request.user.branch
#     context = {
#         "is_courses": True,
#         "details": details,
#     }
#     return render(request, 'branch/courses.html', context)


# @login_required(login_url='/adminapp/login')
# def add_courses(request):
#     details = request.user.branch
#     context = {
#         "is_add_courses": True,
#         "details": details,
#     }
#     return render(request, 'branch/addcourses.html', context)



# exam
# @login_required(login_url='/adminapp/login')
# def exam_list(request):
#     details = request.user.branch
#     context = {
#         "is_exam_list": True,
#         "details": details,
#     }
#     return render(request, 'branch/exam_list.html', context)


# @login_required(login_url='/adminapp/login')
# def exam_add_b_one(request):
#     context = {
#         "is_exam_add_b_one": True
#     }
#     return render(request, 'branch/exam_addb1.html', context)


# @login_required(login_url='/adminapp/login')
# def exam_add_b_two(request):
#     context = {
#         "is_exam_add_b_two": True
#     }
#     return render(request, 'branch/exam_addb2.html', context)


# @login_required(login_url='/adminapp/login')
# def exam_add_b_Three(request):
#     context = {
#         "is_exam_add_b_three": True
#     }
#     return render(request, 'branch/exam_addb3.html', context)






