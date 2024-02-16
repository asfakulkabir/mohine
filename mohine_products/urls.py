
from django.contrib import admin
from django.urls import path, include
from .views import index, about, signup, signin, logout_view, dashboard, view_product, place_order, thank

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('dashboard', dashboard, name='dashboard'),
    path('signup', signup, name='signup'),
    path('login', signin, name='login'),
    path('logout', logout_view, name='logout'),
    path('view_product/<str:id>', view_product, name='view_product'),
    path('place_order', place_order, name='place_order'),
    path('thank', thank, name='thank'),
]
