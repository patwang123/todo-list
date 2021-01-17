from django.shortcuts import render
from .models import Task, Category, Person
from .serializers import TaskSerializer, CategorySerializer, PersonSerializer
from rest_framework import viewsets
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def home(request):
    template = 'tasks.html'

    # FILTER BY COMPLETED, ANNOTATE TIME LEFT, ETC
    incomplete_tasks = Task.objects.all()

    return render(request, template, {'todo_tasks': incomplete_tasks})

def completed(request):
    template = 'tasks.html'

    completed_tasks = Task.objects.all() #FILTER BY COMPLETED, ANNOTATE TIME LEFT, ETC
    return render(request, template, {'todo_tasks': completed_tasks})

def per_person(request):
    template = 'persons.html'

    tasks_per_person = Person.objects.all()
    return render()