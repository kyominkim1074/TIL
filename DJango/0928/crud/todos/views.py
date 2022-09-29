from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    context = {
        "todos": todo,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todos:index")


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        "todos": todo,
    }
    return render(request, "todos/edit.html", context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    completed = request.GET.get("completed")

    todo.completed = completed
    todo.save()
    return redirect("todos:index")


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todos:index")
