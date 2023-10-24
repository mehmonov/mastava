from django.urls import path, include
from . import views
urlpatterns = [
    # template views
    path('',include('books.utils.urls')),
    # Api urls
    path('api',views.AllBooks.as_view())
]
