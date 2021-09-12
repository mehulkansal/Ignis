from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.models import Post
from django.http import JsonResponse
# Create your views here.


def home(request, *args, **kwargs):
    Posts = Post.objects.all().order_by('time')
    data = {'Posts': Posts}

    if request.user.is_authenticated:
        user = request.user
        liked = Post.objects.filter(likes=user).order_by('time')
        not_liked = Post.objects.exclude(likes=user).order_by('time')
        data['Liked'] = liked
        data['Not_Liked'] = not_liked
    return render(request, 'home.html', data)


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


def like(request, id):
    data = {'status': False}
    try:
        user = request.user
        post = Post.objects.get(id=id)
        post.likes.add(user)
        post.save()
        data['status'] = True
    except Exception as e:
        print(e)
    return JsonResponse(data)


def unlike(request, id):
    data = {'status': False}
    try:
        user = request.user
        post = Post.objects.get(id=id)
        post.likes.remove(user)
        post.save()
        data['status'] = True
    except Exception as e:
        print(e)
    return JsonResponse(data)
