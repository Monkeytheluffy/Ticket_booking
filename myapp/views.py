from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pymongo import MongoClient
from .forms import RegisterForm, SignInForm, TicketBookingForm
from .models import Booking
from django.utils import timezone
from .mongodb import bookings_collection


client = MongoClient('mongodb://localhost:27017/')
db = client['ticket_booking_db']
users_collection = db['users']

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')  # Assuming a form field named 'password1'
            
            # Store user details in MongoDB
            user_data = {
                'username': username,
                'email': email,
                'password': password  # Note: It's recommended to hash the password before storing
            }
            
            # Insert user data into MongoDB collection
            users_collection.insert_one(user_data)
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = SignInForm()
    return render(request, 'myapp/signin.html', {'form': form})


from datetime import datetime

def ticket_booking(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            booking_data = {
                "name": form.cleaned_data['name'],
                "departure": form.cleaned_data['departure'],
                "destination": form.cleaned_data['destination'],
                "travel_date": datetime.combine(form.cleaned_data['travel_date'], datetime.min.time()),
                "email": form.cleaned_data['email'],
                "phone": form.cleaned_data['phone'],
            }
           
            bookings_collection.insert_one(booking_data)
            messages.success(request, "Your ticket has been booked successfully!")
            return redirect('home')
    else:
        form = TicketBookingForm()

    return render(request, 'myapp/ticket_booking.html', {'form': form})


def home(request):
    bookings = Booking.objects.all()
    return render(request, 'myapp/home.html', {'bookings': bookings})


