from django.shortcuts import render
from .forms import UserRegForm
from .forms import TeacherRegForm
from .forms import StudentRegForm


def register(request):
    register_button = request.POST.get("m-btn-reg")
    name = ''
    email = ''
    password = ''

    form = UserRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'name': name, 'email': email, 'password': password, 'register_button': register_button}
    return render(request, 'register.html', context)



def teacher_registration(request):
    register_button = request.POST.get("m-btn-reg")
    name = ''
    gender = ''
    salary = ''
    age = ''
    department = ''

    form = TeacherRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        gender = form.cleaned_data.get('gender')
        salary = form.cleaned_data.get('salary')
        age = form.cleaned_data.get('age')
        department = form.cleaned_data.get('department')
    context = {'form': form, 'name': name, 'gender': gender, 'salary': salary, 'age': age, 'department': department, 'register_button': register_button}
    return render(request, 'teacher_registration.html', context)

def student_registration(request):
    register_button = request.POST.get("m-btn-reg")
    name = ''
    age = ''
    gender = ''
    score = ''

    form = StudentRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')
        gender = form.cleaned_data.get('gender')
        score = form.cleaned_data.get('score')
    context = {'form': form, 'name': name, 'age': age, 'gender': gender, 'score': score, 'register_button': register_button}
    return render(request, 'student_registration.html', context)











