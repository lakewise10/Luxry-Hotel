from django.contrib import admin
from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('blog_image','blog_creation_date','blog_title','blog_text')
