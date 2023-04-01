from django import form
class userForm(forms_Form):
    name  = forms.CharField(max_length = 100)
    email = forms.CharField(max_length=100)
    password = form.CharField()