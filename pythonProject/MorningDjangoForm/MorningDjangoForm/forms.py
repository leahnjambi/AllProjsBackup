from django import forms


# Define all the forms as classes

# This is a user registration form
class UserRegForm(forms.Form):
    # These are the input fields
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField()

# This is a teacher registration form
class TeacherRegForm(forms.Form):
    # These are the input fields
        name = forms.CharField( max_length=100)
        gender = forms.CharField(max_length=100)
        salary = forms.CharField(max_length=100)
        age = forms.CharField(max_length=50)
        department = forms.CharField(max_length=100)

# This is a student registration form
class StudentRegForm(forms.Form):
    #These are the input fields
        name = forms.CharField(max_length=100)
        age = forms.CharField()
        gender = forms.CharField()
        score = forms.CharField()




