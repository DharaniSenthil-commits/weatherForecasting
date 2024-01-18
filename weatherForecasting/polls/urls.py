from django.urls import path
from . import views


urlpatterns = [
    path('polls/', views.temp_here, name='temp_here'),
    path('polls/discover', views.temp_somewhere, name='temp_somewhere'),
]