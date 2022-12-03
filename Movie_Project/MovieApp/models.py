from django.db import models


# Create your models here.
class Movie(models.Model):
    movie = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    director = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.movie

