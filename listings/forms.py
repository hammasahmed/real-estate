from django import forms
from .models import UserInput

class AddListingsForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['name', 'discription']
        