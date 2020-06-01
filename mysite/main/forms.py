from .models import Item

from django import forms


class TaskForm(forms.Form):
    task        = forms.CharField( max_length=100)
    complete    = forms.BooleanField(required=False)
