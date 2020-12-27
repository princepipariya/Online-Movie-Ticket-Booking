from django.db import models

# Create your models here.
class Seat(models.Model):
    # class Meta:
    #     unique_together = ('moviename','date','row','column','time')
    username=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    date=models.IntegerField()
    row=models.CharField(max_length=10)
    column=models.CharField(max_length=10)
    time=models.IntegerField()
    