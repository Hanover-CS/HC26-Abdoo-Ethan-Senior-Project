# clubs/urls.py
# URL routing for the clubs app.
# Maps URLs like /clubs/ and /clubs/add/ to corresponding views.


from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('add/', views.add_club, name='add_club'),
    path('', views.club_list, name='club_list'),
    path("delete/<int:club_id>/", views.delete_club, name="delete_club"),
    path('events/', views.event_list, name='event_list'),


]
