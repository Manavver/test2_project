from django.shortcuts import render

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index1.html')