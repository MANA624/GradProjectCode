from django.urls import path
from . import views
from django.conf.urls import url
# We can create namespaces to separate URL patterns
app_name = "tutorials"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tutorial_id>[0-9]+)/$', views.see_tutorial, name='see_tutorial'),
]