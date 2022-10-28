from django.db import models
from django.urls import reverse

RIDE_TYPES = (
    ('R', 'Road'),
    ('M', 'Mountain')
)

NUTRITION_TYPES = (
    ('W', 'Water'),
    ('G', 'Gel'),
    ('B', 'Bar'),
    ('C', 'Chews'),
    ('S', 'Sports drink'),
)

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    type = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})

class Route(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    distance = models.IntegerField('distance (miles)')
    altitude = models.IntegerField('altitude gain')
    rwgps_url = models.CharField('Ride with GPS link', max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('route_detail', kwargs={'pk': self.id})

class Nutrition(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField('Calories per serving/bottle')
    type = models.CharField(
        max_length=1,
        choices=NUTRITION_TYPES,
        default=NUTRITION_TYPES[0][0]
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Ride(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=RIDE_TYPES,
        default=RIDE_TYPES[0][0]
    )
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.date}"

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('ride_detail', kwargs={'ride_id': self.id})

class NutritionPlan(models.Model):
    time = models.CharField(max_length=50)
    nutrition = models.ManyToManyField(Nutrition)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nutrition at {self.time} on {self.ride}"
