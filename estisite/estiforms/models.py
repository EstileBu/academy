import uuid

from django.db import models
from django.contrib.auth.models import User

RATING_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Movie(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=128)
    published = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.name



class Review(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,  default=None)

    def __str__(self):
        return f"{self.movie} review"



from django.db import models

# Create your models here.
