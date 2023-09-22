from django.contrib import admin

from .models import Books, Genre, Image

admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Image)