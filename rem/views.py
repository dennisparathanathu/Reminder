from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . forms import reminder_form
from .models import Reminder


# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashbord')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def dashbord(request):
    remin=Reminder.objects.filter(user=request.user)


    return render(request, 'dash.html', {'rem': remin})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
def add_reminder(request):
    if request.method== 'POST':
        form = reminder_form(request.POST)
        if form.is_valid():
            rem=form.save(commit=False)
            rem.user=request.user
            rem.save()
            return redirect('dashbord')

    else:
        form=reminder_form()
    return render(request, 'addreminder.html', {'form': form})
def edit_reminder(request, pk):

    post= get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form= reminder_form(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('dashbord')
    else:
        form=reminder_form(instance=post)
    return render(request, 'addreminder.html', {'form': form})
def delete_reminder(request, pk):
    try:
        reminder=Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return redirect('dashbord')
    reminder.delete()
    return redirect('dashbord')




