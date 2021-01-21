from django.contrib import admin
from .models import Task, Category, Person
# Register your models here.
admin.register(Task)
admin.register(Category)
admin.register(Person)