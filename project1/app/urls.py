from django.urls import path
from . import views

urlpatterns=[
    path('',views.todolist1),
    path('todo_update/<pk>',views.todo_update),
    path('todo_delete/<pk>',views.todo_delete),
]