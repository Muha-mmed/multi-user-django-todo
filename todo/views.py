from django.shortcuts import render, redirect
from .models import Todo
from .form import SignUpForm,LoginForm,EditProfileForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')  
def index(request):
    todo = Todo.objects.filter(user=request.user).order_by("-created_at")
    if request.method == 'POST':
        todo = Todo(
            title = request.POST['title'],
            user = request.user
        )
        todo.save()
        return redirect('/')
    return render(request,'index.html', {'todos': todo} )


@login_required(login_url='login')  
def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

@login_required(login_url='login')  
def update(request,todo_id):
    if request.method == 'POST':
        newTitle = request.POST['title']
        todo = Todo.objects.get(id=todo_id)
        todo.title = newTitle
        todo.save()
        return redirect(index)
    elif request.method == 'GET':
        todo = Todo.objects.get(id=todo_id)
        return render(request,'update.html',{'todo': todo})
    
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()        
    return render(request,'signup.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password= password)
            if user is not None:
                login(request,user)
                return redirect('index',permanent=True)
    else:
        form = LoginForm()
    return render(request,'login.html',{'form': form})

from django.contrib.auth import logout

@login_required(login_url='login')  
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'you have been logged out successfully.')
        return redirect('/login')
    return redirect('index')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('login')  # Or home page if you prefer
    else:
        return redirect('index')  # Prevent GET access
