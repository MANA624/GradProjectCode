from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials/', include('tutorials.urls')),
    path('forum/', include('forum.urls')),
    url(r'', include('homepage.urls')),
]
