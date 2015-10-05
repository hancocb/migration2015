from django.db import models

#model for index input data
class IndexInput(models.Model):
    num_watershd = models.IntegerField()
    num_gully = models.IntegerField()
    num_steambank = models.IntegerField()

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
class UrbanReferenceRunoff(RunoffAbastract):
  Landuse = models.CharField(max_length=30,unique=True)

class UrbanReferenceRunoffInput(RunoffAbastract):
  Landuse = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Landuse')


#Step 6a. Detailed urban reference runoff curve number
class DetailedRunoff(RunoffAbastract):
  Urban = models.CharField(max_length=30,unique=True)

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
  Landuse = models.CharField(max_length=30,unique=True)

class NutrientRunoffInput(NutrientAbstract):
  Landuse = models.CharField(max_length=30,db_index=True)  
  session_id = models.IntegerField() 
  class Meta:
    unique_together = ('session_id', 'Landuse')

#7a. Nutrient concentration in shallow groundwater (mg/l)
class NutrientGroundwaterRunoff(NutrientAbstract):
  Landuse = models.CharField(max_length=30,unique=True)

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



