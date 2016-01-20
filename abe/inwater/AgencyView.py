from django.views.generic import View
from models import *
from django.shortcuts import render
from django.http import JsonResponse

class AgencyView(View):

    def get(self, request, agency_type, agency_organization):
        
        all_agency_types = Monitoring.objects.distinct("agency_type").values_list("agency_type").order_by('agency_type')

        if agency_type == "all":
            all_agencies = Monitoring.objects.distinct("agency_organization").values_list("agency_organization").order_by('agency_organization')            
        else:
            all_agencies = Monitoring.objects.filter(agency_type=agency_type).distinct("agency_organization").values_list("agency_organization").order_by('agency_organization')            
        
        if agency_organization == "all":
            all_datasets = Monitoring.objects.distinct("name").values_list("name").order_by('name')            
        else:
            all_datasets = Monitoring.objects.filter(agency_organization=agency_organization).distinct("name").values_list("name").order_by('name') 

        jsonMap = {
                    "all_agency_types"  :   self.list2dict(all_agency_types),
                    "all_agencies"      :   self.list2dict(all_agencies),
                    "all_datasets"      :   self.list2dict(all_datasets),
                    }
        return JsonResponse(jsonMap)

    def list2dict(self,mylist):
        ret = {}
        i = 0
        for ele in mylist:
            ret[i] = ele[0]
            i = i+1
        return ret



