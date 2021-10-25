from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect


def home(request):
    # return HttpResponse("Home")
    return render(request, 'todo/home.html')


def todo(request):
    # return HttpResponse("To do list")
    all_todo = Todo.objects.all()
    return render(request, 'todo/todo.html', {'all_todo': all_todo})


def todoDetail(request, id):
    single_todo = Todo.objects.get(id=id)
    return render(request, 'todo/todo-detail.html', {'single_todo': single_todo})


def addTodo(request):
    new_item = Todo(title=request.POST['title'], description=request.POST['description'], priority=request.POST['priority'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, id):
    delete_item = Todo.objects.get(id=id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')
