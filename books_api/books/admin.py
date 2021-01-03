from django.contrib import admin

# Register your models here.
from .models import Book

admin.site.register(Book)  # don't forget to register to the admin 
