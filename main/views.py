from django.shortcuts import render,redirect
from .models import Task 
from .forms import FormTask
# Create your views here.
from django.views import View
from django.views.generic import CreateView

class Tasklist(CreateView):
    model = Task
    form_class = FormTask
    template_name = "main/home.html"
