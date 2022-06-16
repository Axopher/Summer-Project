from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.viewDashboard,name='dashboard'),
    path('students/',views.student,name='student'),
    path('courses/',views.course,name='course'),
    path('teachers/',views.teacher,name='teacher'),
    path('fees/',views.fee,name='fee'),
    path('view_card/<str:pk>',views.view_card,name='view-card'),
    path('add-student/',views.addstudent,name='add-student'),
    path('add-teacher/',views.addteacher,name='add-teacher'),
    path('add-course/',views.addcourse,name='add-course'),
    path('add-fee/',views.addfee,name='add-fee'),
    path('update-student/<str:pk>/',views.updateStudent,name='update-student'),
    path('update-teacher/<str:pk>/',views.updateTeacher,name='update-teacher'),
    path('update-course/<str:pk>/',views.updateCourse,name='update-course'),
    path('update-fee/<str:pk>/',views.updateFee,name="update-fee"),
    path('delete-student/<str:pk>/',views.deleteStudent,name="delete-student"),
    path('delete-teacher/<str:pk>/',views.deleteTeacher,name="delete-teacher"),
    path('delete-course/<str:pk>/',views.deleteCourse,name="delete-course"),
    path('delete-fee/<str:pk>/',views.deleteFee,name="delete-fee"),
]