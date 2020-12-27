from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(primary_key = True, max_length=100)
    movieimg=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.moviename + ":" + str(self.movieimg)
    def image_url(self):
        if self.movieimg and hasattr(self.movieimg, 'url'):
            return self.movieimg.url