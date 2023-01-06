from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.


class Listings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    #image = models.CharField(max_length=100)
    images = ArrayField(models.CharField(max_length=1000), blank=True)
    number_of_persons = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, blank=True)
    map_link = models.CharField(max_length=500, null=True, blank=True)
    property_type = models.CharField(max_length=100, null=True, blank=True)
    slot = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)

    time_to_upsa_walk = models.CharField(max_length=300, null=True, blank=True) 
    time_to_upsa_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_upsa_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_ug_walk = models.CharField(max_length=300, null=True, blank=True) 
    time_to_ug_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_ug_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_radford_walk = models.CharField(max_length=300, null=True, blank=True)
    time_to_radford_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_radford_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_knustford_walk = models.CharField(max_length=300, null=True, blank=True)
    time_to_knustford_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_knustford_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_gsl_walk = models.CharField(max_length=300, null=True, blank=True)
    time_to_gsl_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_gsl_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_lancaster_walk = models.CharField(max_length=300, null=True, blank=True)
    time_to_lancaster_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_lancaster_car = models.CharField(max_length=300, null=True, blank=True)

    time_to_wisconsin_walk = models.CharField(max_length=300, null=True, blank=True)
    time_to_wisconsin_bike = models.CharField(max_length=300, null=True, blank=True)
    time_to_wisconsin_car = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.user.firstName} listing'




class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, null =True)




