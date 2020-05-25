from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks=Task.objects.all()
    context ={'tasks' : tasks }
    return render(request, 'tasks/list.html', context)

def addTask(request):
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        form.shifts=request.POST['shifts']
        form.status=request.POST['status']
        if form.is_valid():
            form.save()
        return redirect('/')

    context ={'form':form }
    return render(request, 'tasks/add.html', context)

def updateTask(request, pk):
    task=Task.objects.get(id=pk)

    form=TaskForm(instance=task)
    if request.method == 'POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context={'form': form}

    return render(request, 'tasks/update_tasks.html', context)


def deleteTask(request, pk):
    item=Task.objects.get(id=pk)
    context={'item': item}

    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', context)

