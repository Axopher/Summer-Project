from django.forms import ModelForm
from .models import *
from django import forms

from users.models import Product

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['StName','StPhone','StEmail']
        exclude = ['StImage']
        labels = {
            'StName':'Name',
            'StPhone':'Phone',
            'StEmail':'Email',
            'StAddress':'Address',
            'StDob':'Dob',
            'StCName':'Course',
            'StGender':'Gender',
            'StRemarks':'Remarks'
        }

        widgets = {
            'StCName': forms.CheckboxSelectMultiple(),
        }


    def  __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'TName':'Name',
            'TPhone':'Phone',
            'TEmail':'Email',
            'TAddress':'Address',
            'TDob':'Dob',
            'TQualification':'Qualification',
            'TGender':'Gender',
        }

    def  __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})        

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'CName':'Course',
            'CTName':'Teacher',
            'CPrice':'Price',
            'CDuration':'Duration',
        }

        widgets = {
            'CTName': forms.CheckboxSelectMultiple(),
        }

    def  __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})        

class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        labels = {
            'FStudName':'Course',
            'FCourseName':'Teacher',
            'FAmount':'Price',
            }


        widgets = {
            'FCourseName': forms.CheckboxSelectMultiple()
        }

    # Admission = forms.CharField(widget=forms.NumberInput(attrs={"disabled"}))

    def  __init__(self, *args, **kwargs):
        super(FeeForm, self).__init__(*args, **kwargs)
        self.fields['Admission'].widget.attrs['readonly'] = True
        self.fields['Refundable_Deposit'].widget.attrs['readonly'] = True

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})    



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        # widgets = {
        #     'CTName': forms.CheckboxSelectMultiple(),
        # }

    def  __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})        
