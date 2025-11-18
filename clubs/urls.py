from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_club, name='add_club'),
    path('', views.club_list, name='club_list'),
]
