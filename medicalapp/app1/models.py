from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=200)
    phone_number=models.IntegerField(unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.name
