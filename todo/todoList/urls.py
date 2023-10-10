from django.urls import path
from todoList import views

urlpatterns = [   
    #home page url
    path('', views.index, name='index'),

    #Create Update Delete todos
    path('todo_create', views.todo_create, name='todo_create'),
    path('todo_update', views.todo_update, name='todo_update'),
    path('todo_delete', views.todo_delete, name='todo_delete'),

    #to add chekbox to amke a todo completed
    path('todo_check', views.todo_check, name='todo_check'),

    #sign up sign in and logout functionality
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]