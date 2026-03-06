from django.shortcuts import render,redirect
from .models import Task 
# Create your views here.
from django.views import View
from django.views.generic import CreateView

class Tasklist(CreateView):
    def get(self,request):
        tasks = Task.objects.all()
        context = {'task':tasks}
        return render(request,'main/home.html',context)
    def post(self,request):
        task = Task.objects.create(
            task_name = request.POST.get('task_name'),
            task_description = request.POST.get('task_description'),
            completed = request.POST.get('completed') == 'on'
        )
        task.save()
        return redirect('tasks')