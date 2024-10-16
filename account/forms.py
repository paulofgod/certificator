from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Certificate

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class CertificatorForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['courses_list' ]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','email','password1', 'password2']





# class Certificate(models.Model):
#     fullname = models.CharField(max_length=30, blank=True)
#     date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
#     courses = (
#         ('Web Development', 'Web Development'),
#         ('Data Science' , 'Data Science' ), 
#         ('Graphics Design', 'Graphics Design' ),
#         ('piano Instrument Expertise', 'piano Instrument Expertise' ),
#         ('Guitar Instrument Expertise', 'Guitar Instrument Expertise' ),
#         ('Crypto-currency Trading', 'Crypto-currency Trading'),
#         ('Foreign Exchange Trading', 'Foreign Exchange Trading'),
#         ('Criminology', 'Criminology'),
#     )
#     courses_list = models.CharField(max_length=30, blank=True, null=True, choices=courses)
