from django.shortcuts import render,redirect
from .models import proffesor

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        sal=request.POST.get("sal")
        branch=request.POST.get("branch")
        email=request.POST.get("email")
        exp=request.POST.get("exp")
        proffesor.objects.create(name=name,sal=sal,branch=branch,email=email,exp=exp)
        return redirect("details")
    return render(request,"index.html")

def details(request):
    prof=proffesor.objects.all()
    return render(request,"table.html",{"prof":prof})
