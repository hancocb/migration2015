from django.db import models

# Create your models here.
class AdminListDisplay(models.Model):
    ClassName = models.CharField(max_length=50, default="")
    FieldName = models.CharField(max_length=50, default="")
    isShown = models.BooleanField(default=True, editable=True)
