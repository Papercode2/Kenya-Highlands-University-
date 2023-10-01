from django import forms
from .models import ContactFormSubmission
from .models import Units,Nominals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'message']




class Units(forms.ModelForm):
    class Meta:
        model = Units
        fields = ['Unit_Name', 'Unit_Code']

class Nominals(forms.ModelForm):
   class Meta:
        model = Nominals
        fields = ['Student_Name', 'Student_ID','Course', 'Semester']



class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username', 'email','password1','password2'] 

