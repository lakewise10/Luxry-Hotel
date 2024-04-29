from django.shortcuts import render,get_object_or_404,HttpResponse, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import FormView,ListView, View
from .forms import AvailabilityForm, CreateUserForm
from luxry.booking_functions.availability import check_availability
from blog.models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# from blog.views import blog


# Create your views here.

def room(request):
    rooms = Rooms.objects.all()
    context = {
        'rooms':rooms,
        # 'blog': blog,
    }
    return render(request, "luxry/home.html",context)



def about (request):
    return render (request, "luxry/about.html")


def gallery (request):
    return render (request, "luxry/gallery.html")



def details(request, id=id):
    rooms = get_object_or_404(Rooms, id=id)
    context = {
        'rooms':rooms,
    }
    return render (request, 'luxry/details.html', context)

    


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'Availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_dataroom
        room_List = Rooms.objects.filter(category = data['room_category'])
        available_rooms = []
        for room in room_List:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
        )   
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of This category of rooms Are Booked ! Try Another One')





class RoomListView(ListView):
    model = Rooms





class BookingList(ListView):
    model = Booking


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
        # room_list = Rooms.objects.filter(category = category)
        context = {
            'room_category': room_category
        }
        return render(request,'luxry/details.html', context)



    # def post(self, request, *args, **kwargs):
    #     room_list = Rooms.objects.filter(category = category)
    #     available_rooms = []
    #     for room in room_List:
    #         if check_availability(room, data['check_in'], data['check_out']):
    #             available_rooms.append(room)

    #     if len(available_rooms) > 0:
    #         room = available_rooms[0]
    #         booking = Booking.objects.create(
    #             user = self.request.user,
    #             room = room,
    #             check_in = data['check_in'],
    #             check_out = data['check_out'],
    #     )   
    #         booking.save()
    #         return HttpResponse(booking)
    #     else:
    #         return HttpResponse('All of This category of rooms Are Booked ! Try Another One')


    #     return render (request, 'room_detail_view.html', context)



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


    context = {'form':form}
    return render(request, 'luxry/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('luxry-room')
        else:
            messages.info(request, "Username or pasword is incorrect")
            
    context = {}
    return render(request, 'luxry/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect ('login')






    












