from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import todoCharts
from django.db.models import Q
from django.utils import timezone

# Create your views here.\

#index page
@login_required(login_url='signin')
def index(request):
    current_datetime = timezone.now()
    todos = todoCharts.objects.filter(user=request.user)

    pendingtodos = todos.filter(Q(completed=False) & Q(due_date__gt=current_datetime))
    checkedtods = todos.filter(completed=True)
    expiredtodos = todos.filter(due_date__lt=current_datetime)
    return render(request, 'index.html', {
        'todos': todos,
        'pendingtodos':pendingtodos,
        'checkedtods':checkedtods,
        'expiredtodos':expiredtodos,
        'username': request.user.username,
        })

#to create a todos list
@login_required(login_url='signin')
def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        todo = todoCharts.objects.create(user=request.user, title=title, description=description, due_date=due_date)
        todo.save()
        return redirect('/')
    
#feture to make a todo completed
@login_required(login_url='signin')
def todo_check(request):
    todo_id = request.POST['todo_id']
    todo = todoCharts.objects.get(id=todo_id)

    completed = request.POST.get('completed', 'off')
    completed = completed == 'on'
    todo.completed = completed
    todo.save()
    return redirect('/')

#to uodate the todo list
@login_required(login_url='signin')
def todo_update(request):    
    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        todo = todoCharts.objects.get(id=todo_id)

        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        if due_date:
            todo.due_date = due_date

        completed = request.POST.get('completed', 'off')
        completed = completed == 'on'

        todo.description=description
        todo.completed = completed
        todo.title=title
        todo.save()
        return redirect('/')
#to delete the todo
@login_required(login_url='signin')
def todo_delete(request):
    if request.method == 'POST':
        id = request.POST['todo_id']
        todo = todoCharts.objects.get(id=id)
        todo.delete()
        return redirect('/')

#logout functionality
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin') 

# to create a new user
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 :
            if User.objects.filter(email = email).exists():
                messages.info(request, 'E mail already exist')
                return render(request, 'signup.html')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exist')
                return render(request, 'signup.html')
            else :
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save()
                return redirect('/')
        else :
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else :
        return render(request, 'signup.html')
    
#login feature
def signin(request):
    if request.method == 'POST' :
        usernameU = request.POST.get('username')
        passwordP = request.POST.get('password')

        user = auth.authenticate(username=usernameU, password=passwordP)

        if user is not None :
            auth.login(request, user)
            return redirect('/') 
        else :
            messages.info(request, 'Username or Password is unmatching')
            return redirect('signin') 
    else :
        return render(request, 'signin.html')