from django.db import models
from django.contrib.auth.models import User
from django.conf import Settings

# Create your models here.


class Rooms(models.Model):
    ROOM_CATEGORIES = (
        'FAMILY ROOM',
        'DELUXE ROOM',
        'SUITE ROOM',
    )
    room_image = models.ImageField(upload_to="room_image",default='room_image/default.png',blank=True,null=True)
    hotel_type = models.CharField(max_length=50)
    Adults = models.IntegerField()
    price = models.PositiveBigIntegerField()
    categories = models.CharField(max_length=10)
    size = models.IntegerField(default=20)
    Facilities = models.TextField(max_length=130)
    beds = models.CharField(max_length=15,blank=True,null=True)
    additional_offer = models.CharField(max_length=21,blank=True,null=True) 
    # carousel image dont forget to add


    def __str__(self):
        return self.hotel_type

    class Meta:
        verbose_name_plural = ('Rooms')




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()


    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'








    















    

