from django.shortcuts import render,redirect
from .models import details

# Create your views here.
def dashboard(request):
    return render(request,"dashboard.html")
def signup(request):
    if request.method=='POST':
        name=request.POST.get("name")
        phno=request.POST.get("phno")
        password=request.POST.get("password")
        details.objects.create(name=name,phone_number=phno,password=password)
        return redirect("homepage")
    return render(request,"signup.html")
