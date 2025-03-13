from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDo
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'home.html')

@login_required(login_url = 'loginuser')
def index(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        description = request.POST.get('description')
        datetime = request.POST.get('datetime')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        task = ToDo(user = request.user,title=title, description=description, datetime=datetime, priority=priority, status=status)
        task.save()
        return redirect('index')
    return render(request, 'index.html', {'task' : ToDo.objects.filter(user = request.user),'name':request.user.username})

@login_required(login_url = 'loginuser')
def edit(request, edit_id):
    edit = get_object_or_404(ToDo,pk = edit_id,user = request.user)
    if request.method == 'POST':
        edit.title = request.POST.get('task')
        edit.description = request.POST.get('description')
        edit.datetime = request.POST.get('datetime')
        edit.priority = request.POST.get('priority')
        edit.status = request.POST.get('status')
        edit.save()
        return redirect('index')
    return render(request, 'edit.html', {'edit' : edit})

@login_required(login_url = 'loginuser')
def delete(request, delete_id):
    task = get_object_or_404(ToDo,pk = delete_id, user = request.user)
    task.delete()
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Automatically log in the user after registration
        return redirect('index')  # Redirect to the homepage or wherever you want

    return render(request, 'register.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username.lower(), password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('index')



























# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from web.models import UserRegister
# from django.db import IntegrityError
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt, csrf_protect

# # Create your views here.
# @login_required(login_url = 'register')
# def index(request):
#     return render(request, 'index.html')

# @csrf_protect
# def register(request):
#     if request.method == "POST":
#         fullname = request.POST.get('fullname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confpass = request.POST.get('confpass')
#         if not fullname or not email or not password or not confpass:
#             return render(request, 'register.html', {'message' : 'Enter All the Details'})
#         if confpass != password:
#             return render(request, 'register.html', {'message' : 'Password Not Matching'})
#         try:
#             user = UserRegister(fullname = fullname, email = email,username=email, password = password)
#             user.save()
#             return redirect('loginuser')
#         except IntegrityError:
#             return render(request, 'register.html', {'message' : 'Email Already Used'})
#     return render(request, 'register.html',{'message' : ''})

# def loginuser(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(Username=email, Password=password)
#         if user is not None:
#             login(request, User)
#             return redirect('index')
#         else:
#             return render(request, 'login.html', {'message': 'Invalid Email & Password'})

#     return render(request, 'login.html')