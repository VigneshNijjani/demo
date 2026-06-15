from django.db import models

# Create your models here.
class proffesor(models.Model):
    name=models.CharField(max_length=100)
    sal=models.IntegerField()
    branch=models.CharField(max_length=4)
    email=models.EmailField()
    exp=models.IntegerField()

    def __str__(self):
        return self.name
