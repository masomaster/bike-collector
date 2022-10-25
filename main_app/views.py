from ast import Del
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Bike, Ride, Route
from .forms import RideForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/index.html', {'bikes': bikes})

def bikes_detail(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    ride_form = RideForm()
    return render(request, 'bikes/detail.html', {'bike': bike, 'ride_form': ride_form})

def add_ride(request, bike_id):
    form = RideForm(request.POST)
    if form.is_valid():
        new_ride = form.save(commit=False)
        new_ride.bike_id = bike_id
        new_ride.save()
    return redirect('detail', bike_id=bike_id)

class BikeCreate(CreateView):
    model = Bike
    fields = '__all__'

class BikeUpdate(UpdateView):
    model = Bike
    fields = '__all__'

class BikeDelete(DeleteView):
    model = Bike
    success_url = '/bikes/'

class RideCreate(CreateView):
    model = Ride
    fields = ['title', 'date', 'type']