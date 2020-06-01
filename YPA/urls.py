from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('team/', include('team.urls', namespace='team')),
    path('chapters/', include('chapters.urls', namespace='chapters')),
    path('events/', include('events.urls', namespace='events')),
    path('contact/', include('contact.urls', namespace='contact')),
]
