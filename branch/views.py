from django.shortcuts import render,redirect
from adminapp.models import Teacher,Student,Batch
from django.contrib.auth import get_user_model

# Create your views here.
def master(request):

    print(request.user.branch.branch_name)
    details=request.user.branch
    print(details.branch_name)
    student=Student.objects.filter(branch=request.user.branch).count()
    teacher=Teacher.objects.filter(branch=request.user.branch).count()

    context={
        "is_master":True,
        "student":student,
        "teacher":teacher,
        "details":details
    }
    return render(request,'branch/home.html', context)

def students(request):
    
    batch = Batch.objects.all()
    print(batch)
    context={
        "is_students":True,
        "batch":batch
        
    }
    return render(request,'branch/students.html', context)

def studentslist(request,id):
    print(id)
    viewstudent = Student.objects.filter(course=id).all()
    print(viewstudent)
    context={
        "is_studentslist":True,
        "viewstudent":viewstudent
    }
    return render(request,'branch/students_list.html', context)

def all_students_list(request):

    student= Student.objects.filter(branch=request.user.branch)
    print(student)
    context={
        "is_all_students_list":True,
        "student":student
    }
    return render(request,'branch/allstudents_list.html', context)

def add_students_branch(request):
    studentFk= request.user.branch.id
    course=Batch.objects.all()
    print(course)
    print(studentFk)
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
        print(courseid)
        studentFk= request.user.branch
        course_id=Batch.objects.get(id=courseid)
        print(studentFk)
        std = Student(course=course_id,branch=studentFk,student_id=studentid, first_name=name, last_name=lastname, gender=gender, dob=dob, phone=phone,email=email ,password=password,fatherphone=fatherphone,fathername=fathername,address=address)
        std.save()
        User = get_user_model()
        User.objects.create_user(email=email, password=password,Student=std)

    context={
        "is_add_students_branch":True,
        "course":course
    }
    return render(request,'branch/studentsaddbranch.html', context)
def editstudent(request,id):
    details= Student.objects.get(id=id)
    if request.method=='POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        fathername = request.POST['fathername']
        fatherphone = request.POST['fatherphone']
        Student.objects.filter(id=id).update( first_name=name, last_name=lastname, gender=gender,phone=phone,email=email ,password=password,fatherphone=fatherphone,fathername=fathername)
        return redirect('/branch/allstudentslist')       

    context={
        "is_add_students_branch":True,
        "details":details
    }
    return render(request,'branch/editstudent.html', context)

def teachers(request):
    techerlist= Teacher.objects.all()
    context={
        "is_teachers":True,
        "techerlist":techerlist
    }
    return render(request,'branch/teacherslist.html', context)

def add_teachers(request):
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
        techerfk= request.user.branch
        
        techer = Teacher(branch=techerfk,teacher_id=techer_id,Password=Password,name=name,gender=gender,dob=Dob ,phone=mobile, email=email, joining_date=JoiningDate, qualification=Qualification, experience=Experience, address=address,pin=zipcode,country=country,state=state,city=city)
        techer.save()
        User = get_user_model()
        User.objects.create_user(email=email, password=Password,teacher=techer)
    context={
        "is_add_teachers":True
    }
    return render(request,'branch/addteacher.html', context)


def editteacher(request,id):
    details= Teacher.objects.get(id=id)
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
        Teacher.objects.filter(id=id).update(Password=Password,name=name,gender=gender,dob=Dob ,phone=mobile, email=email, joining_date=JoiningDate, qualification=Qualification, experience=Experience, address=address,pin=zipcode,country=country,state=state,city=city)
        return redirect('/branch/teacherslist')
    print(details)
    
    context={
        "is_teachers":True,
        "details":details
    }
    return render(request,'branch/editteacher.html', context)
def courses(request):
    context={
        "is_courses":True
    }
    return render(request,'branch/courses.html', context)

def add_courses(request):
    context={
        "is_add_courses":True
    }
    return render(request,'branch/addcourses.html', context)

def fees(request):
    context={
        "is_fees":True
    }
    return render(request,'branch/fees.html', context)

def add_fees(request):
    context={
        "is_add_fees":True
    }
    return render(request,'branch/add_fees.html', context)


# profile

def profile_branch(request):
    details=request.user.branch
    context={
        "is_exam_list":True,
        "details":details
    }
    return render(request,'branch/profile_branch.html',context)

# exam 

def exam_list(request):
    context={
        "is_exam_list":True
    }
    return render(request,'branch/exam_list.html', context)

def exam_add_b_one(request):
    context={
        "is_exam_add_b_one":True
    }
    return render(request,'branch/exam_addb1.html', context)

def exam_add_b_two(request):
    context={
        "is_exam_add_b_two":True
    }
    return render(request,'branch/exam_addb2.html', context)

def exam_add_b_Three(request):
    context={
        "is_exam_add_b_three":True
    }
    return render(request,'branch/exam_addb3.html', context)