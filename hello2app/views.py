from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
  return render(request,"PYC01-HTMLJSDEMO.html")

def hello1(request):
  return render(request,"PYC01-HTMLJSDEMO1.html")