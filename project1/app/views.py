from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def todolist1(request):
    todos=todo.objects.all()
    if request.method=='POST':
        todoarea=request.POST['todoarea']
        data=todo.objects.create(sub=todoarea)
        data.save()
    return render(request,'index.html',{'todods':todos})

def todo_update(request,pk):
    data=todo.objects.get(pk=pk)
    print(data.sub)
    return render(request,'update.html',{'data':data})