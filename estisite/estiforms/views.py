from django.shortcuts import render
from django.http import HttpResponse
from .models import Review, Movie
from .forms import ReviewForm

def index(request):
    return HttpResponse("hello world, this is index")


def all_reviews(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'estiforms/all_reviews.html', context)


def all_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'estiforms/all_movies.html', context)

def add_review(request):
    context = {'form': ReviewForm}
    return render(request, 'estiforms/add_review_form.html', context)
