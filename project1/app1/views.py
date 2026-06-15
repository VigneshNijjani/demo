from django.shortcuts import render
from .models import students

# Create your views here.
def home(request):
    if request.method=="POST":
        id1=request.POST.get("id")
        name=request.POST.get("name")
        age=request.POST.get("age")
        course=request.POST.get("course")
        phone_number=request.POST.get("phno")

        student=students.objects.create(id1=id1,name=name,age=age,course=course,phone=phone_number)
    student=students.objects.all()

    return render(request,"home.html",{"student":student})