from stepl.IndexView import IndexView
from stepl.InputMainView import InputMainView
from django.conf.urls import url

urlpatterns = [ 
    url(r'^$', IndexView.as_view()), 
    url(r'^inputMain$', InputMainView.as_view()), 
]
