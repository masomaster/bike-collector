from django.forms import ModelForm
from .models import Ride, Route, Nutrition

class RideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['title', 'date', 'route']

class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = ['name', 'calories', 'type']