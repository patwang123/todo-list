from .models import Task, Category, Person
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name','category','created_date','due_date','priority')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','task_set',)

class PersonSerializer(serializers.ModelSerializers):
    class Meta:
        model = Person
        fields = ('name', 'task_set',)