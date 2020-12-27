from django.contrib import admin
from movieupdate.models import Movie
from booking.models import Seat
# Register your models here.
admin.site.register(Movie)
admin.site.register(Seat)