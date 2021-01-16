from .models import Task, Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name','category','created_date','due_date','priority')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','task_set',)
