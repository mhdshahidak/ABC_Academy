from datetime import datetime, timedelta, time
# from operator import le

from django.http import JsonResponse

from adminapp.models import Exam, Instructions, Questions, Student,Batch
from django.shortcuts import redirect, render

from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from branch.models import Payment

# from branch.models import Payment
from django.db.models import Sum

from student.models import Answer, ExamStatus
from datetime import datetime
from pytz import timezone 
import time

# Create your views here.
@login_required(login_url='/adminapp/login')
def student_home(request):
    student=request.user.Student
    exams = Exam.objects.filter(batch=student.course).count()
   
    context = {
        "is_home": True,
        "stexamcountudent":student,
        "examcount":exams,
        "student":student
        }
    return render(request,'student/student_home.html',context)


@login_required(login_url='/adminapp/login')
def profile(request):
    student=request.user.Student
    student_profile=Student.objects.get(id=request.user.Student.id)
    context = {
        "is_profile": True,
        "student":student,
        "student_profile":student_profile,
        }
    return render(request,'student/profile.html',context)


@login_required(login_url='/adminapp/login')
def edit_profile(request,id):
    student=request.user.Student
    students_id = student.id
    if request.method == "POST":
        if 'fname' in request.POST:
            # sid=request.POST['sid']
            first_name=request.POST['fname']
            second_name=request.POST['sname']
            # gender=request.POST['gender']
            # dob=request.POST['dob']
            # email=request.POST['email']
            phone=request.POST['phone']
            Student.objects.filter(id=id).update(first_name=first_name,last_name=second_name,phone=phone)
            return redirect('student:profile')
        elif 'address' in request.POST:
            address=request.POST['address']
            Student.objects.filter(id=students_id).update(address=address)
            return redirect('student:profile')
        elif 'currentpassword' in request.POST:
            currentpassword=request.POST['currentpassword']
            newpassword=request.POST['newpassword']
            cnewpassword=request.POST['cnewpassword']
            oldpassword =  Student.objects.get(id=students_id).password
            if newpassword == cnewpassword:
                
                if oldpassword == currentpassword:
                    Student.objects.filter(id=students_id).update(password=newpassword)
                    changePassword = get_user_model().objects.get(id=request.user.id)
                    changePassword.set_password(newpassword) 
                    changePassword.save()
                    return redirect('student:profile')
                else:
                    msg = "Incorrect old password"
            else:
                msg = "re enter correct password"
         
    edit_profile=Student.objects.get(id=id)
    context = {
        "is_editprofile": True,
        "edit_profile":edit_profile,
        "student":student
        }
    return render(request,'student/edit_profile.html',context)


@login_required(login_url='/adminapp/login')
def exam_list(request):
    student = request.user.Student
    exam = Exam.objects.filter(batch=student.course)
    context = {
        "is_examlist": True,
        "student":student,
        "exam":exam,
        }
    return render(request,'student/exam_list.html',context)



@login_required(login_url='/adminapp/login')
def exam_instructions(request,id):
    context = {}
    now = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d')
    exam = Exam.objects.get(id=id)
    exam_date = exam.exam_date
    exam_time = exam.start_time
    end_time = exam.end_time  
   
    if str(exam_date) == str(now):
        currentTime =  datetime.now().time()
        if currentTime > exam_time and currentTime < end_time:   
            pass
        else:
            return redirect('/student/examlist')  
    else:
           
        return redirect('/student/examlist')
    if Instructions.objects.filter(exam_id=exam).exists():
        instructions = Instructions.objects.get(exam_id=exam)
        context = {
            "is_examinst": True,
            "instructions":instructions,
            "exam":exam
        }
    else:
         context = {
            "is_examinst": True,
            "instructions":None,
            "exam":exam
        }
    return render(request,'student/exam_instructions.html',context)


@login_required(login_url='/adminapp/login')
def exam(request,id):
    if ExamStatus.objects.filter(student=request.user.Student,exam_id__id=id).exists():
        return redirect('/student/examlist')    
    exam = Exam.objects.get(id=id)
    student = request.user.Student
    status = "Attended"
    # today = datetime.now().date()
    # attnd_time = datetime.combine(today, time())
    Attending_obj = ExamStatus(exam_id=exam,student=student,status=status)
    Attending_obj.save()
    que = Questions.objects.filter(exam_id=exam)
    context = {
        "is_exam": True,
        "exam":exam,
        "que":que
        }
    return render(request,'student/exam.html',context)


@login_required(login_url='/adminapp/login')
def examq(request):
    student=request.user.Student
    context = {
        "is_exam": True,
        "student":student,
        }
    return render(request,'student/examq.html',context)

# def result(request):
#     student=request.user.Student
#     context = {
#         "is_result": True,
#         "student":student,
#         }
#     return render(request,'student/result.html',context)

@login_required(login_url='/adminapp/login')
def fee(request):
    id=request.user.Student.id
    student = request.user.Student
    paymentdetails = Payment.objects.filter(student=request.user.Student)
    viewpro=Student.objects.get(id=id) 
    total=viewpro.course.course.total_fees
    balanceamount=total
    recvamount = ""
    if paymentdetails.exists():
        recivedamount = Payment.objects.filter(student=viewpro.id).aggregate(Sum('paidamount'))
        recvamount = recivedamount['paidamount__sum']
        balanceamount  = total - recivedamount['paidamount__sum']
       

    context = {
        "is_fee": True,
        "paymentdetails":paymentdetails,
        "recvamount":recvamount,
        "balanceamount":balanceamount,
        "total":total,
        "student":student,

        }
    return render(request,'student/fee.html',context)



def calendar(request):
    context = {
        "is_calendar": True,
        }
    return render(request,'student/calendar.html',context)


@login_required(login_url='/adminapp/login')
def questions(request):
    if request.method == "POST":
        examId = request.POST['exam_id']
        examIds = []
        countQt =  Questions.objects.filter(exam_id = examId).count()
        qts = Questions.objects.filter(exam_id = examId)
        attendedQt = Answer.objects.filter(exam= examId,student=request.user.Student).count()
        for i in qts:
            if Answer.objects.filter(question=i.id,student=request.user.Student).exists():
                pass
            else:
                examIds.append(i.id)
        question = Questions.objects.filter(id__in= examIds).first()
        if len(examIds) > 0:
            choices = question.option.split(',')
            data={
                "question":question.question,
                "id":question.id,
                "option":choices,
                'total_questions':countQt,
                "type":question.type,
                "lenght":len(examIds),
                "attended_questions":attendedQt,
                "mark":question.mark,
            }
        else:
             data={
                "lenght":0,
            }
        return JsonResponse(data)
        
        

def datasave(request):
    if request.method =='POST':
        questionid=request.POST['questionId']
        answer=request.POST['answer']
        exam=request.POST['exam_id']
        studentid=request.user.Student
        queid= Questions.objects.get(id=questionid)
        examid= Exam.objects.get(id=exam)
        ans=Answer(exam=examid,student=studentid,question=queid,savedaswer=answer,status="Wait For Valuation" )
        ans.save()

        return JsonResponse({'msg':'added'})
