from django.shortcuts import render
from django.http import HttpResponse

class Bike:
    def __init__(self, brand, model, year, type, nickname, description):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type
        self.nickname = nickname
        self.description = description

bikes = [
    Bike('Bontrager', 'Race Lite', 1997, 'Cross-country mountain', 'Bob', 'loves singletrack'),
    Bike('Eddy Merckx', 'Mourenx 69', 'Endurance road', 2016, 'Eddy', 'excels at everything'),
    Bike('Guardian', 'Ethos', 2021, 'Kids', '', 'great first bike for kids!'),
]

def home(request):
    return HttpResponse('<h1>Welcome to the Bike Collector!</h1>')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
    return render(request, 'bikes/index.html', {'bikes': bikes})