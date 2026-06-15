from django.contrib import admin
from .models import todo,todo_history

# Register your models here.
admin.site.register(todo)
admin.site.register(todo_history)
