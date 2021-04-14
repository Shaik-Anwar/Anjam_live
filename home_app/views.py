from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
	return render(request, 'index.html', {})

def ece(request):

    all_list=project.objects.all()
    ece = all_list.filter(branch1="ECE")
    context = {'ece': ece}
    return render(request, 'ece.html', context)

def cse(request):
	return render(request, 'cse.html', {})

def eee(request):
	return render(request, 'eee.html', {})
