from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Chat_signup
        fields = ['first_name', 'last_name', 'email', 'username', 'password','role']


class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveForm
        fields = [
            'name',
            'reason',
            'Address',
            'City',
            'State',
            'Zipcode',
            'Room_number',
            'enrollment_number',
            'Parents_contact_number',
            'Destination',
            'Leave_From_date',
            'Leave_to_date',
        ]
        widgets = {
            'Leave_From_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Leave_to_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
