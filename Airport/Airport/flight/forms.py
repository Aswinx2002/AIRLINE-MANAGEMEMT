from django import forms
from .models import Flight

class FlightAddForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('flight_id', 'departure_airport_name', 'departure_date', 'departure_time',
                  'arrival_airport_name', 'arrival_date', 'arrival_time', 'flight_image')

class FlightEditForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('flight_id', 'departure_airport_name', 'departure_date', 'departure_time',
                  'arrival_airport_name', 'arrival_date', 'arrival_time', 'flight_image')

