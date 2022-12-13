from multiprocessing import context
from datetime import datetime
from pytz import timezone
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
# from abc_academy.decorators import auth_admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from adminapp.models import Batch, Branch, Courses, Exam, Instructions, Questions, Teacher, Student
from branch.models import Payment
from django.db.models import Sum
from student.models import Answer, ExamStatus
from website.models import OnlineApplying





# Create your views here.
# @auth_admin
@login_required(login_url='/login/')
def admindashbord(request):
    students=Student.objects.all().count()
    teacher= Teacher.objects.all().count()
    branch= Branch.objects.all().count()
    course= Courses.objects.all().count()
    context={
        "is_admindash":True,
        "students":students,
        "teacher":teacher,
        "branch":branch,
        "course":course,
        
    }
    return render(request,'adminapps/home.html', context)

@login_required(login_url='/adminapp/login')
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
            context={
                "is_addbranch":True,
                "status":1,
            }

        else:
            return HttpResponse('re enter correct password')
    else:
        context={
            "is_addbranch":True,
            "status":0
        }
    return render(request,'adminapps/addbranch.html', context)

@login_required(login_url='/adminapp/login')
def branch_course(request,id):

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
    branches = Branch.objects.all()
    course=Batch.objects.all()
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
            context={
                "is_addteacher":True,
                "branch":branches,
                "course":course,
                "status":1
            }
        else:
            return HttpResponse ('Repeat correct password')
    else:
        context={
                "is_addteacher":True,
                "branch":branches,
                "course":course,
                "status":0
            }
    return render(request,'adminapps/addteacher.html', context)


@login_required(login_url='/adminapp/login')
def delete_teacher(request,id):
    Teacher.objects.get(id=id).delete()
    
    return redirect('/adminapp/teachers')



@login_required(login_url='/adminapp/login')
def students(request):
    branch= Branch.objects.all()
    context={
        "is_students":True,
        "branch":branch
    }
    return render(request,'adminapps/students.html', context)



@login_required(login_url='/adminapp/login')
def students_by_courses(request,id):
    branch = Branch.objects.get(id=id)
    course = Batch.objects.all()
    context={
        "is_students_by_courses":True,
        "course":course,
        "branch":branch,
    }
    return render(request,'adminapps/students_by_branch.html', context)



@login_required(login_url='/adminapp/login')
def studentbatchlish(request,id,bid):
    course = Batch.objects.get(id=id)
    branch = Branch.objects.get(id=bid)
    students = Student.objects.filter(course=id,branch=bid)
    context={
        "is_studentbatchlish":True,
        "students":students,
        "course":course,
        "branch":branch,
    }
    return render(request,'adminapps/students_list.html',context)

@login_required(login_url='/adminapp/login')
def students_list(request):
    
    context={
        "is_students_list":True,

    }
    return render(request,'adminapps/s_list.html', context)


@login_required(login_url='/adminapp/login')
def add_student(request):
    course= Batch.objects.all()
    branch = Branch.objects.all()
    if request.method=='POST':
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
        branch = request.POST['branch']
        
        course_id=Batch.objects.get(id=courseid)
        branch_id = Branch.objects.get(id=branch)
        email_exists = Student.objects.filter(email=email).exists()
        if not email_exists:
            std = Student(course=course_id,branch=branch_id,student_id=studentid, first_name=name, last_name=lastname, gender=gender, dob=dob, phone=phone,email=email ,password=password,fatherphone=fatherphone,fathername=fathername,address=address)
            std.save()
            User = get_user_model()
            User.objects.create_user(email=email, password=password,Student=std)
        else :
            # msg = "email already exists"
            context={
                "is_add_student":True,
                "course":course,
                "branch":branch,
                "status":2
            }
            return render(request,'adminapps/addstudent.html', context)
        context={
            "is_add_student":True,
            "course":course,
            "branch":branch,
            "status":1
        }
    else:
        context={
        "is_add_student":True,
        "course":course,
        "branch":branch,
        "status":0
    }
    
    return render(request,'adminapps/addstudent.html', context)


