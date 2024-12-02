from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from .models import *


# Create your views here.

def test(request):
    return HttpResponse("ONLINE ACTION SYSTEM")


