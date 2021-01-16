from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)

class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now())
    due_date = models.DateTimeField(blank=True, null=True, default='General')

    class Priority(models.IntegerChoices):
        DEFAULT = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        ASAP = 4

    priority = models.IntegerField(choices=Priority.choices)

