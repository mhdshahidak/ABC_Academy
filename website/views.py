from django.shortcuts import render

from adminapp.models import Branch

# Create your views here.

def homepage(request):
    return render(request,'website/home.html')

def allcourses(request):
    return render(request,'website/all_courses.html')

def course_ttc(request):
    return render(request,'website/ttc.html')

def course_fashion(request):
    return render(request,'website/fashion.html')

def course_beautician(request):
    return render(request,'website/beautician.html')

def online_application(request):
    branches = Branch.objects.all()
    context = {
        "branches":branches,
    }
    return render(request,'website/apply_online.html',context)

def about_us(request):
    return render(request,'website/about_us.html')

def contact(request):
    return render(request,'website/contact.html')

def tourtocollege(request):
    return render(request,'website/tour.html')

def blog(request):
    return render(request,'website/blog.html')


def blog_post(request):
    return render(request,'website/blog_post.html')

def news(request):
    return render(request,'website/news.html')

def newspages(request):
    return render(request,'website/newspage.html')

def events(request):
    return render(request,'website/events.html')

def eventpages(request):
    return render(request,'website/eventpage.html')

def gallery(request):
    return render(request,'website/gallery.html')

def franchise(request):
    return render(request,'website/franchise.html')
