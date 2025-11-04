
from django.urls import path
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
]
