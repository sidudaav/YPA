from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('chapters/', views.chapters_home, name='home'),
    path('view-chapters/', views.view_chapters, name="view-chapters"),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('events/', views.events, name='events'),
    path('events/psb', views.events_psb, name='events-psb')
]
