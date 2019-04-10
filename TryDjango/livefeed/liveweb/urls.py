from django.urls import path

from . import views

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'live/', views.livefe, name='live')
]
