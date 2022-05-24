from django.urls import path
from . import views

# URL_Configuration
urlpatterns = [
    path('hello', views.say_hello),
]