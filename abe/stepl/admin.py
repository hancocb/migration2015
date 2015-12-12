from django.contrib import admin
from adminDisplayManage.models import AdminListDisplay
from .models import *

def getDisplayFields(ModelName):
    DisplayFieldsIter = AdminListDisplay.objects.all().filter(ClassName=ModelName, isShown=True)
    FieldList = []
    for cur in DisplayFieldsIter:
        field = str(cur.FieldName)
        FieldList.append(field)
    return FieldList

class CountyDataAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("CountyData")
        return default_list_display
    #list_display = getDisplayFields("CountyData")
    search_fields = ['state_name_name']

class CountyDataInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("CountyDataInput")
        return default_list_display
    search_fields = ['LocName', 'Name']

class IndexInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("IndexInput")
        return default_list_display


admin.site.register(CountyData, CountyDataAdmin)
admin.site.register(CountyDataInput, CountyDataInputAdmin)
admin.site.register(IndexInput, IndexInputAdmin)

#optMain
class SoilDataAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilData")
        return default_list_display
    search_fields = []

class SoilDataInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilDataInput")
        return default_list_display
    search_fields = []

admin.site.register(SoilData, SoilDataAdmin)
admin.site.register(SoilDataInput, SoilDataInputAdmin)

class ReferenceRunoffAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("ReferenceRunoff")
        return default_list_display
    search_fields = ["Landuse"]

class ReferenceRunoffInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("ReferenceRunoffInput")
        return default_list_display
    search_fields = ["Landuse"]

admin.site.register(ReferenceRunoff,ReferenceRunoffAdmin)
admin.site.register(ReferenceRunoffInput, ReferenceRunoffInputAdmin)

class DetailedRunoffAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("DetailedRunoff")
        return default_list_display
    search_fields = ["Urban"]

class DetailedRunoffInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("DetailedRunoffInput")
        return default_list_display
    search_fields = ["Urban"]

admin.site.register(DetailedRunoff, DetailedRunoffAdmin)
admin.site.register(DetailedRunoffInput, DetailedRunoffInputAdmin)

class NutrientRunoffAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("NutrientRunoff")
        return default_list_display
    search_fields = ["Landuse"]

class NutrientRunoffInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("NutrientRunoffInput")
        return default_list_display
    search_fields = ["Landuse"]

admin.site.register(NutrientRunoff, NutrientRunoffAdmin)
admin.site.register(NutrientRunoffInput, NutrientRunoffInputAdmin)

class NutrientGroundwaterRunoffAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("NutrientGroundwaterRunoff")
        return default_list_display
    search_fields = ["Landuse"]

class NutrientGroundwaterRunoffInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("NutrientGroundwaterRunoffInput")
        return default_list_display
    search_fields = ["Landuse"]

admin.site.register(NutrientGroundwaterRunoff, NutrientGroundwaterRunoffAdmin)
admin.site.register(NutrientGroundwaterRunoffInput, NutrientGroundwaterRunoffInputAdmin)

class LanduseDistributionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("LanduseDistribution")
        return default_list_display
    search_fields = []

class LanduseDistributionInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("LanduseDistributionInput")
        return default_list_display
    search_fields = []

admin.site.register(LanduseDistribution, LanduseDistributionAdmin)
admin.site.register(LanduseDistributionInput, LanduseDistributionInputAdmin)

class IrrigationAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("Irrigation")
        return default_list_display
    search_fields = []

class IrrigationInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("IrrigationInput")
        return default_list_display
    search_fields = []

admin.site.register(Irrigation, IrrigationAdmin)
admin.site.register(IrrigationInput, IrrigationInputAdmin)

#from below "If you want to change DBs, click button."
class SoilInfiltrationFractionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilInfiltrationFraction")
        return default_list_display
    search_fields = ["HSG"]

class SoilInfiltrationFractionInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilInfiltrationFractionInput")
        return default_list_display
    search_fields = ["HSG"]

admin.site.register(SoilInfiltrationFraction, SoilInfiltrationFractionAdmin)
admin.site.register(SoilInfiltrationFractionInput, SoilInfiltrationFractionInputAdmin)



class AnimalWeightAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("AnimalWeight")
        return default_list_display
    search_fields = ['Animal']

admin.site.register(AnimalWeight, AnimalWeightAdmin)

class SepticSystemAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SepticSystem")
        return default_list_display
    search_fields = ["Title"]

class FeedlotAnimalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("FeedlotAnimal")
        return default_list_display
    search_fields = ["Animal"]

class SoilTextureAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilTexture")
        return default_list_display

class LateralRecessionRateAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("LateralRecessionRate")
        return default_list_display
    search_fields = ["Category"]

class GullyErosionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("GullyErosion")
        print default_list_display
        return default_list_display

class StreambankErosionAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("StreambankErosion")
        return default_list_display

admin.site.register(SepticSystem, SepticSystemAdmin)
admin.site.register(FeedlotAnimal, FeedlotAnimalAdmin)
admin.site.register(SoilTexture, SoilTextureAdmin)
admin.site.register(LateralRecessionRate, LateralRecessionRateAdmin)
admin.site.register(GullyErosion, GullyErosionAdmin)
admin.site.register(StreambankErosion, StreambankErosionAdmin)

class WildlifeDensityInCropLandAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("WildlifeDensityInCropLand")
        return default_list_display
    search_fields = ["Wildlife"]

class WildlifeDensityInCropLandInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("WildlifeDensityInCropLandInput")
        return default_list_display
    search_fields = ["Wildlife"]

admin.site.register(WildlifeDensityInCropLand, WildlifeDensityInCropLandAdmin)
admin.site.register(WildlifeDensityInCropLandInput, WildlifeDensityInCropLandInputAdmin)

class AnimalWeightInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("AnimalWeightInput")
        return default_list_display
    search_fields = ['Animal']

class SepticSystemInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SepticSystemInput")
        return default_list_display
    search_fields = ["Title"]

class FeedlotAnimalInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("FeedlotAnimalInput")
        return default_list_display
    search_fields = ["Animal"]

class SoilTextureInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("SoilTextureInput")
        return default_list_display

class LateralRecessionRateInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("LateralRecessionRateInput")
        return default_list_display

class GullyErosionInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("GullyErosionInput")
        return default_list_display

class StreambankErosionInputAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("StreambankErosionInput")
        return default_list_display

class UniversalSoilLossEquationAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        default_list_display = getDisplayFields("UniversalSoilLossEquation")
        return default_list_display

admin.site.register(AnimalWeightInput, AnimalWeightInputAdmin)
admin.site.register(SepticSystemInput, SepticSystemInputAdmin)
admin.site.register(FeedlotAnimalInput, FeedlotAnimalInputAdmin)
admin.site.register(SoilTextureInput, SoilTextureInputAdmin)
admin.site.register(LateralRecessionRateInput, LateralRecessionRateInputAdmin)
admin.site.register(GullyErosionInput, GullyErosionInputAdmin)
admin.site.register(StreambankErosionInput, StreambankErosionInputAdmin)
admin.site.register(UniversalSoilLossEquation, UniversalSoilLossEquationAdmin)
