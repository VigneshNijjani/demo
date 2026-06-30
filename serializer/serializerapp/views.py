import json
from django.http import JsonResponse
from django.shortcuts import render
from .serializer import Employeeserializer
from .models import Employee
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_employee(req):
    inp_data=json.loads(req.body)
    filtered_data=Employeeserializer(data=inp_data)
    if filtered_data.is_valid():
        filtered_data.save()
        return JsonResponse({"status":"Employee created"})
    else:
        return JsonResponse(filtered_data.errors)

def view_employee(req,inp_id):
    employee_data=Employee.objects.get(id=inp_id)
    filtered_data=Employeeserializer(employee_data)
    return JsonResponse(filtered_data.data)

@csrf_exempt
def update_employee(req,inp_id):
    employee_data=Employee.objects.get(id=inp_id)
    if req.method =="PATCH":
        data=json.loads(req.body)
        if "name" in data:
            employee_data.name=data["name"]
        if "age" in data:
            employee_data.age=data["age"]
        if "sal" in data:
            employee_data.sal=data["sal"]
        if "dept" in data:
            employee_data.dept=data["dept"]
    
    employee_data.save()
    return JsonResponse({"status":"updated sucessfully"})

def delete_employee(req,inp_id):
    employee=Employee.objects.get(id=inp_id)
    employee.delete()
    return JsonResponse({"status":"deleted sucessfully"})
         

def display(req):
    employee_data=Employee.objects.all()
    filtered_data=Employeeserializer(employee_data,many=True)
    return JsonResponse(filtered_data.data,safe=False)
    
