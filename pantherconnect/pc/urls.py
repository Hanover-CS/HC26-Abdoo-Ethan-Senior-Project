from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("pc/", include("pc.urls")),
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),

]
