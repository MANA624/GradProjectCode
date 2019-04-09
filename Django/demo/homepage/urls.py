from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path('', views.index, name='index'),
    # Could include a path to login if we wanted to
    # path('login', views.login, name='login'),
]
