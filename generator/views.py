import random
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h2>This is home page<h2>')
from generator import models


def home(request):
    # all_passwords = models.Passwords.objects.order_by('-id')[:10][::-1]
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html', {'creator':'Yerqanat'})


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12)) # 12 default

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    newPass = models.Passwords(password=thepassword, created_date=datetime.now())
    newPass.save()

    return render(request, 'generator/password.html', {'password': thepassword})


def oldPasswords(request):
    all_passwords = models.Passwords.objects.order_by('-id')[:10][::-1]
    return render(request, 'generator/oldPasswords.html', {'all_passwords': all_passwords})
