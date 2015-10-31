from stepl.stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from stepl.models import *
from stepl.templatetags.simple_tags import twonum
from stepl.tools import extract

data = {}
f = open("tmp/inputMainStaticData.txt","r")
res = f.read()
lines = res.split("\n")
for line in lines:
    pair = line.split("$")
    data[pair[0]] = float(pair[1])
        
def importReferenceRunoff():
    keyMap = (  ('Urban',   'urban'),
                ('Cropland',    'crop'),
                ('Pastureland', 'past'),
                ('Forest',  'frst'),
                ('User Defined',    'user') )
    for t in KeyMap:
        
    
def importSoilTexture():
    for i in range(1,11):
    textureClass = Soil_Textural_Class_Choices[i-1][0]
    dryDencity = data['GullyDB_'+twonum(i)+"1"]
    correctFactor = data['GullyDB_'+twonum(i)+"2"]
    s = SoilTexture(Standard=INPUT_STANDARD,Soil_Textural_Class=textureClass,Dry_Density=dryDencity,Correction_Factor=correctFactor)
    s.save()
