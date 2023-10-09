from django.urls import path
from todoList import views

urlpatterns = [   
    path('', views.index, name='index'),
    path('todo_create', views.todo_create, name='todo_create'),
    path('todo_update', views.todo_update, name='todo_update'),
    path('todo_check', views.todo_check, name='todo_check'),
    path('todo_delete', views.todo_delete, name='todo_delete'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]