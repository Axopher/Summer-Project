
from calendar import month
from django.shortcuts import redirect, render,HttpResponse
from .models import *

from .forms import *

from django.contrib.auth.decorators import login_required

from .utils import * 
from users.models import Order

# from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

# user roles
# from .decorators import allowed_users


import re
from django.contrib import messages

# for charts
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def viewDashboard(request):
    courseCount = Course.objects.all().count()
    studentCount = Student.objects.all().count()
    teacherCount = Teacher.objects.all().count()
    fees = Fee.objects.all()

    total_fee = 0
    for fee in fees:
        total_fee+=fee.FAmount
    

    # monthly fee dictionary calculations
    monthly_fees_dict = {}
    for fee in fees:
        if fee.FDate.strftime("%B") not in monthly_fees_dict:
            monthly_fees_dict[fee.FDate.strftime("%B")] = fee.FAmount
        else:
            monthly_fees_dict[fee.FDate.strftime("%B")] += fee.FAmount   
      
    # end of monthly fee dictionary calculations
   

    # top courses count
    students = Student.objects.all()
    total_courses = {}
    for student in students:
        for cname in student.StCName.all():
            if cname not in total_courses:
                total_courses[cname] = 1
            else:
                total_courses[cname] += 1 

    sort_courses = sorted(total_courses.items(), key=lambda x: x[1], reverse=True)
    # end of top courses count

    # Fees generating courses 
    total_fees_by_courses = {}
    for fee in fees:       
        for cname in fee.FCourseName.all():
            if cname not in total_fees_by_courses:
                print(type(cname))
                total_fees_by_courses[cname] = fee.FAmount
            else:
                total_fees_by_courses[cname] += fee.FAmount

    sort_courses_by_fees = sorted(total_fees_by_courses.items(), key=lambda x: x[1], reverse=True)
    # end of Fees generating courses

    # payment read count
    unreadCount = Order.objects.filter(is_read=False).count()

    context = {
        'courseCount':courseCount,
        'total_fee':total_fee,
        'studentCount':studentCount,
        'teacherCount':teacherCount,
        'sortedCourse':sort_courses,
        'fees':fees,
        'monthly_fees_dict':monthly_fees_dict,
        'sort_courses_by_fees':sort_courses_by_fees,
        'unreadCount':unreadCount,
    }


    return render(request,'adminpanel/dashboard.html',context)


