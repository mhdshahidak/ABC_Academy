from django.shortcuts import render

# Create your views here.

def student_home(request):
    return render(request,'student/student_home.html')

def profile(request):
    return render(request,'student/profile.html')

def edit_profile(request):
    return render(request,'student/edit_profile.html')