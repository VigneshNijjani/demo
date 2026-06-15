from django.db import models

# Create your models here.
class todo(models.Model):
    task=models.CharField(max_length=100)
    desc=models.TextField()
    priority=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class todo_history(models.Model):
    task=models.CharField(max_length=100)
    desc=models.TextField()
    priority=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.name
