from django.shortcuts import render,redirect
from.models import employee

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get("name")
        age=request.POST.get("age")
        dept=request.POST.get("dept")
        sal=request.POST.get("sal")
        company=request.POST.get("company")
        employee.objects.create(name=name,age=age,dept=dept,sal=sal,company=company)
        return redirect("details")
    return render(request,"home.html")

def details(request):
    emp=employee.objects.all()
    return render(request,"details.html",{"emp":emp})

def single(request,id):
    emp=employee.objects.get(id=id)
    return render(request,"single.html",{"emp":emp})

def update(request,id):
    emp=employee.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("name")
        age=request.POST.get("age")
        dept=request.POST.get("dept")
        sal=request.POST.get("sal")
        company=request.POST.get("company")
        

        if emp.id==id:
            emp.name=name
            emp.age=age
            emp.dept=dept
            emp.sal=sal
            emp.company=company
            emp.save()
            return redirect("single",id=id)
    return render(request,"update.html",{"emp":emp})

def delete(request,id):
    emp=employee.objects.get(id=id)
    emp.delete()
    return redirect("details")