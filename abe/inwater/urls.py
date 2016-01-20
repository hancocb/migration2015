from django.conf.urls import url
from inwater.IndexView import IndexView
from inwater.AgencyView import AgencyView

urlpatterns = [
    url(r'^$', IndexView.as_view()), 
    url(r'^agency/([^/]+)/([^/]+)/$', AgencyView.as_view()), 
]
