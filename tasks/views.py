from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


# Create your views here.


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('index')

    return render(request, 'tasks/update.html', {'form': form})


def update_task(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'tasks/update.html', {'form': form})


def delete_task(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        task.delete()

        return redirect('index')

    return render(request, 'tasks/delete.html', {'task': task})


def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.complete = True
    todo.save()

    return redirect('index')
