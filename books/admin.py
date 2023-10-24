from django.contrib import admin

from .models import Books, Genre, Image, Exchange, BookLikes

admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Image)
admin.site.register(Exchange)
admin.site.register(BookLikes)