from django.db import models

# Create your models here.
class IndexInput(models.Model):
    num_watershd = models.IntegerField()
    num_gully = models.IntegerField()
    num_steambank = models.IntegerField()
