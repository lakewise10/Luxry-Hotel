from django.shortcuts import render
from .models import Blog
from django.shortcuts import redirect


# Create your views here.


def blog(request):
    blog = Blog.objects.all()
    blog = "blog"
    return redirect("luxry/home.html", blog=blog)



