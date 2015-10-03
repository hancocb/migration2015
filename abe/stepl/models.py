from django.db import models

#model for index input data
class IndexInput(models.Model):
    num_watershd = models.IntegerField()
    num_gully = models.IntegerField()
    num_steambank = models.IntegerField()

#model for county data
class CountyData(models.Model):
   state_name = models.CharField(max_length=30)  
   name = models.CharField(max_length=30) 
   state_name_name = models.CharField(max_length=30) 
   rainfall_inches = models.FloatField()
   raindays = models.FloatField()
   runoff = models.FloatField()
   station_name = models.CharField(max_length=30 ,null=True ) 
   ptrecipitation_correction_factor = models.FloatField( null=True )
   no_of_rain_days_correction_factor = models.FloatField( null=True )
   rmean = models.FloatField( null=True )
   kmean = models.FloatField( null=True )
   lsavg = models.FloatField( null=True )
   cavg  = models.FloatField( null=True )
   pavg  = models.FloatField( null=True )
   class Meta:
    unique_together = ('state_name', 'name')
