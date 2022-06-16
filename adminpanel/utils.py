from .models import *

from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage



def searchStudents(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    studentObj = Student.objects.filter(StName__icontains=search_query)
    return studentObj
    
def searchFees(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    feeObj = Fee.objects.filter(FStudName__StName__icontains=search_query)

    return feeObj

def searchCourses(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    courseObj = Course.objects.filter(CName__icontains=search_query)

    return courseObj   

def searchTeachers(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    teacherObj = Teacher.objects.filter(TName__icontains=search_query)

    return teacherObj      

def paginateFees(request,fees,results):
    
    page = request.GET.get('page')
    paginator = Paginator(fees,results)

    try:
        fees = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        fees = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        fees = paginator.page(page)

    leftIndex = (int(page)-3)
    
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1    

    custom_range = range(leftIndex,rightIndex)
    return custom_range,fees
    
def paginateStudents(request,students,results):
    
    page = request.GET.get('page')
    paginator = Paginator(students,results)

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        students = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        students = paginator.page(page)

    leftIndex = (int(page)-3)
    
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1    

    custom_range = range(leftIndex,rightIndex)
    return custom_range,students


def paginateTeachers(request,teachers,results):
    
    page = request.GET.get('page')
    paginator = Paginator(teachers,results)

    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        teachers = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        teachers = paginator.page(page)

    leftIndex = (int(page)-3)
    
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1    

    custom_range = range(leftIndex,rightIndex)
    return custom_range,teachers
    
def paginateCourses(request,courses,results):
    
    page = request.GET.get('page')
    paginator = Paginator(courses,results)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        courses = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        courses = paginator.page(page)

    leftIndex = (int(page)-3)
    
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+4)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1    

    custom_range = range(leftIndex,rightIndex)
    return custom_range,courses    
    