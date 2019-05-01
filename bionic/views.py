from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'bionic/home.html')

def about(request):
	return render(request, 'bionic/about.html')