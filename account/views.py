from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import SignUpForm, LoginForm, CertificatorForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404
from .models import Certificate
# Create your views here.



def index(request):
    return render(request, 'index.html')

def notavailable(request):
    return render(request, '404.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            print("step 1")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
            print(msg)
    return render(request, 'login.html', {'form': form, 'msg': msg})

def home(request):
    return render(request, 'homepage.html', {})


def certificate(request):
    cert = Certificate.objects.all()
    certificate_number = "007cae"
    context = {
       'certificate':cert
    }
    return render(request, "certificate.html", context)


def certificate_login(request):
    form = CertificatorForm
    if request.method == 'POST':
        form = CertificatorForm(request.POST)
        if form.is_valid():
            form.save()
            # msg = 'user created'
            return redirect('certificate')
        else:
            msg = 'form is not valid'
            print(msg)
    else:
        print("not posted")
        form = CertificatorForm
    return render(request, 'certificate_login.html', {'form': form})