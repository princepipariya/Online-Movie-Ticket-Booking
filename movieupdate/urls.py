from django.urls import path
from django.conf.urls import url
from .views import add_view,homesuper_view,delete_view
#from .view import 

urlpatterns=[
    url('addmovie/',add_view),
    url('homesuper/',homesuper_view),
    url('deletemovie/',delete_view)
]