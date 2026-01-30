# pantherconnect/urls.py
# Defines the URL routing for the project.
# Includes paths for admin, members, and clubs apps.

from django.contrib import admin
from django.urls import include, path
from clubs.views import login_view
from clubs import views

urlpatterns = [
    path("members/", include("members.urls")),
    path("clubs/", include("clubs.urls")),
    path("admin/", admin.site.urls),
    path("", views.home_view, name="home"),
]

