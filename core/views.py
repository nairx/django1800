from django.shortcuts import render
from core import models

def home(request):
    return render(request,"home.html")

def services(request):
    return render(request,"services.html")

def faq(request):
    return render(request,"faq.html")

def contact(request):
    return render(request,"contact.html")

def todo(request):
    if request.method == "POST":
        task = request.POST.get("task")
        data = models.todo(task=task)
        data.save()
    mytodo = models.todo.objects.all()
    res = {'todos':mytodo}
    return render(request,"todo.html",res)

def deleteTodo(request):
    if request.method == "GET":
        todoId = int(request.GET.get("id"))
        models.todo.objects.filter(id=todoId).delete()
    return todo(request)
    