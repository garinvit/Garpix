
from django import forms
from ..models.booking import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'