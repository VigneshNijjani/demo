from django.shortcuts import render,redirect
from .models import emp

# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        dept=request.POST.get("dept")
        sal=request.POST.get("sal")
        exp=request.POST.get("exp")

        emp.objects.create(name=name,dept=dept,sal=sal,exp=exp)
        return redirect(display)
    return render(request,"index.html")

def display(request):
    a=emp.objects.all()
    return render(request,"table.html",{"emp":a})