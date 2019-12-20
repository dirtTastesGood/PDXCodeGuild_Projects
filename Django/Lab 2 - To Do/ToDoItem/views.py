from django.shortcuts import render, redirect, get_object_or_404

from .models import ToDoItem

def index(request):

    tasks = ToDoItem.objects.all()

    context = {
        'tasks':tasks,
    }

    return render(request, 'toDoItem/index.html', context)

def create(request):
    if(request.method == 'GET'):
        context = {
            'action_type': 'Create',
            'action_url': 'http://127.0.0.1:8000/new/',
        }

        return render(request, 'toDoItem/new.html', context)
    elif(request.method == 'POST'):
        new_task_title = request.POST['title']
        new_task_text = request.POST['task_text']

        task = ToDoItem.objects.create(
            title=new_task_title, 
            task_text=new_task_text
        )

        return redirect('/')


def show(request, id):
    task = get_object_or_404(ToDoItem, pk=id)

    context = {
        'task':task,
    }

    return render(request, 'toDoItem/show.html/', context)

def edit(request, id):
    task = ToDoItem.objects.get(id=id)
    if(request.method == 'GET'):
        context = {
            'task': task,
            'action_type': 'Update',
            'action_url': f'http://127.0.0.1:8000/edit/{id}',
        }
        
        return render(request,'toDoItem/edit.html', context)
    elif(request.method == 'POST'):

        task.title = request.POST['title']
        task.task_text = request.POST['task_text']
        task.save()

        return redirect('/')

def delete(request, id):
    pass