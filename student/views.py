
from datetime import datetime, timedelta, time
from django.shortcuts import render

from adminapp.models import Exam, Instructions, Student,Batch
from branch.models import Payment
from django.db.models import Sum

from student.models import ExamStatus


# Create your views here.

def student_home(request):
    student=request.user.Student
    context = {
        "is_home": True,
        "student":student,
        }
    return render(request,'student/student_home.html',context)



def profile(request):
    student=request.user.Student
    student_profile=Student.objects.get(id=request.user.Student.id)
    context = {
        "is_profile": True,
        "student":student,
        "student_profile":student_profile,
        }
    return render(request,'student/profile.html',context)



def edit_profile(request):
    edit_profile=Student.objects.get(id=request.user.Student.id)
    context = {
        "is_editprofile": True,
        "edit_profile":edit_profile
        }
    return render(request,'student/edit_profile.html',context)



def exam_list(request):
    student = request.user.Student
    exam = Exam.objects.filter(batch=student.course)
    # print(exam)
    # print(student)
    context = {
        "is_examlist": True,
        "student":student,
        "exam":exam,
        }
    return render(request,'student/exam_list.html',context)



def exam_instructions(request,id):
    
    exam = Exam.objects.get(id=id)
    instructions = Instructions.objects.get(exam_id=exam)
    context = {
        "is_examinst": True,
        "instructions":instructions,
        "exam":exam
        }
    return render(request,'student/exam_instructions.html',context)


def exam(request,id):
    exam = Exam.objects.get(id=id)
    student = request.user.Student
    status = "Attended"
    today = datetime.now().date()
    attnd_time = datetime.combine(today, time())
    # print(today,today_start)
    Attending_obj = ExamStatus(exam_id=exam,student=student,status=status,Attended_time=attnd_time)
    Attending_obj.save()
    print(Attending_obj)
    context = {
        "is_exam": True,
        "exam":exam,
        }
    return render(request,'student/exam.html',context)

def examq(request):
    context = {
        "is_exam": True,
        }
    return render(request,'student/examq.html',context)

def result(request):
    context = {
        "is_result": True,
        }
    return render(request,'student/result.html',context)

def fee(request):
    print(request.user.id)
    id=request.user.Student.id
    print(id)
    paymentdetails = Payment.objects.filter(student=request.user.Student)
    viewpro=Student.objects.get(id=id) 
    # print(viewpro)
    total=viewpro.course.course.total_fees
    print(total)
    balanceamount=total
    if paymentdetails.exists():
        recivedamount = Payment.objects.filter(student=viewpro.id).aggregate(Sum('paidamount'))
        recvamount= recivedamount['paidamount__sum']
        balanceamount  = total - recivedamount['paidamount__sum']
        print(total)
        print(balanceamount)
    print(paymentdetails)

    context = {
        "is_fee": True,
        "paymentdetails":paymentdetails,
        "recvamount":recvamount,
        "balanceamount":balanceamount,
        "total":total

        }
    return render(request,'student/fee.html',context)

def calendar(request):
    context = {
        "is_calendar": True,
        }
    return render(request,'student/calendar.html',context)