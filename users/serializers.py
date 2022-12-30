from email.policy import default
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from . models import *

from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=100)
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=100, default="")
    school = serializers.CharField(max_length=100, default="")
    level = serializers.CharField(max_length=100, default="")
    
    is_landlord = serializers.BooleanField(default=False)

    #LANDLORDS DETAILS
    location = serializers.CharField(max_length=100, default="")

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['phone_number'] = self.validated_data.get('phone_number', '')
        data_dict['firstName'] = self.validated_data.get('firstName', '')
        data_dict['lastName'] = self.validated_data.get('lastName', '')
        data_dict['gender'] = self.validated_data.get('gender', '')
        data_dict['school'] = self.validated_data.get('school', '')
        data_dict['level'] = self.validated_data.get('level', '')
        
        data_dict['is_landlord'] = self.validated_data.get('is_landlord', '')
        
        #LANDLORDS DETAILS
        data_dict['location'] = self.validated_data.get('location', '')

        return data_dict


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('phone_number', 'firstName', 'lastName', 'gender', 'school',  'level', 'is_landlord','location', )



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

