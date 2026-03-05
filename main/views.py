from django.shortcuts import render,redirect
from .models import Task 
# Create your views here.
from django.views import View

class Tasklist(View):
    def get(self,request):
        tasks = Task.objects.all().order_by('-updated')
        context = {'task':tasks}
        return render(request,'main/home.html',context)
    def post(self,request):
        task = Task.objects.create(
            body = request.POST.get('body')
        )
        task.save()
        return redirect('tasks')