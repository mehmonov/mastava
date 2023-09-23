
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('dj_rest_auth.urls')), # login, logout, 
    path('book/', include('books.urls')), # book so'zidan keyin kitoblarga oid sozlamalar bor 

]
