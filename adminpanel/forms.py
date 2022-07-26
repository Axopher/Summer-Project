from django.forms import ModelForm
from .models import *
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['StName','StPhone','StEmail']
        # exclude = ['StCName']

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

    def  __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})        

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

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