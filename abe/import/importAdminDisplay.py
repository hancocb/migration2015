from django.shortcuts import render
from adminDisplayManage.models import AdminListDisplay as AdminListDisplay

import stepl.models as SM


def has_existed(className,field):
    data = AdminListDisplay.objects.all().filter(ClassName=className, FieldName=field)
    return len(data)>0    


def fieldCheck(modelClass):
    '''
        Two direction check.
        1. Class & Field name in stepl database exist in AdminDisplay
            if not, add it.
        2. item in AdminDisplay reflects a exist Class&Field name in stepl
            if not, delete this item in AdminDisplay
    '''
    # 1. Class & Field name in stepl database exist in AdminDisplay
    Log = ""
    className = modelClass.__name__
    classFields = []
    for field in modelClass._meta.get_fields():
        field = field.name
        classFields.append(className+"."+field)
        if not has_existed(className,field):
            Log += "ADD\t" + className + "\t" + field + "\n"       #show change log to screen
            AdminLD = AdminListDisplay(ClassName=className, FieldName=field, isShown=True)
            AdminLD.save()
   


    # 2. item in AdminDisplay reflects a exist Class&Field name in stepl
    AdminLDs = AdminListDisplay.objects.all().filter(ClassName=className)
    for cur in AdminLDs:
        AppClassField = cur.ClassName + "." + cur.FieldName
        # print AppClassField
        if AppClassField not in classFields:
            cur.delete()
            Log += "DEL\t" + cur.ClassName + "\t" + cur.FieldName + "\n"

    print Log


def AdminListDisplayViewModify():

    #fieldCheck(SM.AnimalWeight)
    allNames = dir(SM)
    for name in allNames:
        #those are not real models 
        if name[0].islower() or name.find("_")>-1 or name.find("Abstract")>-1:
            continue
        else:
            print "---"
            fieldCheck( getattr(SM,name) )

    print "=== finish ==="


#if __name__ == "__main__":
AdminListDisplayViewModify()
