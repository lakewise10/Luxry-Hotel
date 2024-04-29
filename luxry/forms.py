from django import forms
from .models import Booking,Rooms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class AvailabilityForm(forms.Form):
    # ROOM_CATEGORIES = (
    #     ('FR','FAMILY ROOM'),
    #     ('DR','DELUXE ROOM'),
    #     ('SR','SUITE ROOM'),

    # )
    # room_category = forms.ChoiceField(choices= ROOM_CATEGORIES,required=True)
    check_in = forms.DateTimeField(required=True ,input_formats = ["%Y-%m-dT%H:%M"])
    check_out = forms.DateTimeField(required=True,input_formats = ["%Y-%m-dT%H:%M"])

    # class Meta:
    #     model = Booking
    #     fields = ('__all__')


    #     labels={
    #         'name':'',  
    #         'address':'',
    #         'description':'',
    #         'capacity':'',
    #     }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
