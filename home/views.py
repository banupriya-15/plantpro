from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'home/home.html')

def scan(request, *args, **kwargs):
    return render(request, 'home/scan.html')

def remedy(request, *args, **kwargs):
    return render(request, 'home/remedy.html')

def status(request, *args, **kwargs):
    return render(request, 'home/status.html')
