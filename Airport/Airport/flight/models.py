from django.db import models
# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(max_length=100, primary_key=True)  # Custom ID field
    departure_airport_name = models.CharField(max_length=255)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_airport_name = models.CharField(max_length=255)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    flight_image = models.ImageField(upload_to='flight/images/')

    def __str__(self):
        return self.flight_id
