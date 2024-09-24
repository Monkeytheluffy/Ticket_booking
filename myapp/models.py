from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myapp_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myapp_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
class Booking(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.departure} to {self.destination} on {self.travel_date}'
  

