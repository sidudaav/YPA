from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('events/', views.events, name='events'),
    path('events/psb', views.events_psb, name='events-psb'),
    path('events/codeify', views.events_codeify, name='events-codeify'),
    path('events/think', views.events_think, name='events-think'),
]
