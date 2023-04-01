from django.shortcuts import render

def home(request):
    return render(request, 'my_home')

def about(request):
    return render(request, 'my_about')

