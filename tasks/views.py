from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    task_list = Task.objects.order_by('id')

    form = TaskForm

    context = {'task_list': task_list, 'form': form}
    return render(request, 'base.html', context)


@require_POST
def create_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(text=request.POST['text'])
        new_task.save()

    return redirect('index')


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.complete = True
    task.save()

    return redirect('index')


def delete_task(request):
    Task.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Task.objects.all().delete()