from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CalendarForm(forms.Form):
    from_date = forms.DateField(label=False, input_formats='%d/%m/%Y', widget=forms.DateInput(
        attrs={
            'type': 'date'
        }
    ))
    to_date = forms.DateField(label=False, input_formats='%d/%m/%Y', widget=forms.DateInput(
        attrs={
            'type': 'date'
        }
    ))

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username',)
