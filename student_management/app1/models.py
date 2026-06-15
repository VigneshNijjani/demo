from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    branch=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class students_history(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    branch=models.CharField(max_length=10)
    email=models.EmailField()

    def __str__(self):
        return self.name