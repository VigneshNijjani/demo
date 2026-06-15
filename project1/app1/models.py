from django.db import models

# Create your models here.
class students(models.Model):
    id1=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    phone=models.IntegerField()


    def __str__(self):
        return self.name
