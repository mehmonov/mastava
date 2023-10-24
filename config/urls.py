
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

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
    path('user/',include('users.urls')),
    
    path('api-auth/', include('dj_rest_auth.urls')), # login, logout, 
    path('info/',TemplateView.as_view(template_name='info.html'), name='info'),
    path('', include('books.urls')), # book so'zidan keyin kitoblarga oid sozlamalar bor 
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)