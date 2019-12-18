from django.shortcuts import render, redirect

from .models import ToDoItem

def index(request):

    tasks = ToDoItem.objects.all()

    context = {
        'tasks':tasks,
    }

    return render(request, 'ToDoItem/index.html', context)

def create(request):
    pass

def show(request, id):
    pass

def edit(request, id):
    pass

def delete(request, id):
    pass