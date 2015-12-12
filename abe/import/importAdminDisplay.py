from django.shortcuts import render
from adminDisplayManage.models import AdminListDisplay as AdminListDisplay

import stepl.models as SM


def check_exist(field):
    data = AdminListDisplay.objects.all().filter(ClassName=field[1], FieldName=field[2])
    return len(data)    # if length == 1  ==> exist;  else not exist;


def fieldCheck(allData):
    '''
        Two direction check.
        1. Class & Field name in stepl database exist in AdminDisplay
            if not, add it.
        2. item in AdminDisplay reflects a exist Class&Field name in stepl
            if not, delete this item in AdminDisplay
    '''
    # 1. Class & Field name in stepl database exist in AdminDisplay
    Log = ""
    className = ""
    allDataStr = []
    for cur in allData:
        for field in cur._meta.fields:
            field = str(field)
            allDataStr.append(field)
            field = field.split('.')
            isExist = check_exist(field)
            className = field[1]
            if isExist == 0:
                Log += "ADD\t" + field[1] + "\t" + field[2] + "\n"       #show change log to screen
                AdminLD = AdminListDisplay(ClassName=field[1], FieldName=field[2], isShown=True)
                AdminLD.save()
        break


    # 2. item in AdminDisplay reflects a exist Class&Field name in stepl
    AdminDisplayField = AdminListDisplay.objects.all().filter(ClassName=className)
    for cur in AdminDisplayField:
        AppClassField = "stepl." + cur.ClassName + "." + cur.FieldName
        # print AppClassField
        if AppClassField not in allDataStr:
            cur.delete()
            Log += "DEL\t" + cur.ClassName + "\t" + cur.FieldName + "\n"

    return Log


def AdminListDisplayViewModify():
    Log = ""

    db_get_data = SM.AnimalWeight.objects.all()
    Log += fieldCheck(db_get_data)


    db_get_data = SM.AnimalWeightInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.CountyData.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.CountyDataInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.DetailedRunoff.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.DetailedRunoffInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.FeedlotAnimal.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.FeedlotAnimalInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.GullyErosion.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.GullyErosionInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.IndexInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.Irrigation.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.IrrigationInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.LanduseDistribution.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.LanduseDistributionInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.LateralRecessionRate.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.LateralRecessionRateInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.NutrientGroundwaterRunoff.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.NutrientGroundwaterRunoffInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.NutrientRunoff.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.NutrientRunoffInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.ReferenceRunoff.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.ReferenceRunoffInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SepticSystemInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SepticSystem.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilData.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilDataInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilInfiltrationFraction.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilInfiltrationFractionInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilTexture.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.SoilTextureInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.StreambankErosion.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.StreambankErosionInput.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.UniversalSoilLossEquation.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.WatershedLandUse.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.WildlifeDensityInCropLand.objects.all()
    Log += fieldCheck(db_get_data)

    db_get_data = SM.WildlifeDensityInCropLandInput.objects.all()
    Log += fieldCheck(db_get_data)

    print "=== finish ==="
    print Log


if __name__ == "__main__":
    AdminListDisplayViewModify()
