from django.urls import path
from . import views
from.views import RoomListView, BookingView,BookingList, BookingView, RoomDetailView


# app_name = 'luxry'


urlpatterns = [
    path('',views.room, name='luxry-room'),
    path('<int:id>/',views.details, name='luxry-details'),
    path('about/',views.about, name='luxry-about'),
    path('gallery/',views.gallery, name='luxry-gallery'),
    path('room_list/', RoomListView.as_view(), name='RoomListView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('login/', views.logoutUser, name='logout'),
]




