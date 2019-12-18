from django.shortcuts import render

from .models import ToDoItem

def index(request):

    tasks = ToDoItem.objects.all()

    context = {
        'tasks':tasks,
    }

    return render(request, 'ToDoItem/index.html', context)
