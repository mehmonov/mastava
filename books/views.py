from django.shortcuts import render
from rest_framework import generics
from .models import  Books
from .serializers import BookSerializers
class AllBooks(generics.ListAPIView):
    queryset =  Books.objects.all()

    serializer_class = BookSerializers

    