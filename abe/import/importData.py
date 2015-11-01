from stepl.stepl_setting import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from stepl.models import *
from stepl.templatetags.simple_tags import twonum
from stepl.tools import extract
      
    
def iSoilTexture(data):
    for i in range(1,11):
        textureClass = Soil_Textural_Class_Choices[i-1][0]
        dryDencity = data['GullyDB_'+twonum(i)+"1"]
        correctFactor = data['GullyDB_'+twonum(i)+"2"]
        s = SoilTexture(Standard=INPUT_STANDARD,Soil_Textural_Class=textureClass,Dry_Density=dryDencity,Correction_Factor=correctFactor)
        s.save()
def iReferenceRunoff(data):
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
def iDetailedReferenceRunoff(data):
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
def iNutrientRunoff(data):
    keyMap = (
            ('L-Cropland','ntLcrop_1'),
            ('L-Cropland-w/-manure','ntLcrop_2'),
            ('M-Cropland','ntMcrop_1'),
            ('M-Cropland-w/-manure','ntMcrop_2'),
            ('H-Cropland','ntHcrop_1'),
            ('H-Cropland-w/-manure','ntHcrop_2'),
            ('Pastureland','ntPast'),
            ('Forest','ntFrst'),
            ('User-Defined','ntUser')
        )
    for t in keyMap:
        r = NutrientRunoff(Standard=INPUT_STANDARD,Landuse=t[0])
        r.N = data[t[1]+"_N"]
        r.P = data[t[1]+"_P"]
        r.BOD = data[t[1]+"_B"]
        r.save() 

def iNutrientGroundwaterRunoff(data):
    keyMap = (
            ('Urban','GntUrbn'),
            ('Cropland','GntCrop'),
            ('Pastureland','GntPast'),
            ('Forest','GntFrst'),
            ('Feedlot','GntFeed'),
            ('User-Defined','GntUser'),
        )
    for t in keyMap:
        r = NutrientGroundwaterRunoff(Standard=INPUT_STANDARD,Landuse=t[0])
        r.N = data[t[1]+"_N"]
        r.P = data[t[1]+"_P"]
        r.BOD = data[t[1]+"_B"]
        r.save() 
def iSoilInfiltrationFraction(data):
    HSGs = ['','Urban','Cropland','Pastureland','Forest','User-Defined']
    for i in range(1,6):
        HSG = HSGs[i]
        r = SoilInfiltrationFraction(Standard=INPUT_STANDARD,HSG=HSG)
        r.A = data['gwInft_'+str(i)+"1"]
        r.B = data['gwInft_'+str(i)+"2"]
        r.C = data['gwInft_'+str(i)+"3"]
        r.D = data['gwInft_'+str(i)+"4"]
        r.save() 

def iLanduseDistributionAbstract():
    l = LanduseDistribution(Standard=INPUT_STANDARD)
    l.Commercial = 15
    l.Industrial = 10
    l.Institutional = 10
    l.Transportation = 10
    l.Multi_Family = 10
    l.Single_Family = 30
    l.Urban_Cultivated = 5
    l.Vacant_developed  = 5
    l.Open_Space = 5
    l.Total = 100
    l.save()

def iIrrigation():    
    i  = Irrigation(Standard=INPUT_STANDARD)
    i.Cropland_Acres_Irrigated = 0
    i.Water_Depth_in_per_Irrigation_Before_BMP = 0
    i.Water_Depth_in_per_Irrigation_After_BMP = 0
    i.Irrigation_Frequency_perYear = 0
    i.save()
def iAnimalWeight(data):
    Animals = ['','Beef cattle','Dairy cow','Hog','Sheep','Horse','Chicken (Layer)','Turkey','Duck','Goose','Deer','Beaver','Raccoon','Other',]
    for i in range(1,14):
        Animal = Animals[i]
        r = AnimalWeight(Standard=INPUT_STANDARD,Animal=Animal)
        r.MassLb = data['Reference_'+twonum(i)+"1"]
        r.BOD_per_1000lb = data['Reference_'+twonum(i)+"2"]
        r.BOD_per_day = data['Reference_'+twonum(i)+"3"]
        r.BDO_per_year = data['Reference_'+twonum(i)+"4"]
        r.save() 
def iSepticSystem():
    s1 = SepticSystem(Standard=INPUT_STANDARD,Title='Total Nitrogen-mg/L ')
    s1.ACR = 60
    s1.Wastewater_per_capita = 40
    s1.save()
    s2 = SepticSystem(Standard=INPUT_STANDARD,Title='Total Phosphorus-mg/L')
    s2.ACR = 23.5
    s2.Wastewater_per_capita = 8
    s2.save()
    s3 = SepticSystem(Standard=INPUT_STANDARD,Title='Organics (BOD)-mg/L')
    s3.ACR = 245
    s3.Wastewater_per_capita = 220
    s3.save()
    s4 = SepticSystem(Standard=INPUT_STANDARD,Title='TSO^2-gal/day/person ')
    s4.ACR = 70
    s4.Wastewater_per_capita = 75
    s4.save()
def iFeedlotAnimal(data):
    Animals = ['','Slaughter Steer','Young Beef','Dairy Cow','Young Dairy Stock','Swine','Feeder Pig','Sheep','Horse','Chicken','Turkey','Duck']
    for i in range(1,12):
        Animal = Animals[i]
        r = FeedlotAnimal(Standard=INPUT_STANDARD,Animal=Animal)
        r.N = data['Feedlot_'+twonum(i)+"1"]
        r.P = data['Feedlot_'+twonum(i)+"2"]
        r.BOD = data['Feedlot_'+twonum(i)+"3"]
        r.COD = data['Feedlot_'+twonum(i)+"4"]
        r.save() 
def iLateralRecessionRate():
    l = LateralRecessionRate(Standard=INPUT_STANDARD,Category='Slight')
    l.LRR = '0.01 - 0.05' 
    l.Medium_Value = 0.03
    l.save()
    l = LateralRecessionRate(Standard=INPUT_STANDARD,Category='Moderate')
    l.LRR = '0.06 - 0.20'
    l.Medium_Value = 0.13
    l.save()
    l = LateralRecessionRate(Standard=INPUT_STANDARD,Category='Severe')
    l.LRR = '0.30 - 0.50'
    l.Medium_Value = 0.40
    l.save()
    l = LateralRecessionRate(Standard=INPUT_STANDARD,Category='Very Severe')
    l.LRR = '0.50 +'
    l.Medium_Value = 0.50
    l.save()
def iGullyErosion():
    #all to zero
    g = GullyErosion(Standard=INPUT_STANDARD)
    g.save()
def iStreambankErosion():
    #all to zero
    s = StreambankErosion(Standard=INPUT_STANDARD)
    s.save()

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

iSoilTexture(data)
iReferenceRunoff(data)
iDetailedReferenceRunoff(data)
iNutrientRunoff(data)
iNutrientGroundwaterRunoff(data)
iSoilInfiltrationFraction(data)
iLanduseDistributionAbstract()
iIrrigation()
iAnimalWeight(data)
iFeedlotAnimal(data)
iLateralRecessionRate()
iGullyErosion()
iStreambankErosion()