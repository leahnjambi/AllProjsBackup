from django.shortcuts import render
from .forms import userForm

def index(request):
    submit_button = request .POST.get('submit')
    name =''
    email =''
    password =''

    form = userForm(request.POST or none)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        context = {'form': form, 'name': name,
                   'email': email, 'password': password,
                   'submit_button': submit_button}

    return render(request, 'index_html', context)


def login(request):
    return render(request, 'my_login')

def register(request):
    return render(request, 'my_register')