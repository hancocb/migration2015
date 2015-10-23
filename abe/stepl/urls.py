from stepl.IndexView import IndexView
from stepl.InputMainView import InputMainView
from stepl.BmpMainView import BmpMainView
from stepl.CLIGENMapView import CLIGENMapView
from stepl.CountyDataJson import CountyDataJson
from stepl.OptMainView import OptMainView
from stepl.OtherTablesView import OtherTablesView
from django.conf.urls import url

urlpatterns = [ 
    url(r'^$', IndexView.as_view()), 
    url(r'^inputMain$', InputMainView.as_view()), 
    url(r'^bmpMain$', BmpMainView.as_view()), 
    url(r'^CLIGENMap$', CLIGENMapView.as_view()), 
    url(r'^CountyDataJson$', CountyDataJson.as_view()), 
    url(r'^optMain$', OptMainView.as_view()), 
    url(r'^otherTables$', OtherTablesView.as_view()), 
]
