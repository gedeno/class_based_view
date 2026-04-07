from django.shortcuts import render,redirect
from .models import Task 
from .forms import FormTask
from django.views.generic.edit import FormView
from . forms import contactForm
# Create your views here.
from django.views import View
from django.views.generic import CreateView, ListView ,DeleteView

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
        context["Tasks"] = Task.objects.all()
        return context
class ContactFormview(FormView):
    template_name = "main/contact.html"
    form_class = contactForm
    success_url = "/"
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
class Dataupdate(DeleteView):
    model = Task
    template_name = 'main/completed.html'
    context_object_name = 'work'
    def get_object(self):
        return Task.objects.get(id=self.kwargs['pk'])
    def post(self, request, *args, **kwargs):
        complet = request.POST.get('complet')
        user = self.get_object()
        user.completed = complet
        user.save()
        return redirect('home')