@login_required(login_url='login')
def viewPayment(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    orders = Order.objects.filter(sname__icontains=search_query)

    custom_range,orders = paginateOrders(request,orders,7)



    context = {'orders':orders,'custom_range':custom_range}
    return render(request,'adminpanel/payments.html',context)



@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def student(request):
    students,myFilter=searchStudents(request)

    custom_range,students = paginateStudents(request,students,7)

    context = {'students' : students,'custom_range':custom_range,'myFilter':myFilter}
    return render(request,'adminpanel/students.html',context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def course(request):
    courses,myFilter = searchCourses(request)

    custom_range,courses = paginateStudents(request,courses,7)

    context = {
        'courses':courses,
        'custom_range':custom_range,
        'myFilter':myFilter
    }

    return render(request,'adminpanel/courses.html',context)  

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def teacher(request):
    teachers,myFilter = searchTeachers(request)

    custom_range,teachers = paginateFees(request,teachers,7)

    context = {
        'teachers':teachers,'custom_range':custom_range,'myFilter':myFilter    
    }
    return render(request,'adminpanel/teachers.html',context)   

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def fee(request):
    fees,myFilter = searchFees(request)

    custom_range,fees = paginateFees(request,fees,7)

    context = {
        'fees':fees,'custom_range':custom_range,'myFilter':myFilter
    }
    return render(request,'adminpanel/fees.html',context)       



@login_required(login_url='login') 
# @allowed_users(allowed_roles=['admin'])   
def addstudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        dob = request.POST['StDob']
        phn = request.POST['StPhone']
        phn_pattern = re.compile('^9(8|7)\d{8}$')
        dob_pattern = re.compile('^(19\d{2}|(2\d{3}))[-/](0|1)\d{1}[-/](0|1|2|3)(0|1|2|3)$')

        if(phn_pattern.match(phn)):
            if(dob_pattern.match(dob)):
                if form.is_valid():
                    form.save()
                messages.success(request,'Student successfully added.')    
                return redirect('student')  
            else:
                messages.warning(request,'Invalid date of birth')
        else:
            messages.warning(request,'Invalid phone number')    

        
        
        # form = StudentForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('student')


    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateStudent(request,pk):
    student = Student.objects.get(StNum=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        
        phn = request.POST['StPhone']
        dob = request.POST['StDob']

        phn_pattern = re.compile('^9(8|7)\d{8}$')
        dob_pattern = re.compile('^(19\d{2}|(2\d{3}))[-/](0|1)\d{1}[-/](0|1|2|3)(0|1|2|3)$')

        if(phn_pattern.match(phn)):
            if(dob_pattern.match(dob)):
                if form.is_valid():
                    form.save()
                    messages.success(request,'Table updated successfully.')    
                    return redirect('student')  
                else:
                    messages.warning(request,"Table update failed")
            else:
                messages.warning(request,'Invalid date of birth')
        else:
            messages.warning(request,'Invalid phone number')     

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
        messages.success(request,'Deletion successful.')
        return redirect('student')


    return render(request,"delete_object.html",context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def addteacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)

        phn = request.POST['TPhone']
        dob = request.POST['TDob']

        phn_pattern = re.compile('^9(8|7)\d{8}$')
        dob_pattern = re.compile('^(19\d{2}|(2\d{3}))[-/](0|1)\d{1}[-/](0|1|2|3)(0|1|2|3)$')

        if(phn_pattern.match(phn)):
            if(dob_pattern.match(dob)):
                if form.is_valid():
                    form.save()
                    messages.success(request,'Teacher successsfully added.')    
                    return redirect('teacher')
                else:
                    messages.warning(request,'Failed to add teacher.')
            else:
                messages.warning(request,'date of birth is incorrect')    
        else:
            messages.warning(request,'phone number is incorrect')    

    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateTeacher(request,pk):
    teacher = Teacher.objects.get(TNum=pk)
    form = TeacherForm(instance=teacher)
    if request.method=='POST':
        form = TeacherForm(request.POST,instance=teacher)

        phn = request.POST['TPhone']
        dob = request.POST['TDob']

        phn_pattern = re.compile('^9(8|7)\d{8}$')
        dob_pattern = re.compile('^(19\d{2}|(2\d{3}))[-/](0|1)\d{1}[-/](0|1|2|3)(0|1|2|3)$')

        if(phn_pattern.match(phn)):
           if(dob_pattern.match(dob)):
                if form.is_valid():
                    form.save()
                    messages.success(request,'Table Updated Successfully.')    
                    return redirect('teacher')  
                else:
                    messages.warning(request,'Update Failed.')    
           else:
               messages.warning(request,'Date of birth is incorrect')    
        else:
            messages.warning(request,'Phone number is incorrect') 

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
        messages.success(request,'Deletion successful.')
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
            messages.success(request,'Course Added Successfully.') 
            return redirect('course')
        else:
            messages.warning(request,'Course could not be added.')     

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
            messages.success(request,'Table Updated Successfully.') 
            return redirect('course')
        else:
            messages.warning(request,'Table Update Failed.') 
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
        messages.success(request,'Deletion successful.')
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
            messages.success(request,'Fee added successfully.') 
            return redirect('fee')
        else:
            messages.warning(request,'Failed to add fee.')
            


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
            messages.success(request,'Table updated successfully.') 
            return redirect('fee')
        else:
            messages.warning(request,'Table update failed.')


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
        messages.success(request,'Deletion successful.')
        return redirect('fee')


    return render(request,"delete_object.html",context)


@login_required(login_url='login')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('home')
        else:
            messages.warning(request,'Failed to add Product.')
            


    context = {'form':form}
    return render(request,'adminpanel/edit_form.html',context)      


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)

    context={
        'object':product
    }

    if request.method == 'POST':
        product.delete()
        return redirect('home')

    return render(request,"delete_object.html",context) 