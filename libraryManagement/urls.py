
from django.contrib import admin
from django.urls import path, include
from .views import api_root_view

urlpatterns = [
    path('',api_root_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include("api.urls"), name='api-root')
]
