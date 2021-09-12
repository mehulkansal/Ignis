from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.models import Post
# Create your views here.


def home(request, *args, **kwargs):
    objects = Post.objects.all()
    print(objects, "mehul...................")
    return render(request, 'home.html', {'objects': objects})


def signup(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect("home")
        else:
            newuser = User.objects.create_user(
                username=username, email=email, password=password)
            return redirect("home")
    else:
        return redirect("home")


def signin(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return redirect("home")


def logout1(request):
    logout(request)
    return redirect("home")


def add(request):
    if request.method == "POST":
        name = request.user
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        date = request.POST['date']
        image = request.FILES['image']

        new_post = Post.objects.create(
            Name=name, title=title, description=description, location=location, time=date, image=image)
        new_post.save()

    return redirect('home')
