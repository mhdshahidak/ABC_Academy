from django.shortcuts import render

from adminapp.models import Branch
from website.models import OnlineApplying

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
    if request.method == "POST":
        first_name = request.POST['name_apply']
        last_name = request.POST['lastname_apply']
        email = request.POST['email_apply']
        phone = request.POST['phone_apply']
        dob = request.POST['birth_apply']
        gender = request.POST['gender_apply']
        address = request.POST['address_apply']
        town = request.POST['town_apply']
        country = request.POST['country_apply']
        pin = request.POST['postal_code_apply']
        branch_apply = request.POST['branch_apply']
        course = request.POST['fav_course']

        branch = Branch.objects.get(id=branch_apply)
        new_apply = OnlineApplying(first_name=first_name,last_name=last_name,email=email,phone=phone,gender=gender,dob=dob,course=course,branch=branch,address=address,city=town,country=country,pin=pin)
        new_apply.save()
        context = {
            "status":1
        }
    context = {
        "branches":branches,
        "status":0
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
