from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles, name='home'),
    path('sample/', views.sample, name='sample')
]
