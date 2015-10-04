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
  SHG = models.CharField(max_length=10, unique=True)

class SoilDataInput(SoilDataAbstract):
  session_id = models.IntegerField()   
  watershd_id = models.IntegerField()
  class Meta:
    unique_together = ('session_id', 'watershd_id')

#Detailed urban reference runoff curve number
class UrbanReferenceRunoffAbastract(models.Model):
  SHG_A = models.IntegerField()
  SHG_B = models.IntegerField()
  SHG_C = models.IntegerField()
  SHG_D = models.IntegerField()
  class Meta:
    abstract = True

class UrbanReferenceRunoff(UrbanReferenceRunoffAbastract):
  Urban = models.CharField(max_length=10,unique=True)

class UrbanReferenceRunoffInput(UrbanReferenceRunoffAbastract):
  Urban = models.CharField(max_length=10,db_index=True)  
  session_id = models.IntegerField(unique=True) 
