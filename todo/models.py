from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
class Task(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    due_date = models.DateTimeField(blank=True, null=True)

    class Priority(models.IntegerChoices):
        DEFAULT = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        ASAP = 4

    priority = models.IntegerField(choices=Priority.choices)

