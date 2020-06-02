from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='events'),
    path('psb/', views.psb_details, name='psb-details')
]
