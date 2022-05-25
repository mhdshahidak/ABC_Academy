from django.shortcuts import render

# Create your views here.

def student_home(request):
    context = {
        "is_home": True,
        }
    return render(request,'student/student_home.html',context)



def profile(request):
    context = {
        "is_profile": True,
        }
    return render(request,'student/profile.html',context)



def edit_profile(request):
    context = {
        "is_editprofile": True,
        }
    return render(request,'student/edit_profile.html',context)



def exam_list(request):
    context = {
        "is_examlist": True,
        }
    return render(request,'student/exam_list.html',context)



def exam_instructions(request):
    context = {
        "is_examinst": True,
        }
    return render(request,'student/exam_instructions.html',context)


def exam(request):
    context = {
        "is_exam": True,
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
    context = {
        "is_fee": True,
        }
    return render(request,'student/fee.html',context)

def calendar(request):
    context = {
        "is_calendar": True,
        }
    return render(request,'student/calendar.html',context)