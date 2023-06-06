from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ("War", "War"),
    ("Adventure", "Adventure"),
    ("Documentary", "Documentary"),
    ("Romance", "Romance"),
    ("Animation", "Animation"),
    ("Drama", "Drama"),
    ("Science fiction", "Scence fiction"),
    ("Sports", "Sports"),
    ("Musical", "Musical"),
    ("Thriller", "Thriller"),
    ("Horror", "Horror")

)


class Movie(models.Model):
    title = models.CharField(max_length=300)
    date_released = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    actors = models.ManyToManyField("Actor", related_name ="movies")
    description = models.TextField()
    duration = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    poster = models.ImageField(upload_to="movie_posters/")
    trailer_link = models.URLField()

    def __str__(self):
        return self.title
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default=True)

    def __str__(self):
        return self.name





    