from django.contrib import admin
from .models import students,students_history

# Register your models here.
admin.site.register(students),
admin.site.register(students_history)
