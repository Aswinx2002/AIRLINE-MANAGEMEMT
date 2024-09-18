from .forms import FlightAddForm,FlightEditForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight

# Create your views here.
def home(request):
    return render(request,'Home.html')

def flight_list(request):
    search_performed = False
    flights = []

    if 'flight_id' in request.GET or 'departure_date' in request.GET or 'departure_airport_name' in request.GET:
        search_performed = True
        flight_id = request.GET.get('flight_id', '')
        departure_date = request.GET.get('departure_date', '')
        departure_airport_name = request.GET.get('departure_airport_name', '')

        flights = Flight.objects.filter(
            flight_id__icontains=flight_id,
            departure_date__icontains=departure_date,
            departure_airport_name__icontains=departure_airport_name
        )

    return render(request, 'search_flight.html', {
        'flights': flights,
        'search_performed': search_performed
    })


def flight_detail(request,passed_flight_id):
    flight_details = get_object_or_404(Flight,flight_id=passed_flight_id)
    print(flight_details)
    return render(request,'flightdetails.html',{'flight_details':flight_details})


def add_flight(request):
    add_flight_form=FlightAddForm(request.POST,request.FILES)
    if request.method=='POST':
        if add_flight_form.is_valid():
            new_flight=add_flight_form.save(commit=False)
            print(new_flight)
            new_flight.save()
            return redirect('home')
        else:
            add_flight_form=FlightAddForm()
    return render(request,'account/add_flight.html',{'add_flight_form':add_flight_form})

def delete_flight(request, passed_flight_id):
    # get the post (single object) with id value in the table as passed_id received from url
    flight_details = get_object_or_404(Flight, flight_id=passed_flight_id)
    flight_details.delete()
    return redirect('home')









def edit_flight(request, passed_flight_id):
    flight_details = get_object_or_404(Flight, flight_id=passed_flight_id)
    edit_flight_form = FlightEditForm(request.POST or None, request.FILES or None, instance=flight_details)
    if edit_flight_form.is_valid():
        edit_flight_form.save()
        return redirect('home')
    return render(request, 'account/edit_flight.html', {'edit_flight_form': edit_flight_form})

def all_flights(request):
    flights = Flight.objects.all()  # Retrieve all flights
    return render(request, 'all_flights.html', {'flights': flights})
