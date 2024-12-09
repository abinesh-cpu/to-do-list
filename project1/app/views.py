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
    return render(request,'index.html',{'todos':todos})

def todo_update(request,pk):
    todos=todo.objects.all()
    if request.method=='POST':
        todoarea=request.POST['todoarea']
        todo.objects.filter(pk=pk).update(sub=todoarea)
        return redirect(todolist1)
    else:
        data=todo.objects.get(pk=pk)
        print(data.sub)
    return render(request,'index.html',{'data':data,'todos':todos})
def todo_delete(request,pk):
    todo.objects.filter(pk=pk).delete()
    return redirect(todolist1)