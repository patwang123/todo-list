from .models import Task, Category, Person
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name','description','category','person','created_date','due_date','priority')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','task_set',)
        depth = 2

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'task_set',)
        depth = 2