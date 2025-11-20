# clubs/urls.py
# URL routing for the clubs app.
# Maps URLs like /clubs/ and /clubs/add/ to corresponding views.


from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_club, name='add_club'),
    path('', views.club_list, name='club_list'),
    path("delete/<int:club_id>/", views.delete_club, name="delete_club"),

]
