from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'my_gallery')

def login(request):
    return render(request, 'my_login')

def register(request):
    return render(request, 'my_register')
