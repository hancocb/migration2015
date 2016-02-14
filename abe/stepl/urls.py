from stepl.IndexView import IndexView
from stepl.InputMainView import InputMainView
from stepl.ImportMainView import ImportMainView
from stepl.UserSessionView import UserSessionView
from stepl.LogoutView import LogoutView
from stepl.BmpMainView import BmpMainView
from stepl.RunStep1View import RunStep1View
from stepl.RerunStep1View import RerunStep1View
from stepl.CLIGENMapView import CLIGENMapView
from stepl.CountyDataJson import CountyDataJson
from stepl.OptMainView import OptMainView
from stepl.OtherTablesView import OtherTablesView
from stepl.ItemView import ItemView
from django.conf.urls import url

urlpatterns = [ 
    url(r'^$', IndexView.as_view()), 
    url(r'^inputMain$', InputMainView.as_view()), 
    url(r'^importMain$', ImportMainView.as_view()), 
    url(r'^userSession$', UserSessionView.as_view()), 
    url(r'^logout$', LogoutView.as_view()), 
    url(r'^bmpMain$', BmpMainView.as_view()), 
    url(r'^runStep1$', RunStep1View.as_view()), 
    url(r'^rerunStep1$', RerunStep1View.as_view()), 
    url(r'^CLIGENMap$', CLIGENMapView.as_view()), 
    url(r'^CountyDataJson$', CountyDataJson.as_view()), 
    url(r'^optMain$', OptMainView.as_view()), 
    url(r'^otherTables$', OtherTablesView.as_view()), 
    url(r'^item/(\w+)/(\d+)/$', ItemView.as_view()), 

]
