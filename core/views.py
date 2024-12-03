from django.shortcuts import render,redirect
from core import models
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

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

def logout_view(request):
    logout(request)
    return home(request)

def signup(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'signup.html',context)