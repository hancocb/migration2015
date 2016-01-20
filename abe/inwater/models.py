from django.db import models

# each instance of Monitoring model is a dataset of a agency(organization) of a agency type
class Monitoring(models.Model):
    gid             = models.IntegerField(db_index=True)
    agency_type     = models.CharField(max_length=200, db_index=True)
    agency_organization = models.CharField(max_length=200, db_index=True)
    name            = models.CharField(max_length=200, db_index=True)
    site_no         = models.CharField(max_length=200)
    description     = models.CharField(max_length=1000)
    parameter_type  = models.CharField(max_length=1000)
    parameter       = models.CharField(max_length=1000)
    frequency       = models.CharField(max_length=100)
    publicly_available  = models.CharField(max_length=10)
    start_date      = models.CharField(max_length=10)
    end_date        = models.CharField(max_length=10)
    contact_url     = models.CharField(max_length=1000)
    quality         = models.CharField(max_length=10)
    user_email      = models.CharField(max_length=200)
    huc_8           = models.CharField(max_length=8)
    huc_10          = models.CharField(max_length=10)
    huc_12          = models.CharField(max_length=12)

    #for input and converting into clipped_geom
    text_geom       = models.CharField(max_length=1000,default="")
    #text_geom into automatically by heart-beating script
    clipped_geom    = models.BinaryField()
    class Meta:
        index_together = [
            #for select distinct name where agency_type=xxx
            ["agency_type", "name"],
            ##for select distinct name where agency_organization=xxx
            ["agency_organization", "name"],
        ]
