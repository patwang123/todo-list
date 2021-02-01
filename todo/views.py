from django.shortcuts import render, redirect
import django
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

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def home(request):
    template = 'tasks.html'

    # FILTER BY COMPLETED, ANNOTATE TIME LEFT, ETC
    incomplete_tasks = Task.objects.all().order_by('due_date')
    categories = Category.objects.all()
    people = Person.objects.all()

    if request.method == "POST":  # checking if the request method is a POST
        print(request.POST)
        if "add_task" in request.POST:  # checking if there is a request to add a todo
            name = request.POST['name']

            description = request.POST['description']

            due_date = request.POST["date"]  # date
            if due_date == '':
                due_date = None

            category = request.POST['category']
            if category == '':
                category = 'General'
            category, _ = Category.objects.get_or_create(name=category)

            person = request.POST['person']
            if person == '':
                person = None
            person, _ = Person.objects.get_or_create(name=person)


            priority = request.POST['priority']
            Todo = Task(name=name, description=description, due_date=due_date,
                            category=category, person=person, priority = priority)

            Todo.save()
            return redirect("/")

        if "delete_task" in request.POST:

            id_to_delete = request.POST.getlist("id_to_delete")
            for todo_id in id_to_delete:
                todo = Task.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo

            return redirect('/')

    if request.is_ajax():
        template = 'category_template.html'
        return render(request, template, {'todo_tasks': incomplete_tasks})

    return render(request, template, {'todo_tasks': incomplete_tasks, 'categories': categories, 'people': people, 'priorities': [x[0] for x in Task.Priority.choices]})

def completed(request):
    template = 'tasks.html'

    completed_tasks = Task.objects.all() #FILTER BY COMPLETED, ANNOTATE TIME LEFT, ETC

    return render(request, template, {'todo_tasks': completed_tasks})

def per_person(request):
    template = 'persons.html'

    tasks_per_person = Person.objects.all() #FILTER TASKSET BY COMPLETED ETC

    return render(request, template, {'peoples_tasks': tasks_per_person})
