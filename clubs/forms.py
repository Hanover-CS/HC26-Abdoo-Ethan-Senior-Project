# clubs/forms.py
# Contains Django ModelForms for the clubs app.
# Currently includes ClubForm for creating and validating Club objects.


from django import forms
from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'city', 'country', 'contact_email']
