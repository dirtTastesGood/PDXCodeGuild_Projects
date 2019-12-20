from django.shortcuts import render, redirect

from .models import ToDoItem

def index(request):

    tasks = ToDoItem.objects.all()

    context = {
        'tasks':tasks,
    }

    return render(request, 'ToDoItem/index.html', context)

def create(request):
    if(request.method == 'GET'):
        return render(request, 'ToDoItem/new.html')
    elif(request.method == 'POST'):
        new_task_title = request.POST['title']
        new_task_text = request.POST['task_text']

        task = ToDoItem.objects.create(
            title=new_task_title, 
            task_text=new_task_text
        )

        return redirect('/')


def show(request, id):
    pass

def edit(request, id):
    pass

def delete(request, id):
    pass