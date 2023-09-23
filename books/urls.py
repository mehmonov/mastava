from django.urls import path
from . import views
urlpatterns = [
    path('',views.AllBooks.as_view())
]
