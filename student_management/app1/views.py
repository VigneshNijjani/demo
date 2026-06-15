from django.shortcuts import render,redirect
from .models import students,students_history

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST.get("name")
        age=request.POST.get("age")
        rollno=request.POST.get("rollno")
        gender=request.POST.get("gender")
        branch=request.POST.get("branch")
        email=request.POST.get("email")
        students.objects.create(name=name,age=age,rollno=rollno,gender=gender,branch=branch,email=email)
        return redirect("display")
    return render(request,"home.html")


def display(request):
    student=students.objects.all()
    return render(request,"display.html",{"student":student})


def update(request,id):
    student=students.objects.get(id=id)
    
    if request.method=='POST':            
        student.name=request.POST.get("name")
        student.age=request.POST.get("age")
        student.rollno=request.POST.get("rollno")
        student.gender=request.POST.get("gender")
        student.branch=request.POST.get("branch")
        student.email=request.POST.get("email")
        student.save()
        return redirect("display")

    return render(request,"update.html",{"student":student})


def delete(request,id):
    student=students.objects.get(id=id)
    students_history.objects.create(
        name=student.name,
        age=student.age,
        rollno=student.rollno,
        gender=student.gender,
        branch=student.branch,
        email=student.email)
    student.delete()
    return redirect("history")


def history(request):
    student=students_history.objects.all()
    return render(request,"history.html",{"student":student})


def undo(request,id):
    student=students_history.objects.get(id=id)
    students.objects.create(
    name=student.name,
    age=student.age,
    rollno=student.rollno,
    gender=student.gender,
    branch=student.branch,
    email=student.email)
    student.delete()
    return redirect("display")



def per_delete(request,id):
    student=students_history.objects.get(id=id)
    student.delete()
    return redirect("history")

