from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import EventsForm, PasswordChangingForm, PasswordForm, TodosForm, UserUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Passwords, Todos, Events


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, "user_side/profile.html", context)


@login_required(login_url='login')
def todos(request):
    form = TodosForm
    if request.method == 'POST':
        form = TodosForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        if form.is_valid():
            form.save()
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/todos.html", {
        "todos": todos,
        'form': form
    })


@login_required(login_url='login')
def editTodo(request, pk):
    todo = Todos.objects.get(id=pk)
    form = TodosForm(request.POST)
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if(str(form.data['title']) != "" and str(form.data['description']) != ""):
            todo.title = form.data['title']
            todo.description = form.data['description']
            todo.save()
        return redirect('user-todos')
    return render(request, "user_side/edit_todo.html", {
        "todos": todos,
        'form': form,
        "todo": todo
    })


@login_required(login_url='login')
def todo(request, pk):
    item = Todos.objects.get(id=pk)
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/todo.html", {
        "todo": item,
        "todos": todos,
    })


@login_required(login_url='login')
def events(request):
    form = EventsForm
    if request.method == 'POST':
        form = EventsForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        if form.is_valid():
            form.save()
    events = Events.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/events.html", {
        "events": events,
        'form': form
    })


@login_required(login_url='login')
def passwords(request):
    form = PasswordForm
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        if form.is_valid():
            form.save()
    passwords = Passwords.objects.filter(user=request.user).order_by('-id')
    return render(request, "user_side/password_manager.html", {
        "passwords": passwords,
        'form': form
    })


@login_required(login_url='login')
def viewPassword(request, pk):
    passwords = Passwords.objects.filter(user=request.user).order_by('-id')
    item = Passwords.objects.get(id=pk)
    return render(request, "user_side/password_view.html", {
        "passwords": passwords,
        'password': item
    })


@login_required(login_url='login')
def editPassword(request, pk):
    item = Passwords.objects.get(id=pk)
    form = PasswordForm(request.POST)
    passwords = Passwords.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        print(str(form.data['username']) == "")
        print(str(form.data['password']))
        if(str(form.data['username']) != "" and str(form.data['password']) != ""):
            item.username = form.data['username']
            item.password = form.data['password']
            item.save()
        return redirect('user-passwords')
    return render(request, "user_side/edit_password.html", {
        "passwords": passwords,
        'form': form,
        "password": item
    })


@login_required(login_url='login')
def deleteTodo(request, pk):
    item = Todos.objects.get(id=pk)
    item.delete()
    return redirect("user-todos")


@login_required(login_url='login')
def deletePassword(request, pk):
    item = Passwords.objects.get(id=pk)
    item.delete()
    return redirect("user-passwords")


@login_required(login_url='login')
def deleteEvent(request, pk):
    item = Events.objects.get(id=pk)
    item.delete()
    return redirect("user-events")


# @login_required(login_url='login')


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')
