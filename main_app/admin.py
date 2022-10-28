from django.contrib import admin
from .models import Bike, Ride, Route, Nutrition, NutritionPlan

# Register your models here.
admin.site.register(Bike)
admin.site.register(Ride)
admin.site.register(Route)
admin.site.register(Nutrition)
admin.site.register(NutritionPlan)