from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_reviews', views.all_reviews, name='all_reviews'),
    path('all_movies', views.all_movies, name='all_movies'),
    path('add_review', views.add_review, name='add_review')
]