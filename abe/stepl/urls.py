from stepl.IndexView import IndexView
from stepl.InputMainView import InputMainView
from stepl.CLIGENMapView import CLIGENMapView
from django.conf.urls import url

urlpatterns = [ 
    url(r'^$', IndexView.as_view()), 
    url(r'^inputMain$', InputMainView.as_view()), 
    url(r'^CLIGENMap$', CLIGENMapView.as_view()), 
]