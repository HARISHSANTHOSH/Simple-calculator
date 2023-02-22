
from django.shortcuts import render,redirect
import os
from django.http import HttpResponse

from .models import *

from django.contrib.auth.models import User
import uuid
from django.contrib import messages

from django.core.mail import send_mail
from django.contrib.auth import authenticate


# Create your views here.


def freak(request):

    return HttpResponse("hai freak")

def calculator(request):

    return render(request,"calculator.html")