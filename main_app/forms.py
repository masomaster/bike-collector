from django.forms import ModelForm
from .models import NutritionPlan, Ride, Route, Nutrition

class RideForm(ModelForm):
    class Meta:
        model = Ride
        fields = ['title', 'date', 'route']

class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = ['name', 'carbs', 'type']

class NutritionPlanForm(ModelForm):
    class Meta:
        model = NutritionPlan
        fields = ['time', 'nutrition']