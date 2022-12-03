
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


# Create your views here.
def product(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'home.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    return render(request, 'details.html', {'movie_key': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('movie')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        director = request.POST.get('director')
        img = request.FILES['img']
        movie = Movie(movie=name, year=year, desc=desc, director=director, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['password1']

        if password == c_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('/register')

            else:
                user = User.objects.create_user(username=user_name, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.info(request, 'User Created')
        else:
            messages.info(request, 'password not matched')
            return redirect('/register')

        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'User Not Found')
            return redirect('/login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
