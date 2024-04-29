from django.contrib import admin
from .models import Rooms, Booking



# Register your models here.

@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    fields = ('hotel_type','Adults', 'price', 'categories', 'size','Facilities','room_image','additional_offer','beds')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = ('user','room','check_in','check_out')



