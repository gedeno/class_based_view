from django.shortcuts import render,redirect
from .models import Task 
from .forms import FormTask
# Create your views here.
from django.views import View
from django.views.generic import CreateView, ListView

class Tasklist(CreateView):
    model = Task
    form_class = FormTask
    template_name = "main/home.html"
    success_url = "/"
class Feach(ListView): 
    model = Task
    context_object_name = "base"
    template_name = "main/base.html"
class Feach2(ListView):
    model = Task
    template_name = 'main/display.html'
    context_object_name = "base"
    def get_queryset(self):
        return Task.objects.all()
class Feach3(ListView):
    model = Task
    template_name = 'main/display2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_lists'] = Task.objects.all()
        return context