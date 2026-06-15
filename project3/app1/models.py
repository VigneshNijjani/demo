from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    sal=models.IntegerField()
    exp=models.IntegerField()

    def __str__(self):
        return self.name
    
    
