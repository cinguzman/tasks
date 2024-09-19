from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import CreateNewTask

def index(request):
    title = 'Mis Tareas!!'
    return render(request, 'index.html', {'titulo': title})

def list_tasks(request):
    tarea = Task.objects.all()
    return render(request, 'tasks/list.html',{'tasks': tarea
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create.html', {'form':CreateNewTask()})
    else: 
        Task.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect('list_tasks')

def edit_task(request, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        tarea.title = request.POST.get('title')
        tarea.description = request.POST.get('description')
        tarea.save()
        return redirect('list_tasks')
    return render(request, 'tasks/edit.html', {'task': tarea})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect ('list_tasks')

def complete_task(request, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    tarea.terminado = True
    tarea.save()
    return redirect('list_tasks')