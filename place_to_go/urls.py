from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('random/', views.random_place_view, name='random_place'),
    path('places/', views.place_list, name='place_list'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
    path('add/', views.add_place, name='add_place'),
]