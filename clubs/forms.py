# clubs/forms.py
# Contains Django ModelForms for the clubs app.
# Currently includes ClubForm for creating and validating Club objects.


from django import forms
from .models import Club
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'city', 'country', 'contact_email']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]