from django.contrib import admin
from django.urls import path
from generato import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('generate/', views.generate_password, name='generate'),
]