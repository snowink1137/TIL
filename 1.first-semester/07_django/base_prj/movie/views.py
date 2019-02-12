from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm, MovieModelForm
from django.contrib.auth.decorators import login_required


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie/list.html', context)


# def create(request):
#     if request.method == "POST":
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             title_eng = form.cleaned_data.get('title_en')
#             audience = form.cleaned_data.get('audience')
#             open_date = form.cleaned_data.get('open_date')
#             genre = form.cleaned_data.get('genre')
#             watch_grade = form.cleaned_data.get('watch_grade')
#             score = form.cleaned_data.get('score')
#             poster_url = form.cleaned_data.get('poster_url')
#             description = form.cleaned_data.get('description')
#
#             Movie.objects.create(
#                 title=title,
#                 title_eng=title_eng,
#                 audience=audience,
#                 open_date=open_date,
#                 genre=genre,
#                 watch_grade=watch_grade,
#                 score=score,
#                 poster_url=poster_url,
#                 description=description,
#             )
#             return redirect('movie:create')
#     else:
#         form = MovieForm()
#         context = {
#             'form': form,
#         }
#
#     return render(request, 'movie/create.html', context)

@login_required(login_url='/accounts/signin/')
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:list')

    else:
        form = MovieModelForm()

    context = {
        'form': form,
    }
    return render(request, 'movie/create.html', context)


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', id)
    else:
        form = MovieModelForm(instance=movie)

    context = {
        'form': form,
    }
    return render(request, 'movie/update.html', context)
