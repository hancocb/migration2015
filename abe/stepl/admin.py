from django.contrib import admin

from .models import *

class CountyDataAdmin(admin.ModelAdmin):
    list_display = ("state_name","name")
    search_fields = ['state_name']

class IndexInputAdmin(admin.ModelAdmin):
    list_display = ("id","num_watershd","num_gully","num_steambank")

admin.site.register(CountyData, CountyDataAdmin)
admin.site.register(CountyDataInput, CountyDataAdmin)
admin.site.register(IndexInput, IndexInputAdmin)

#optMain
admin.site.register(SoilData)
admin.site.register(SoilDataInput)

admin.site.register(UrbanReferenceRunoff)
admin.site.register(UrbanReferenceRunoffInput)

admin.site.register(DetailedRunoff)
admin.site.register(DetailedRunoffInput)
admin.site.register(NutrientRunoff)
admin.site.register(NutrientRunoffInput)
admin.site.register(NutrientGroundwaterRunoff)
admin.site.register(NutrientGroundwaterRunoffInput)
admin.site.register(LanduseDistribution)
admin.site.register(LanduseDistributionInput)
admin.site.register(Irrigation)
admin.site.register(IrrigationInput)

#from below "If you want to change DBs, click button."
admin.site.register(SoilInfiltrationFraction)
admin.site.register(WildlifeDensityInCropLand)
admin.site.register(AnimalWeight)
admin.site.register(SepticSystem)
admin.site.register(FreelotAnimal)
admin.site.register(SoilTexture)
admin.site.register(LateralRecessionRate)
admin.site.register(GullyErosion)
admin.site.register(StreambankErosion)

admin.site.register(SoilInfiltrationFractionInput)
admin.site.register(WildlifeDensityInCropLandInput)
admin.site.register(AnimalWeightInput)
admin.site.register(SepticSystemInput)
admin.site.register(FreelotAnimalInput)
admin.site.register(SoilTextureInput)
admin.site.register(LateralRecessionRateInput)
admin.site.register(GullyErosionInput)
admin.site.register(StreambankErosionInput)