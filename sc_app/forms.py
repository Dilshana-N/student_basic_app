from django import forms
from django.contrib.auth.forms import UserCreationForm

from sc_app.models import Login, Student_Register, Complaint, Notification


class login_form(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class student_register_form(forms.ModelForm):
    class Meta:
        model = Student_Register
        fields = '__all__'
        exclude = ('user',)

class complaint_form(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('complaint',)

class notification_form(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('notifications',)

