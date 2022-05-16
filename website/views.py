from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'website/home.html')

def allcourses(request):
    return render(request,'website/all_courses.html')

def course_ttc(request):
    return render(request,'website/ttc.html')

def course_fashion(request):
    return render(request,'website/fashion.html')

def online_application(request):
     return render(request,'website/apply_online.html')

def about_us(request):
     return render(request,'website/about_us.html')

def tourtocollege(request):
     return render(request,'website/tour.html')

