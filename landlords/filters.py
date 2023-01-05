from . models import *
import django_filters

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listings
        fields = ['gender','location', 'price', 'number_of_persons', 'property_type', 'user']