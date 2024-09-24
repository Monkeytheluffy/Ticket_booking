from django.urls import path
from .views import home, register, signin, ticket_booking

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('ticket_booking/', ticket_booking, name='ticket_booking'),
]
