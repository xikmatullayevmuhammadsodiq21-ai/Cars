from django.urls import path
from . import views

urlpatterns = [
    path('car_detail/', views.car_detail, name='car_detail'),
    path('car_list/', views.car_list, name='car_list'),
    path('delete/', views.delete_car, name='delete'),
    path('edit/', views.edit_car, name='edit'),
    path('home_page/', views.home_page, name='home_page'),
    path('add/', views.add_car, name='add'),
]

