from django.db import models
from django.utils.functional import lazy

#model for index input data
class IndexInput(models.Model):
    num_watershd = models.IntegerField()
    num_gully = models.IntegerField()
    num_steambank = models.IntegerField()
    #Groundwater load calculation
    gwOpt = models.BooleanField(default=True)
    #Treat all the subwatersheds as parts of a single watershed
    swsOpt = models.BooleanField(default=True)

#map 1~6 (for form mapping and mapping to fortran model)
WatershedLandUse_index_map = ['',  "Urban" ,  "Cropland" ,  "Pastureland" ,  'Forest' ,  'UserDefined' ,  'Feedlots' ]
class WatershedLandUse(models.Model):
  watershd_id = models.IntegerField()
  #Soil Hydrologic Group(A,B,C,D)
  HSG = models.IntegerField(default=1)
  Urban = models.FloatField(default=0)
  Cropland = models.FloatField(default=0)
  Pastureland = models.FloatField(default=0)
  Forest = models.FloatField(default=0)
  UserDefined = models.FloatField(default=0)
  Feedlots = models.FloatField(default=0)
  FeedlotPercentPaved = models.IntegerField(default=20)
  Total = models.FloatField(default=0)
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'watershd_id')

#map 1~8 (for form mapping and mapping to fortran model)
AgriAnimal_index_map = ['','Beef' ,  'Dairy',  'Swine',  'Sheep',  'Horse' ,  'Chicken',  'Turkey' ,  'Duck' ]
class AgriAnimal(models.Model):
  watershd_id = models.IntegerField()
  Beef = models.IntegerField(default=0)
  Dairy = models.IntegerField(default=0)
  Swine = models.IntegerField(default=0)
  Sheep = models.IntegerField(default=0)
  Horse = models.IntegerField(default=0)
  Chicken = models.IntegerField(default=0)
  Turkey = models.IntegerField(default=0)
  Duck = models.IntegerField(default=0)
  numMonthsManureApplied = models.IntegerField(default=0)
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'watershd_id')

class SepticNillegal(models.Model):
  watershd_id = models.IntegerField()
  numSepticSystems = models.IntegerField(default=0)
  PopulationPerSeptic = models.IntegerField(default=0)
  SepticFailureRate_Percent = models.IntegerField(default=0)
  Wastewater_Direct_Discharge_numPeople = models.IntegerField(default=0)
  Direct_Discharge_Reduction_Percent = models.IntegerField(default=0)
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'watershd_id')

'''
#for hidden static data KV...just found that I have already implemented it in other way...
shit....wasted 2 hours here!!!!!
class StaticInputMainData(models.Model):
    Standard = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.FloatField(default=0)
    class Meta:
      unique_together = ('Standard', 'key')

class StaticInputMainInput(models.Model):
    session_id = models.IntegerField() 
    key = models.CharField(max_length=30)
    value = models.FloatField(default=0)
    class Meta:
      unique_together = ('session_id', 'key')
'''

#model for county abstract data
class CountyDataAbstract(models.Model):
   state_name = models.CharField(max_length=30)  
   name = models.CharField(max_length=30) 
   
   rmean = models.FloatField( null=True )
   kmean = models.FloatField( null=True )
   lsavg = models.FloatField( null=True )
   cavg  = models.FloatField( null=True )
   pavg  = models.FloatField( null=True )
   class Meta:
    abstract = True


#model for county static data
class CountyData(CountyDataAbstract):
    #combination of state_name and name (county name)
   state_name_name = models.CharField(max_length=30) 

   rainfall_inches = models.FloatField()
   raindays = models.FloatField()
   runoff = models.FloatField()
   station_name = models.CharField(max_length=30 ,null=True ) 
   ptrecipitation_correction_factor = models.FloatField( null=True )
   no_of_rain_days_correction_factor = models.FloatField( null=True )
   class Meta:
    unique_together = ('state_name', 'name')
  

#model for county input data
class CountyDataInput(CountyDataAbstract):
  session_id = models.IntegerField(unique=True) 

#soil data
class SoilDataAbstract(models.Model):
  Soil_N_Conc =  models.FloatField()
  Soil_P_Conc =  models.FloatField()
  Soil_BOD_Conc =  models.FloatField()
  class Meta:
    abstract = True

class SoilData(SoilDataAbstract):
  Standard = models.CharField(max_length=30, unique=True)

class SoilDataInput(SoilDataAbstract):
  session_id = models.IntegerField()   
  watershd_id = models.IntegerField()
  class Meta:
    unique_together = ('session_id', 'watershd_id')

#runoff curve number
class RunoffAbastract(models.Model):
  SHG_A = models.IntegerField()
  SHG_B = models.IntegerField()
  SHG_C = models.IntegerField()
  SHG_D = models.IntegerField()
  class Meta:
    abstract = True

#Step 6. Reference runoff curve number
class ReferenceRunoff(RunoffAbastract):
  Landuse = models.CharField(max_length=30)
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Landuse')

class ReferenceRunoffInput(RunoffAbastract):
  Landuse = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Landuse')


