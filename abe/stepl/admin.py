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

admin.site.register(ReferenceRunoff)
admin.site.register(ReferenceRunoffInput)

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

class AnimalWeightAdmin(admin.ModelAdmin):
    list_display = ("Standard","Animal")
    search_fields = ['Animal']
admin.site.register(AnimalWeight,AnimalWeightAdmin)
admin.site.register(SepticSystem)
admin.site.register(FeedlotAnimal)
admin.site.register(SoilTexture)
admin.site.register(LateralRecessionRate)
admin.site.register(GullyErosion)
admin.site.register(StreambankErosion)

admin.site.register(SoilInfiltrationFractionInput)
admin.site.register(WildlifeDensityInCropLandInput)

class AnimalWeightInputAdmin(admin.ModelAdmin):
    list_display = ("Standard","Animal")
    search_fields = ['Animal']
admin.site.register(AnimalWeightInput)
admin.site.register(SepticSystemInput)
admin.site.register(FeedlotAnimalInput)
admin.site.register(SoilTextureInput)
admin.site.register(LateralRecessionRateInput)
admin.site.register(GullyErosionInput)
admin.site.register(StreambankErosionInput)
admin.site.register(UniversalSoilLossEquation)
