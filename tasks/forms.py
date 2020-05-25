from django import forms
from django.forms import ModelForm

from .models import Task

class DateInput(forms.DateTimeInput):
    input_type= 'date'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'created': DateInput()}

    
    