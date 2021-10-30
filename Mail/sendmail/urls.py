from django.urls import path
from . import views
from .views import index, home

urlpatterns = [
    path('', views.index),
    path('index/', index),
    path('home/', home)
]
