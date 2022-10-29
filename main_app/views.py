from ast import Del
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Bike, Ride, Route, Nutrition
from .forms import NutritionPlanForm, RideForm, NutritionForm

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
    route = Route.objects.get(id=ride.route.id)
    bike = Bike.objects.get(id=ride.bike.id)
    nutrition = Nutrition.objects.all()
    nutrition_form = NutritionForm()
    nutrition_plan_form = NutritionPlanForm()
    
    def total_carbs(ride):
        total = 0
        for plan in ride.nutritionplan_set.all():
            for nutrient in plan.nutrition.all():
                total += nutrient.carbs
        return total
    
    total_carbs = total_carbs(ride)
    carbs_per_hr = round((total_carbs / ride.est_time), 1)
    context = {
        'ride': ride, 
        'route': route, 
        'bike': bike, 
        'nutrition_form': nutrition_form, 
        'nutrition_plan_form': nutrition_plan_form,
        'nutrition': nutrition,
        'total_carbs': total_carbs,
        'carbs_per_hr': carbs_per_hr,
    }
    return render(request, 'rides/detail.html', context)

class RideUpdate(UpdateView):
    model = Ride
    fields = '__all__'

class RideDelete(DeleteView):
    model = Ride
    success_url = '/rides/'

def add_nutrition_plan(request, ride_id):
    form = NutritionPlanForm(request.POST)
    nutrient_list = request.POST.getlist('nutrition')
    if form.is_valid():
        new_np = form.save(commit=False)
        new_np.ride_id = ride_id
        new_np.save()
        for nutrient in nutrient_list:
            new_np.nutrition.add(nutrient)
    return redirect('ride_detail', ride_id=ride_id)

def create_nutrition(request, ride_id):
    print("we got to views!")
    form = NutritionForm(request.POST)
    if form.is_valid():
        new_nutrient = form.save(commit=False)
        new_nutrient.save()
    return redirect('ride_detail', ride_id=ride_id)