#Step 6a. Detailed urban reference runoff curve number
class DetailedRunoff(RunoffAbastract):
  Urban = models.CharField(max_length=30)
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Urban')

class DetailedRunoffInput(RunoffAbastract):
  Urban = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Urban')

#abstract chemical Nutrient
class NutrientAbstract(models.Model):
  N =  models.FloatField()
  P =  models.FloatField()
  BOD =  models.FloatField()
  class Meta:
    abstract = True

#7.Nutrient concentration in runoff
class NutrientRunoff(NutrientAbstract):
  Landuse = models.CharField(max_length=30)
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Landuse')

class NutrientRunoffInput(NutrientAbstract):
  Landuse = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Landuse')

#7a. Nutrient concentration in shallow groundwater (mg/l)
class NutrientGroundwaterRunoff(NutrientAbstract):
  Landuse = models.CharField(max_length=30)
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Landuse')

class NutrientGroundwaterRunoffInput(NutrientAbstract):
  Landuse = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Landuse')

#8. Input or modify urban land use distribution
class LanduseDistributionAbstract(models.Model):
  Commercial = models.FloatField(default=0)
  Industrial = models.FloatField(default=0)  
  Institutional = models.FloatField(default=0) 
  Transportation = models.FloatField(default=0)  
  Multi_Family = models.FloatField(default=0)  
  Single_Family = models.FloatField(default=0) 
  Urban_Cultivated = models.FloatField(default=0)  
  Vacant_developed = models.FloatField(default=0)
  Open_Space = models.FloatField(default=0)
  Total = models.FloatField(default=0)
  class Meta:
    abstract = True
# watershd_id
class LanduseDistribution(LanduseDistributionAbstract):
  Standard = models.CharField(max_length=30, unique=True)

class LanduseDistributionInput(LanduseDistributionAbstract):
  session_id = models.IntegerField()   
  watershd_id = models.IntegerField()
  class Meta:
    unique_together = ('session_id', 'watershd_id')

#9.Input irrigation area (ac) and irrigation amount (in)
class IrrigationAbstract(models.Model):
  Cropland_Acres_Irrigated = models.FloatField(default=0) 
  Water_Depth_in_per_Irrigation_Before_BMP = models.FloatField(default=0) 
  Water_Depth_in_per_Irrigation_After_BMP = models.FloatField(default=0)  
  Irrigation_Frequency_perYear = models.FloatField(default=0) 
  class Meta:
    abstract = True
    
# watershd_id
class Irrigation(IrrigationAbstract):
  Standard = models.CharField(max_length=30, unique=True)

class IrrigationInput(IrrigationAbstract):
  session_id = models.IntegerField()   
  watershd_id = models.IntegerField()
  class Meta:
    unique_together = ('session_id', 'watershd_id')

#optMain ends...

# Reference Soil Infiltration Fraction for Precipitation
class SoilInfiltrationFractionAbstract(models.Model):
  HSG = models.CharField(max_length=30,default='',db_index=True)
  A = models.FloatField(default=0) 
  B = models.FloatField(default=0) 
  C = models.FloatField(default=0) 
  D = models.FloatField(default=0) 
  class Meta:
    abstract = True

class SoilInfiltrationFraction(SoilInfiltrationFractionAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'HSG')

class SoilInfiltrationFractionInput(SoilInfiltrationFractionAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'HSG')

#Wildlife density in cropland
class WildlifeDensityInCropLandAbstract(models.Model):
  Wildlife = models.CharField(max_length=30,default='')
  NumPerMileSquare = models.IntegerField(default=0)
  class Meta:
    abstract = True

