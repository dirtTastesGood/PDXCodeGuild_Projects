from django.shortcuts import render

from .models import ToDoItem

def index(request):

    items = ToDoItem.objects.all()

    return render(request, 'ToDoItem/index.html', {'items':items})
