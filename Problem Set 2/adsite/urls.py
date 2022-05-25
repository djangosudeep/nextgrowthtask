from . import views
from django.urls import path


urlpatterns = [
    path('', views.submit),
    path('submit', views.home),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
]