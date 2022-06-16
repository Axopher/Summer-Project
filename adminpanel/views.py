
from django.shortcuts import redirect, render,HttpResponse
from .models import *

from .forms import *

from django.contrib.auth.decorators import login_required

from .utils import *

from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

# user roles
from .decorators import allowed_users

# Create your views here.

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def viewDashboard(request):
    courseCount = Course.objects.all().count()
    studentCount = Student.objects.all().count()
    teacherCount = Teacher.objects.all().count()

    total_fee = 0
    feeObj = Fee.objects.all()
    for fee in feeObj:
        total_fee+=fee.FAmount
    
    context = {
        'courseCount':courseCount,
        'total_fee':total_fee,
        'studentCount':studentCount,
        'teacherCount':teacherCount
    }

    return render(request,'adminpanel/dashboard.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def student(request):
    students=searchStudents(request)

    custom_range,students = paginateStudents(request,students,10)

    context = {'students' : students,'custom_range':custom_range}
    return render(request,'adminpanel/students.html',context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def course(request):
    courses = searchCourses(request)

    custom_range,courses = paginateStudents(request,courses,10)

    context = {
        'courses':courses,
        'custom_range':custom_range
    }

    return render(request,'adminpanel/courses.html',context)  

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def teacher(request):
    teachers = searchTeachers(request)

    custom_range,teachers = paginateFees(request,teachers,10)

    context = {
        'teachers':teachers,'custom_range':custom_range    
    }
    return render(request,'adminpanel/teachers.html',context)   

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def fee(request):
    fees = searchFees(request)

    custom_range,fees = paginateFees(request,fees,10)

    

    context = {
        'fees':fees,'custom_range':custom_range
    }
    return render(request,'adminpanel/fees.html',context)       


def context_data():
    context = {
        'page_name' : '',
        'page_title' : 'Chat Room',
        'system_name' : 'Employee ID with QR Code Generator',
        'topbar' : True,
        'footer' : True,
    }

    return context

@login_required
def view_card(request, pk=None):
    if pk is None:
        return HttpResponse("Student ID is Invalid")
    else:
        context = context_data()
        context['student'] = Student.objects.get(StNum=pk)
        return render(request, 'adminpanel/view_id.html', context)



@login_required(login_url='login') 
# @allowed_users(allowed_roles=['admin'])   
def addstudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')


    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateStudent(request,pk):
    student = Student.objects.get(StNum=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {
        'form':form
    }
    return render(request,"adminpanel/edit_form.html",context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteStudent(request,pk):
    student = Student.objects.get(StNum=pk)
    context = {
        'object':student
    }
    if request.method=='POST':
        student.delete()
        return redirect('student')


    return render(request,"delete_object.html",context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def addteacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')

    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateTeacher(request,pk):
    teacher = Teacher.objects.get(TNum=pk)
    form = TeacherForm(instance=teacher)
    if request.method=='POST':
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    context={
        'form':form
    }
    return render(request,"adminpanel/edit_form.html",context) 

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteTeacher(request,pk):
    teacher = Teacher.objects.get(TNum=pk)

    context={
        'object':teacher
    }

    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher')

    return render(request,"delete_object.html",context) 


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def addcourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')

    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateCourse(request,pk):
    course = Course.objects.get(CNum=pk)
    form = CourseForm(instance=course)
    if request.method=='POST':
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course')
    context={
        'form':form
    }
    return render(request,"adminpanel/edit_form.html",context) 

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteCourse(request,pk):
    course = Course.objects.get(CNum=pk)

    context={
        'object':course
    }

    if request.method == 'POST':
        course.delete()
        return redirect('Course')

    return render(request,"delete_object.html",context) 

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def addfee(request):
    form = FeeForm()

    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee')


    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)                

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateFee(request,pk):
    fee = Fee.objects.get(FNum=pk)
    form = FeeForm(instance=fee)
    context = {
        'form' :form
    }
    if request.method == 'POST':
        form = FeeForm(request.POST,instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee')


    return render(request,"adminpanel/edit_form.html",context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteFee(request,pk):
    fee = Fee.objects.get(FNum=pk)
    context = {
        'object' :fee
    }
    if request.method == 'POST':
        fee.delete()
        return redirect('fee')


    return render(request,"delete_object.html",context)
