from django.forms import ModelForm
from .models import *

class Employee_Forms(ModelForm):

     class Meta: #why we are using this which model type of this form

         model = Employee
         fields = ['name', 'emp_id', 'department', 'salary']