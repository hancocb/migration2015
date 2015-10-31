from stepl.stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from stepl.models import *
from stepl.templatetags.simple_tags import twonum
from stepl.tools import extract
      
    
def importSoilTexture(data):
    for i in range(1,11):
        textureClass = Soil_Textural_Class_Choices[i-1][0]
        dryDencity = data['GullyDB_'+twonum(i)+"1"]
        correctFactor = data['GullyDB_'+twonum(i)+"2"]
        s = SoilTexture(Standard=INPUT_STANDARD,Soil_Textural_Class=textureClass,Dry_Density=dryDencity,Correction_Factor=correctFactor)
        s.save()
def importReferenceRunoff(data):
    keyMap = (  ('Urban',   'urban'),
                ('Cropland',    'crop'),
                ('Pastureland', 'past'),
                ('Forest',  'frst'),
                ('User Defined',    'user') )
    for t in keyMap:
        r = ReferenceRunoff(Standard=INPUT_STANDARD,Landuse=t[0])
        r.SHG_A = data["CN_"+t[1]+"_A"]
        r.SHG_B = data["CN_"+t[1]+"_B"]
        r.SHG_C = data["CN_"+t[1]+"_C"]
        r.SHG_D = data["CN_"+t[1]+"_D"]
        r.save() 
def importDetailedReferenceRunoff(data):
    keyMap = (
            ('Commercial','comm'),
            ('Industrial','indu'),
            ('Institutional','inst'),
            ('Transportation','tran'),
            ('Multi-Family','mult'),
            ('Single-Family','sing'),
            ('Urban-Cultivated','urcu'),
            ('Vacant-Developed','vade'),
            ('Open Space',  'open')
        )
    for t in keyMap:
        r = DetailedRunoff(Standard=INPUT_STANDARD,Urban=t[0])
        r.SHG_A = data["CN_"+t[1]+"_A"]
        r.SHG_B = data["CN_"+t[1]+"_B"]
        r.SHG_C = data["CN_"+t[1]+"_C"]
        r.SHG_D = data["CN_"+t[1]+"_D"]
        r.save() 

data = {}
f = open("import/inputMainStaticData.txt","r")
res = f.read()
lines = res.split("\n")
lineNum = 0
for line in lines:
    lineNum = lineNum + 1
    pair = line.split("$")
    try:
        data[pair[0]] = float(pair[1])
    except:
        print "error in data:"+str(lineNum)+":"+str(line)
        exit()

#importSoilTexture(data)
#importReferenceRunoff(data)
importDetailedReferenceRunoff(data)

