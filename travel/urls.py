from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-home'),
    path('about/', views.about, name='travel-about'),
    path('travel/', views.travel, name='travel-travel'),
    path('travels/', views.travelform, name='travel-travelform'),
]
