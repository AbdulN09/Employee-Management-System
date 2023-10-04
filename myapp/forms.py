from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employeeId', 'fullName', 'phone', 'dob', 'nationality', 'email', 'company', 'position', 'salary', 'projects']



