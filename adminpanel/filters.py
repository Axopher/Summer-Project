import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class StudentFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="created",lookup_expr="gte")
    # end_date = DateFilter(field_name="created",lookup_expr="lte")
    StPhone = CharFilter(field_name="StPhone",lookup_expr='icontains')
    StEmail = CharFilter(field_name="StEmail",lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ['StPhone','StEmail']




class CourseFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="created",lookup_expr="gte")
    # end_date = DateFilter(field_name="created",lookup_expr="lte")
    # CName = CharFilter(field_name="CName",lookup_expr='icontains')
    # CTName = CharFilter(field_name="CTName",lookup_expr='icontains')
    class Meta:
        model = Course
        fields = ['CPrice','CDuration']

       

class TeacherFilter(django_filters.FilterSet):
    TPhone = CharFilter(field_name="TPhone",lookup_expr='icontains')
    
    class Meta:
        model = Teacher
        fields = ['TPhone','TQualification']        


class FeeFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="FDate",lookup_expr="gte")
    end_date = DateFilter(field_name="FDate",lookup_expr="lte")
    