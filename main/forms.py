from django.forms import ModelForm  
from django import forms
from .models import Task

class FormTask(ModelForm):
    class Meta:
        model = Task 
        fields = "__all__"
class contactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    def send_email(self):
        pass 

