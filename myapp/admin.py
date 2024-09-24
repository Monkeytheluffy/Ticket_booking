from django.contrib import admin
from .models import Booking, User

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('departure', 'destination', 'travel_date', 'name', 'email', 'phone', 'created_at')
    list_filter = ('departure', 'destination', 'travel_date')
    search_fields = ('name', 'email', 'departure', 'destination')


admin.site.register(User)