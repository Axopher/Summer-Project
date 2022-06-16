from django.forms import ModelForm
from .models import Profile
from django.forms.widgets import DateInput

from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields = '__all__'

        labels = {
            'comment':'your experience with instruments',
            'dob': ('D.O.B'),
        }