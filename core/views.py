from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def services(request):
    return render(request,"services.html")

def faq(request):
    return render(request,"faq.html")

def contact(request):
    return render(request,"contact.html")