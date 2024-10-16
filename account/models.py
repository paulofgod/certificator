from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _  # Django 4.0
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(unique=True, null=True)
    REQUIRED_FIELDS = ['email']



class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    courses = (
        ('Web Development', 'Web Development'),
        ('Data Science' , 'Data Science' ), 
        ('Graphics Design', 'Graphics Design' ),
        ('piano Instrument Expertise', 'piano Instrument Expertise' ),
        ('Guitar Instrument Expertise', 'Guitar Instrument Expertise' ),
        ('Crypto-currency Trading', 'Crypto-currency Trading'),
        ('Foreign Exchange Trading', 'Foreign Exchange Trading'),
        ('Criminology', 'Criminology'),
    )
    courses_list = models.CharField(max_length=30, blank=True, null=True, choices=courses)


