from datetime import datetime, timedelta, time
# from operator import le

from django.http import JsonResponse

from adminapp.models import Exam, Instructions, Questions, Student,Batch
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

# from branch.models import Payment
# from django.db.models import Sum

from student.models import Answer, ExamStatus
from datetime import datetime
from pytz import timezone 
import time

# Create your views here.
@login_required(login_url='/adminapp/login')
def student_home(request):
    student=request.user.Student
    context = {
        "is_home": True,
        "student":student,
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
    if request.method == "POST":
        if 'id' in request.POST:
            id=request.POST['id']
            first_name=request.POST['fname']
            second_name=request.POST['sname']
            gender=request.POST['gender']
            dob=request.POST['dob']
            email=request.POST['email']
            phone=request.POST['phone']
            Student.objects.filter(id=cid).update(student_id=id,first_name=first_name,last_name=second_name,gender=gender,dob=dob,phone=phone,email=email)
            return redirect('student:profile')
        # elif 'fname' in request.POST:
        #     fname=request.POST['fname']
        #     fatherphone=request.POST['fatherhone']
        #     address=request.POST['address']
        #     Student.objects.filter(id=cid).update(fathername=fname,fatherphone=fatherphone,address=address)
        #     return redirect('student:profile')
        elif 'cid' in request.POST:
            cid=request.POST['cid']
            cname=request.POST['cname']
            batch=request.POST['batch']
            duration=request.POST['duration']
            Student.objects.filter(id=cid).update(course__course__course_id=cid,course__course__couse_name=cname,course__course__Duration=duration,course__starting_date=batch)
            return redirect('student:profile')
            
    edit_profile=Student.objects.get(id=id)
    context = {
        "is_editprofile": True,
        "edit_profile":edit_profile,
        "student":student
        }
    return render(request,'student/edit_profile.html',context)



def exam_list(request):
    student = request.user.Student
    exam = Exam.objects.filter(batch=student.course)
    context = {
        "is_examlist": True,
        "student":student,
        "exam":exam,
        }
    return render(request,'student/exam_list.html',context)



def exam_instructions(request,id):
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
    instructions = Instructions.objects.get(exam_id=exam)
    context = {
        "is_examinst": True,
        "instructions":instructions,
        "exam":exam
        }
    return render(request,'student/exam_instructions.html',context)


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

def examq(request):
    student=request.user.Student
    context = {
        "is_exam": True,
        "student":student,
        }
    return render(request,'student/examq.html',context)

def result(request):
    student=request.user.Student
    context = {
        "is_result": True,
        "student":student,
        }
    return render(request,'student/result.html',context)

def fee(request):
    # print(request.user.id)
    # id=request.user.Student.id
    # print(id)
    # paymentdetails = Payment.objects.filter(student=request.user.Student)
    # viewpro=Student.objects.get(id=id) 
    # # print(viewpro)
    # total=viewpro.course.course.total_fees
    # print(total)
    # balanceamount=total
    # if paymentdetails.exists():
    #     recivedamount = Payment.objects.filter(student=viewpro.id).aggregate(Sum('paidamount'))
    #     recvamount= recivedamount['paidamount__sum']
    #     balanceamount  = total - recivedamount['paidamount__sum']
    #     print(total)
    #     print(balanceamount)
    # print(paymentdetails)

    # context = {
    #     "is_fee": True,
    #     "paymentdetails":paymentdetails,
    #     "recvamount":recvamount,
    #     "balanceamount":balanceamount,
    #     "total":total

    #     }
    return render(request,'student/fee.html')

def calendar(request):
    context = {
        "is_calendar": True,
        }
    return render(request,'student/calendar.html',context)


def questions(request):
    if request.method == "POST":
        print(request.user.Student)
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
        print(request.POST)
        questionid=request.POST['questionId']
        answer=request.POST['answer']
        exam=request.POST['exam_id']
        studentid=request.user.Student
        queid= Questions.objects.get(id=questionid)
        examid= Exam.objects.get(id=exam)
        ans=Answer(exam=examid,student=studentid,question=queid,savedaswer=answer,status="Wait For Valuation" )
        ans.save()

        return JsonResponse({'msg':'added'})
