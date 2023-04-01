from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

courses = [
    {"name", "Python", "duration", "2 months", "cost", "Ksh 25k"},
    {"name", "Android", "duration", "2 months", "cost", "Ksh 25k"},
    {"name", "Datascience", "duration", "4 months", "cost", "Ksh 60k"},

]
def courses(request):
    context = {"courses":courses}
    return render(request, 'courses.html', context)




