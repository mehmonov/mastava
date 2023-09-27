
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Mastava-Server API",
      default_version='v1',
      description="Kitoblar ro'yhati va boshqa narsalar uchun dokumentatsiya",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('dj_rest_auth.urls')), # login, logout, 
    path('book/', include('books.urls')), # book so'zidan keyin kitoblarga oid sozlamalar bor 
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
