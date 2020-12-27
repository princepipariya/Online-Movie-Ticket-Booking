from django.urls import path
from django.conf.urls import url
from .views import booknow_view,timecheck_view,seat_view,show_ticket_view

urlpatterns=[
    url('booknow/',booknow_view),
    url('timecheck/',timecheck_view),
    url('seat/',seat_view),
    url('show_ticket/',show_ticket_view)
]


