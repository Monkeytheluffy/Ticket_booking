from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Booking, User
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'departure', 'destination', 'travel_date']


    def clean_travel_date(self):
        travel_date = self.cleaned_data.get('travel_date')
        if travel_date < timezone.now().date():
            raise forms.ValidationError("The travel date cannot be in the past.")
        return travel_date
    



