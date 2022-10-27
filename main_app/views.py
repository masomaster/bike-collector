from ast import Del
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Bike, Ride, Route, Nutrition
from .forms import RideForm, NutritionForm

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

class RouteCreate(CreateView):
    model = Route
    fields = '__all__'

class RouteList(ListView):
    model = Route
    fields = '__all__'

class RouteDetail(DetailView):
    model = Route
    fields = '__all__'

class RouteUpdate(UpdateView):
    model = Route
    fields = '__all__'

class RouteDelete(DeleteView):
    model = Route
    success_url = '/routes/'

class RideCreate(CreateView):
    model = Ride
    fields = '__all__'

class RideList(ListView):
    model = Ride
    fields = ['title', 'date']

class RideDetail(DetailView):
    model = Ride
    fields = '__all__'

def ride_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    nutrition = Nutrition.objects.all()
    route = Route.objects.get(id=ride.route.id)
    bike = Bike.objects.get(id=ride.bike.id)
    nutrition_form = NutritionForm()
    return render(request, 'rides/detail.html', {'ride': ride, 'nutrition': nutrition, 'route': route, 'bike': bike, 'nutrition_form': nutrition_form})

class RideUpdate(UpdateView):
    model = Ride
    fields = '__all__'

class RideDelete(DeleteView):
    model = Ride
    success_url = '/rides/'