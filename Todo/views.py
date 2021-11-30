from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    task_list = Task.objects.all()
    context = {'tasks': task_list, 'form': form}
    return render(request, "Todo/index.html", context)


def completed_task(request, id):
    task_item = Task.objects.get(id=id)
    task_item.completed = True
    task_item.save()
    return redirect("index")


def delete_task(request, id):

    task_item = Task.objects.get(id=id)

    if request.method == 'POST':
        task_item.delete()
        return redirect('index')

    return render(request, 'Todo/delete.html', {'task_item': task_item})


def update_task(request, id):
    task_item = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task_item)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'Todo/update.html', {'form': form})