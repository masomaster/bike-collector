from django.db import models
from django.urls import reverse

RIDE_TYPES = (
    ('R', 'Road'),
    ('M', 'Mountain')
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

class Ride(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=RIDE_TYPES,
        default=RIDE_TYPES[0][0]
    )

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.date}"

    class Meta:
        ordering = ['date']