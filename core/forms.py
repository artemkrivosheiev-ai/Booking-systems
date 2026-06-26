from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'room': forms.Select(attrs={'class': 'form-input'}),
        }