class WildlifeDensityInCropLand(WildlifeDensityInCropLandAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Wildlife')

class WildlifeDensityInCropLandInput(WildlifeDensityInCropLandAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Wildlife')

#Standard Animal Weight Table
class AnimalWeightAbstract(models.Model):
  Animal = models.CharField(max_length=30,default='')
  MassLb = models.FloatField(default=0) 
  BOD_per_1000lb = models.FloatField(default=0) 
  BOD_per_day = models.FloatField(default=0) 
  BDO_per_year = models.FloatField(default=0) 
  class Meta:
    abstract = True

class AnimalWeight(AnimalWeightAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Animal')

class AnimalWeightInput(AnimalWeightAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Animal')

#DB for Septic System  
class SepticSystemAbstract(models.Model):
  Title = models.CharField(max_length=30,default='')
  ACR = models.FloatField(default=0)
  Wastewater_per_capita = models.FloatField(default=0)
  class Meta:
    abstract = True

class SepticSystem(SepticSystemAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Title')

class SepticSystemInput(SepticSystemAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Title')

# Feedlot DB table: Ratio of nutrients produced by animals relative to 1000 lb of slaughter steer
class FeedlotAnimalAbstract(models.Model):
  Animal = models.CharField(max_length=30,default='')
  N = models.FloatField(default=0) 
  P = models.FloatField(default=0) 
  BOD = models.FloatField(default=0) 
  COD = models.FloatField(default=0) 
  class Meta:
    abstract = True

class FeedlotAnimal(FeedlotAnimalAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Animal')

class FeedlotAnimalInput(FeedlotAnimalAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Animal')

#GullyDB: Soil Textural DB
Soil_Textural_Class_Choices = (
    ('Clay','Clay'),
    ('ClayLoam','ClayLoam'),
    ('FineSandyLoam','FineSandyLoam'),
    ('Loams,SandyClayLoams','Loams,SandyClayLoams'),
    ('Organic','Organic'),
    ('Sands,LoamySands','Sands,LoamySands'),
    ('SandyClay','SandyClay'),
    ('SandyLoam','SandyLoam'),
    ('SiltLoam','SiltLoam'),
    ('SiltyClayLoam,SiltyClay','SiltyClayLoam,SiltyClay'),
  )
class SoilTextureAbstract(models.Model):
  Soil_Textural_Class = models.CharField(max_length=30,default='Clay',choices=Soil_Textural_Class_Choices)
  Dry_Density = models.FloatField(default=0) 
  Correction_Factor = models.FloatField(default=0) 
  class Meta:
    abstract = True

class SoilTexture(SoilTextureAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Soil_Textural_Class')

class SoilTextureInput(SoilTextureAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Soil_Textural_Class')

#GullyDB: Lateral Recession Rate (LRR) DB
class LateralRecessionRateAbstract(models.Model):
  Category = models.CharField(max_length=30,default='')
  LRR = models.FloatField(default=0) 
  Medium_Value = models.FloatField(default=0) 
  class Meta:
    abstract = True

class LateralRecessionRate(LateralRecessionRateAbstract):
  Standard = models.CharField(max_length=30)
  class Meta:
    unique_together = ('Standard', 'Category')

class LateralRecessionRateInput(LateralRecessionRateAbstract):
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Category')

# Eroion: Gully 
class GullyErosionAbstract(models.Model):
  SoilTexture = models.CharField(max_length=30,default='Clay',choices=Soil_Textural_Class_Choices)
  BMP_Efficiency = models.FloatField(default=0) 
  Years_to_Form = models.FloatField(default=0) 
  Length = models.FloatField(default=0) 
  Depth = models.FloatField(default=0) 
  Bottom_Width = models.FloatField(default=0) 
  Top_Width = models.FloatField(default=0) 
  class Meta:
    abstract = True

class GullyErosion(GullyErosionAbstract):
  Standard = models.CharField(max_length=30,unique=True)

#import pdb; pdb.set_trace()
def get_models_watershd_choices():
  return GullyErosionInput.models_choices_tuple
 
class GullyErosionInput(GullyErosionAbstract):
  models_choices_tuple = []
  session_id = models.IntegerField() 
  Gully_id = models.IntegerField() 
  watershd_id = models.IntegerField( ) 
  class Meta:
    unique_together = ('session_id', 'Gully_id')
  def __init__(self,  *args, **kwargs):
      super(GullyErosionInput, self).__init__(*args, **kwargs)
      self._meta.get_field_by_name('watershd_id')[0]._choices = get_models_watershd_choices()

# Eroion: Streambank
class StreambankErosionAbstract(models.Model):
  SoilTexture = models.CharField(max_length=30,default='Clay',choices=Soil_Textural_Class_Choices)
  BMP_Efficiency = models.FloatField(default=0) 
  Lateral_Recession = models.FloatField(default=0) 
  Length = models.FloatField(default=0) 
  Height = models.FloatField(default=0) 
  class Meta:
    abstract = True

class StreambankErosion(StreambankErosionAbstract):
  Standard = models.CharField(max_length=30,unique=True)

class StreambankErosionInput(StreambankErosionAbstract):
  session_id = models.IntegerField() 
  Streambank_id = models.IntegerField() 
  watershd_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Streambank_id')
  def __init__(self,  *args, **kwargs):
      super(StreambankErosionInput, self).__init__(*args, **kwargs)
      self._meta.get_field_by_name('watershd_id')[0]._choices = get_models_watershd_choices()

#bmp input
class  BMPInput(models.Model):
  session_id = models.IntegerField() 
  #!!!landtype_id: 1~5 : Cropland, pastland, forest,user defined, feedlot
  landtype_id = models.IntegerField() 
  watershd_id = models.IntegerField() 
  BMP = models.IntegerField(default=0)
  PercentApplied = models.FloatField(default=100)
  N = models.FloatField(default=0)
  P = models.FloatField(default=0)
  BOD = models.FloatField(default=0)
  Sediment = models.FloatField(default=0)
  class Meta:
    unique_together = ('session_id', 'landtype_id','watershd_id')

#UrbanBmpInput
class UrbanBmpInput(models.Model):
    session_id = models.IntegerField() 
    # 1)for(i=1~4)
    #    for(j=1~9) 
    #       UrbnConc_ij
    # 2) {% for k in ctx.range5 %}
    #     {% for i in ctx.rangeWSD %}
    #       {% for j in ctx.range9 %}
    #         UrbanBMP_{{k}}_{{i|twonum}}{{j}} 
    key = models.CharField(max_length=30)
    value = models.FloatField(default=0)
    class Meta:
      unique_together = ('session_id', 'key')
#
#