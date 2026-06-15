from django.shortcuts import render,redirect
from .models import todo,todo_history

# Create your views here.
def create(request):
    if request.method=="POST":
        task=request.POST.get("task")
        desc=request.POST.get("desc")
        priority=request.POST.get("priority")
        status=request.POST.get("status")
        todo.objects.create(task=task,desc=desc,priority=priority,status=status)
        return redirect("display")
    return render(request,"create_task.html")


def display(request):
    task1=todo.objects.all()
    return render (request,"display_task.html",{"task1":task1})


def update(request,id):
    task1=todo.objects.get(id=id)
    if request.method=="POST":
        task1.task=request.POST.get("task")
        task1.desc=request.POST.get("decs")
        task1.priority=request.POST.get("priority")
        task1.status=request.POST.get("status")
        task1.save()
        return redirect("display")
    return render(request,"update.html",{"task1":task1})

def single(request,id):
    task1=todo.objects.get(id=id)
    return render(request,"view.html",{"task1":task1})