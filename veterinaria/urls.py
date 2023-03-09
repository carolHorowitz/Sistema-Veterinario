
from django.contrib import admin
from django.urls import include, path
from django import views

urlpatterns = [
    path('', include('sistema.urls')),
    path('admin/', admin.site.urls),     
]