@login_required(login_url='/adminapp/login')
def edit_student_by_admin(request,id):
    print(id)
    editdetails = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        # password = request.POST['password']
        fathername = request.POST['fathername']
        fatherphone = request.POST['fatherphone']
        #  email=email, password=password,
        Student.objects.filter(id=id).update(first_name=name,email=email, last_name=lastname, gender=gender,
                                             phone=phone, fatherphone=fatherphone, fathername=fathername)
        # Student.objects.filter(id=students_id).update(password=newpassword)
        get_user_model().objects.filter(Student = id).update(email=email)
        return redirect('admins:students')

    context = {
        "is_edit_student_by_admin": True,
        "editdetails": editdetails,
        }
    return render(request,'adminapps/edit_student_admin.html',context)


# @login_required(login_url='/adminapp/login')
# def delete_student(request,id):
#     Student.objects.get(id=id).delete()
    
#     return redirect('/adminapp/students')



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
        "is_add_courses":True,
    
    }
    return render(request,'adminapps/addcourses.html', context)



# batch 
@login_required(login_url='/adminapp/login')
def edit_course(request,id):
    course =Courses.objects.get(id=id)
    if request.method == "POST":
        c_name = request.POST['name']
        duration = request.POST['duration']
        fees = request.POST['fees']
        maxstudent = request.POST['maxstudent']
        # new_course = Courses(course_id=course_id,couse_name=c_name,Duration=duration,total_fees=fees,max_students=maxstudent)
        # new_course.save()
        # return redirect('admins:courses')
        Courses.objects.filter(id=id).update(couse_name=c_name,Duration=duration,total_fees=fees,max_students=maxstudent)  # direct updation
        msg = "updated successfully"
        return redirect('admins:courses')                  
    context = {
        "is_edit_course":True,
        "course":course
    }
    return render(request,'adminapps/edit_course.html', context)

@login_required(login_url='/adminapp/login')
def batch(request):
    courses = Courses.objects.all()
    batches = Batch.objects.all().order_by('-starting_date')
    context={
        "is_batch":True,
        "course":courses,
        "batch":batches,
    }
    return render(request,'adminapps/batch_list.html', context)



@login_required(login_url='/adminapp/login')
def add_batch(request):
    courses = Courses.objects.all()
    if request.method == 'POST':
        course_id = request.POST['course']
        start_date = request.POST['startdate']
        end_date = request.POST['endingdate']

        course = Courses.objects.get(id=course_id)
        new_batch = Batch(course=course,starting_date=start_date,ending_date=end_date)
        new_batch.save()
        context={
            "is_batch":True,
            "course":courses,
            "status":1,
        }
    else:
        context={
            "is_batch":True,
            "course":courses,
            "status":0,
        }
    return render(request,'adminapps/batch.html', context)

