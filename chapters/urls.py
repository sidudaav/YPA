from django.urls import path
from . import views

app_name = 'chapters'

urlpatterns = [
    path('home/', views.home, name='home')
]
