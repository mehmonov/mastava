from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.LoginUser.as_view(), name='loginuser'),
    path('profile/', views.Profile.as_view(), name='profileuser'),
]
