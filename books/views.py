from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from books.utils.timeago import time_since
from .models import  BookLikes, Books, Exchange
from .serializers import BookSerializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views import generic
from .forms import SearchForm
  
from search_views.search import SearchListView
from search_views.filters import BaseFilter

class AllBooks(generics.ListAPIView):
    queryset =  Books.objects.all()

    serializer_class = BookSerializers


class BookMain(View):
    
    def get(self, request):
        # Exchange modelida mavjud bo'lgan kitoblar ro'yxatini yaratamiz
        exchanged_books = Exchange.objects.values_list('book', flat=True) 
        # Ushbu ro'yxatda bo'lmagan kitoblarni tanlaymiz
        last_exchange_books = Books.objects.exclude(id__in=exchanged_books).order_by('-created_time')[:3]
        
        context = { 'last_books': last_exchange_books, "exchanged_books": exchanged_books}
        return render(request, 'main.html', context)
  

class BookChange(LoginRequiredMixin, generic.ListView):
    template_name = 'books/index.html'
    queryset = Books.objects.all()
  
class BookSearchFilter(BaseFilter):
    search_fields = {
        'search_text' : ['name','author'  ],
    }
    

class BookSearch(SearchListView):
    model = Books
    paginate_by = 30
    template_name = "books/search.html"
    form_class = SearchForm
    filter_class = BookSearchFilter


class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['likes_count'] = BookLikes.objects.filter(book=book).count()
        return context
    
class BookExchange(View):
    
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        
        return render(request, 'exchange/index.html', {"book":book})


class AddBook(View):
    
    def get(self, request):
        return render(request, 'books/add.html')
        