from rest_framework import serializers
from .models import Employee

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

        read_only=id

        extra_kwargs={
            "age":{
                "write_only":True
            },
            "dept":{
                "required":False,
                "default":"cse",
            }
        }