@login_required(login_url='/adminapp/login')
def edit_batch(request,id):
    batch=Batch.objects.get(id=id)
    course=Courses.objects.all()
    if request.method == "POST":
        # coursename=request.POST['coursename']
        stardate=request.POST['startdate']
        enddate=request.POST['endingdate']
        # courses=Courses.objects.get(id=coursename)
        Batch.objects.filter(id=id).update(starting_date=stardate,ending_date=enddate)

        context={
            "is_edit":True,
            "batch":batch,
            "status":1
        }
    else:
        context={
            "is_edit":True,
            "batch":batch,
            "courses":course,
            "status":0
        }
    return render(request,'adminapps/edit_batch.html',context)

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
    exam = Exam.objects.filter(batch=batch)
    # currentTime =  datetime.now().time()
    now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    upcoming_exam = Exam.objects.filter(batch=batch,exam_date__gte=str(now))
    previuos_exam = Exam.objects.filter(batch=batch,exam_date__lt=str(now))
 

    context={
        "is_exam_add_list":True,
        "batch":batch,
        "exam":exam,
        "uexam":upcoming_exam,
        "pexam":previuos_exam,
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
        return redirect('/adminapp/examsaddone/'+str(new_exam.id))

    batch = Batch.objects.get(id=id)
    context={
        "is_exam_add_first":True,
        "batch":batch,
    }
    return render(request,'adminapps/exam_add1.html', context)


@login_required(login_url='/adminapp/login')
def exam_add_one(request,id):
    
    if request.method == 'POST':
    
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
    Question= Questions.objects.filter(exam_id=id)
    context={
        "is_exam_add_two":True,
        "exam":exam,
        "Question":Question
    }
    return render(request,'adminapps/exam_add2.html', context)


@login_required(login_url='/login/')
def savedata(request):
    question = request.POST['question']
    type = request.POST['radio']
    exam_id = request.POST['exam_id']
    options = request.POST['options']
    mark = request.POST['mark']
    answer = request.POST['answer']

    exam_pk = Exam.objects.get(id=exam_id)
    new_question = Questions(exam_id=exam_pk,question=question,type=type,option=options,mark=mark,true_answer=answer)
    new_question.save()
    # answer = QuestionAnswer(question=new_question,true_answer=answer)
    # answer.save()
    data={
        'no':new_question.id,
        'question':new_question.question,
        'type':new_question.type,
        'mark':new_question.mark,
    }
    return JsonResponse(data)





@login_required(login_url='/login/')
@csrf_exempt
def editQuestiontdata(request,id):

    editquestion=Questions.objects.get(id=id)
    data={
        "question":editquestion.question,
        "type":editquestion.type,
        "option":editquestion.option,
        "answer":editquestion.true_answer,
        "mark":editquestion.mark,

    }
    return JsonResponse({'question': data}) 


@login_required(login_url='/login/')
@csrf_exempt
def updateQuestion(request):
    id=request.POST['Questionid']
    editquestion = request.POST['editquestion']
    editoptions = request.POST['editoptions']
    editanswer = request.POST['editanswer']
    editmark = request.POST['editmark']
 
    Questions.objects.filter(id=id).update(question=editquestion, option=editoptions, true_answer=editanswer, mark=editmark)
    return JsonResponse({'message': 'sucesses'})   





@login_required(login_url='/login/')
def editExam(request,id):
    exam = Exam.objects.get(id=id)
    if request.method == 'POST':
    
        name = request.POST['examname']
        date = request.POST['examdate']
        start_time = request.POST['starttime']
        end_time = request.POST['endtime']
        duration = request.POST['duration']
        mark = request.POST['totalmark']
        

        # new_exam = Exam(batch=batch,exam_name=name,exam_date=date,start_time=start_time,end_time=end_time,duration=duration,total_mark=mark)
        # new_exam.save()
        # return redirect()
        Exam.objects.filter(id=id).update(exam_name=name,exam_date=date,start_time=start_time,end_time=end_time,duration=duration,total_mark=mark)
        return redirect('admins:exams')

    context={
            "is_editExam":True,
            "exam":exam,        
        }  
    return render(request,'adminapps/edit_exam_details.html', context)


# rechedule

@login_required(login_url='/adminapp/login')
def reschedule(request):
    exams = Exam.objects.all()
    context={
            "is_reschedule":True,
            "exams":exams,
        }
    return render(request,'adminapps/reschedule.html', context)



@login_required(login_url='/adminapp/login')
def reschedule_list(request,id):
    exam_status = ExamStatus.objects.filter(exam_id=id,status="Attended")
    context={
            "is_reschedule_list":True,
            "exam_status":exam_status,
        }
    return render(request,'adminapps/reschedule_list.html', context)


@login_required(login_url='/adminapp/login')
def delete_schedule_status(request,id):
    
    ExamStatus.objects.get(id=id).delete()
    
    return redirect('/adminapp/reschedule')


# fees adding 

@login_required(login_url='/adminapp/login')
def fees_adding(request):
    if request.method=='POST':
        studentid = request.POST['studentid']
        paidamount = request.POST['paidamount']
        paiddate = request.POST['paiddate']
        student_id= Student.objects.get(student_id=studentid) 
        payment= Payment(student=student_id, paidamount=paidamount, paiddate=paiddate)
        payment.save()
        context={
            "is_fees_adding":True,
            "status":1
        }
    else:
        context={
            "is_fees_adding":True,
            "status":0
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
                return redirect('teacher:profile')
            elif user.Student !=None:
                return redirect('student:home')
        else:
            msg = "* Incorrect email or password *"
            return render(request,'adminapps/login.html',{'msg':msg,})
    return render(request,'adminapps/login.html')



def logout_view(request):
    logout(request)
    return redirect('/adminapp/login')




@csrf_exempt
def getdatapayment(request):
    studentid = request.POST['studentid']
    course = request.POST['course']
    if Student.objects.filter(student_id = studentid).exists():
        viewpro=Student.objects.get(student_id=studentid) 
        total=viewpro.course.course.total_fees
        balanceamount=total
        # batch = Student.objects.get(course=)
        if Payment.objects.filter(student=viewpro.id).exists():
            recivedamount = Payment.objects.filter(student=viewpro.id).aggregate(Sum('paidamount'))
            balanceamount  = total - recivedamount['paidamount__sum']
        
            data={     
                "msg":'success',
                "name":viewpro.first_name,
                "coursename":viewpro.course.course.couse_name,
                "price":viewpro.course.course.total_fees,
                "balanceamount":balanceamount
            }
            return JsonResponse({'details':data})
        else:
            data = {
            'msg':2,
            "name":viewpro.first_name,
            "coursename":viewpro.course.course.couse_name,
            "price":viewpro.course.course.total_fees,
            "balanceamount":0
        }
        return JsonResponse({'details':data})
    else:
        data = {
            'msg':'0',
        }
        return JsonResponse({'details':data})



@login_required(login_url='/adminapp/login')
def result_batch(request):
    # answer= Answer.objects.filter()
    # answer= ExamStatus.objects.all()
    batch = Batch.objects.all()
    
    context={
        "is_result_batch":True,
        "batch":batch,


    }
    return render(request,'adminapps/result_batch.html', context)

@login_required(login_url='/adminapp/login')
def result_exam(request,id):
    exams = Exam.objects.filter(batch__id=id)
    context={
        "is_result_exam":True,
        "exams":exams,
        
    }
    return render(request,'adminapps/result_exam.html', context)


@login_required(login_url='/adminapp/login')
def result(request,id,bid):
    # answer= Answer.objects.filter()
    exam = Exam.objects.get(id=id)
    answer= ExamStatus.objects.filter(student__course__id=bid,exam_id=id)
    context={
        "is_result":True,
        "answer":answer,
        "exam":exam,
    }
    return render(request,'adminapps/result.html', context)


def resultPublish(request,id):
    exam = Exam.objects.get(id=id)
    exam.is_published = True
    exam.save()
    return redirect("admins:resultbatch")



@login_required(login_url='/adminapp/login')
def checkresult(request,eid,sid):
    answer = Answer.objects.filter(exam=eid,student=sid)
    total_mark = Questions.objects.filter(exam_id=eid).aggregate(Sum('mark'))
    mark = Answer.objects.filter(exam=eid,student=sid).aggregate(Sum('mark'))
    std= Student.objects.get(id=sid)
    context={
        "is_checkresult":True,
        "answer":answer,
        "std":std,
        "total_mark":total_mark,
        "mark":mark,

    }
    return render(request,'adminapps/checkresult.html', context)



@login_required(login_url='/adminapp/login')
def check_registration(request):
    registrations = OnlineApplying.objects.all()
    context = {
        "is_check_registration":True,
        "registrations":registrations,
    }
    return render(request,'adminapps/registration_list.html',context)


@login_required(login_url='/adminapp/login')
def delete_registration(request,id):
    OnlineApplying.objects.get(id=id).delete()
    
    return redirect('/adminapp/checkregistration')