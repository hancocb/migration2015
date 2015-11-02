#!/usr/local/bin/python
#-----------------w3c Validated-------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, 'Java' , 'Step5'

#----S input----------------------------------------------------------------------------------------------------

numWSD = 0

try:
  numWSD = int(form.getvalue('numWSD'))

except:
  numWSD = 0
#----E input----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '  <title>STEPL WEB</title>'

print '<script>'            #--------------------Java
print '  function init() {'
for i in range(1,numWSD+1) :
  tmpStr = '    document.optMain.HSG_' + str('%02i'%i) + '.value = opener.document.inputMain.HSG_' + str('%02i'%i) + '[0].value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilN_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilN_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilP_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilP_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    document.optMain.SoilB_' + str('%02i'%i) + '.value = opener.document.inputMain.SoilB_' + str('%02i'%i) + '.value ;'
  print tmpStr

#----Step6, Step6a, Step7, Step7a
print '    document.optMain.CN_urban_A.value = opener.document.inputMain.CN_urban_A.value ;'
print '    document.optMain.CN_urban_B.value = opener.document.inputMain.CN_urban_B.value ;'
print '    document.optMain.CN_urban_C.value = opener.document.inputMain.CN_urban_C.value ;'
print '    document.optMain.CN_urban_D.value = opener.document.inputMain.CN_urban_D.value ;'
print '    document.optMain.CN_crop_A.value = opener.document.inputMain.CN_crop_A.value ;'
print '    document.optMain.CN_crop_B.value = opener.document.inputMain.CN_crop_B.value ;'
print '    document.optMain.CN_crop_C.value = opener.document.inputMain.CN_crop_C.value ;'
print '    document.optMain.CN_crop_D.value = opener.document.inputMain.CN_crop_D.value ;'
print '    document.optMain.CN_past_A.value = opener.document.inputMain.CN_past_A.value ;'
print '    document.optMain.CN_past_B.value = opener.document.inputMain.CN_past_B.value ;'
print '    document.optMain.CN_past_C.value = opener.document.inputMain.CN_past_C.value ;'
print '    document.optMain.CN_past_D.value = opener.document.inputMain.CN_past_D.value ;'
print '    document.optMain.CN_frst_A.value = opener.document.inputMain.CN_frst_A.value ;'
print '    document.optMain.CN_frst_B.value = opener.document.inputMain.CN_frst_B.value ;'
print '    document.optMain.CN_frst_C.value = opener.document.inputMain.CN_frst_C.value ;'
print '    document.optMain.CN_frst_D.value = opener.document.inputMain.CN_frst_D.value ;'
print '    document.optMain.CN_user_A.value = opener.document.inputMain.CN_user_A.value ;'
print '    document.optMain.CN_user_B.value = opener.document.inputMain.CN_user_B.value ;'
print '    document.optMain.CN_user_C.value = opener.document.inputMain.CN_user_C.value ;'
print '    document.optMain.CN_user_D.value = opener.document.inputMain.CN_user_D.value ;'
print '    document.optMain.CN_wetl_A.value = opener.document.inputMain.CN_wetl_A.value ;'
print '    document.optMain.CN_wetl_B.value = opener.document.inputMain.CN_wetl_B.value ;'
print '    document.optMain.CN_wetl_C.value = opener.document.inputMain.CN_wetl_C.value ;'
print '    document.optMain.CN_wetl_D.value = opener.document.inputMain.CN_wetl_D.value ;'

print '    document.optMain.CN_comm_A.value = opener.document.inputMain.CN_comm_A.value ;'
print '    document.optMain.CN_comm_B.value = opener.document.inputMain.CN_comm_B.value ;'
print '    document.optMain.CN_comm_C.value = opener.document.inputMain.CN_comm_C.value ;'
print '    document.optMain.CN_comm_D.value = opener.document.inputMain.CN_comm_D.value ;'
print '    document.optMain.CN_indu_A.value = opener.document.inputMain.CN_indu_A.value ;'
print '    document.optMain.CN_indu_B.value = opener.document.inputMain.CN_indu_B.value ;'
print '    document.optMain.CN_indu_C.value = opener.document.inputMain.CN_indu_C.value ;'
print '    document.optMain.CN_indu_D.value = opener.document.inputMain.CN_indu_D.value ;'
print '    document.optMain.CN_inst_A.value = opener.document.inputMain.CN_inst_A.value ;'
print '    document.optMain.CN_inst_B.value = opener.document.inputMain.CN_inst_B.value ;'
print '    document.optMain.CN_inst_C.value = opener.document.inputMain.CN_inst_C.value ;'
print '    document.optMain.CN_inst_D.value = opener.document.inputMain.CN_inst_D.value ;'
print '    document.optMain.CN_tran_A.value = opener.document.inputMain.CN_tran_A.value ;'
print '    document.optMain.CN_tran_B.value = opener.document.inputMain.CN_tran_B.value ;'
print '    document.optMain.CN_tran_C.value = opener.document.inputMain.CN_tran_C.value ;'
print '    document.optMain.CN_tran_D.value = opener.document.inputMain.CN_tran_D.value ;'
print '    document.optMain.CN_mult_A.value = opener.document.inputMain.CN_mult_A.value ;'
print '    document.optMain.CN_mult_B.value = opener.document.inputMain.CN_mult_B.value ;'
print '    document.optMain.CN_mult_C.value = opener.document.inputMain.CN_mult_C.value ;'
print '    document.optMain.CN_mult_D.value = opener.document.inputMain.CN_mult_D.value ;'
print '    document.optMain.CN_sing_A.value = opener.document.inputMain.CN_sing_A.value ;'
print '    document.optMain.CN_sing_B.value = opener.document.inputMain.CN_sing_B.value ;'
print '    document.optMain.CN_sing_C.value = opener.document.inputMain.CN_sing_C.value ;'
print '    document.optMain.CN_sing_D.value = opener.document.inputMain.CN_sing_D.value ;'
print '    document.optMain.CN_urcu_A.value = opener.document.inputMain.CN_urcu_A.value ;'
print '    document.optMain.CN_urcu_B.value = opener.document.inputMain.CN_urcu_B.value ;'
print '    document.optMain.CN_urcu_C.value = opener.document.inputMain.CN_urcu_C.value ;'
print '    document.optMain.CN_urcu_D.value = opener.document.inputMain.CN_urcu_D.value ;'
print '    document.optMain.CN_vade_A.value = opener.document.inputMain.CN_vade_A.value ;'
print '    document.optMain.CN_vade_B.value = opener.document.inputMain.CN_vade_B.value ;'
print '    document.optMain.CN_vade_C.value = opener.document.inputMain.CN_vade_C.value ;'
print '    document.optMain.CN_vade_D.value = opener.document.inputMain.CN_vade_D.value ;'
print '    document.optMain.CN_open_A.value = opener.document.inputMain.CN_open_A.value ;'
print '    document.optMain.CN_open_B.value = opener.document.inputMain.CN_open_B.value ;'
print '    document.optMain.CN_open_C.value = opener.document.inputMain.CN_open_C.value ;'
print '    document.optMain.CN_open_D.value = opener.document.inputMain.CN_open_D.value ;'

print '    document.optMain.ntLcrop_1_N.value = opener.document.inputMain.ntLcrop_1_N.value ;'
print '    document.optMain.ntLcrop_1_P.value = opener.document.inputMain.ntLcrop_1_P.value ;'
print '    document.optMain.ntLcrop_1_B.value = opener.document.inputMain.ntLcrop_1_B.value ;'
print '    document.optMain.ntLcrop_2_N.value = opener.document.inputMain.ntLcrop_2_N.value ;'
print '    document.optMain.ntLcrop_2_P.value = opener.document.inputMain.ntLcrop_2_P.value ;'
print '    document.optMain.ntLcrop_2_B.value = opener.document.inputMain.ntLcrop_2_B.value ;'
print '    document.optMain.ntMcrop_1_N.value = opener.document.inputMain.ntMcrop_1_N.value ;'
print '    document.optMain.ntMcrop_1_P.value = opener.document.inputMain.ntMcrop_1_P.value ;'
print '    document.optMain.ntMcrop_1_B.value = opener.document.inputMain.ntMcrop_1_B.value ;'
print '    document.optMain.ntMcrop_2_N.value = opener.document.inputMain.ntMcrop_2_N.value ;'
print '    document.optMain.ntMcrop_2_P.value = opener.document.inputMain.ntMcrop_2_P.value ;'
print '    document.optMain.ntMcrop_2_B.value = opener.document.inputMain.ntMcrop_2_B.value ;'
print '    document.optMain.ntHcrop_1_N.value = opener.document.inputMain.ntHcrop_1_N.value ;'
print '    document.optMain.ntHcrop_1_P.value = opener.document.inputMain.ntHcrop_1_P.value ;'
print '    document.optMain.ntHcrop_1_B.value = opener.document.inputMain.ntHcrop_1_B.value ;'
print '    document.optMain.ntHcrop_2_N.value = opener.document.inputMain.ntHcrop_2_N.value ;'
print '    document.optMain.ntHcrop_2_P.value = opener.document.inputMain.ntHcrop_2_P.value ;'
print '    document.optMain.ntHcrop_2_B.value = opener.document.inputMain.ntHcrop_2_B.value ;'
print '    document.optMain.ntPast_N.value = opener.document.inputMain.ntPast_N.value ;'
print '    document.optMain.ntPast_P.value = opener.document.inputMain.ntPast_P.value ;'
print '    document.optMain.ntPast_B.value = opener.document.inputMain.ntPast_B.value ;'
print '    document.optMain.ntFrst_N.value = opener.document.inputMain.ntFrst_N.value ;'
print '    document.optMain.ntFrst_P.value = opener.document.inputMain.ntFrst_P.value ;'
print '    document.optMain.ntFrst_B.value = opener.document.inputMain.ntFrst_B.value ;'
print '    document.optMain.ntWetl_N.value = opener.document.inputMain.ntWetl_N.value ;'
print '    document.optMain.ntWetl_P.value = opener.document.inputMain.ntWetl_P.value ;'
print '    document.optMain.ntWetl_B.value = opener.document.inputMain.ntWetl_B.value ;'
print '    document.optMain.ntUser_N.value = opener.document.inputMain.ntUser_N.value ;'
print '    document.optMain.ntUser_P.value = opener.document.inputMain.ntUser_P.value ;'
print '    document.optMain.ntUser_B.value = opener.document.inputMain.ntUser_B.value ;'

print '    document.optMain.GntUrbn_N.value = opener.document.inputMain.GntUrbn_N.value ;'
print '    document.optMain.GntUrbn_P.value = opener.document.inputMain.GntUrbn_P.value ;'
print '    document.optMain.GntUrbn_B.value = opener.document.inputMain.GntUrbn_B.value ;'
print '    document.optMain.GntCrop_N.value = opener.document.inputMain.GntCrop_N.value ;'
print '    document.optMain.GntCrop_P.value = opener.document.inputMain.GntCrop_P.value ;'
print '    document.optMain.GntCrop_B.value = opener.document.inputMain.GntCrop_B.value ;'
print '    document.optMain.GntPast_N.value = opener.document.inputMain.GntPast_N.value ;'
print '    document.optMain.GntPast_P.value = opener.document.inputMain.GntPast_P.value ;'
print '    document.optMain.GntPast_B.value = opener.document.inputMain.GntPast_B.value ;'
print '    document.optMain.GntFrst_N.value = opener.document.inputMain.GntFrst_N.value ;'
print '    document.optMain.GntFrst_P.value = opener.document.inputMain.GntFrst_P.value ;'
print '    document.optMain.GntFrst_B.value = opener.document.inputMain.GntFrst_B.value ;'
print '    document.optMain.GntWetl_N.value = opener.document.inputMain.GntWetl_N.value ;'
print '    document.optMain.GntWetl_P.value = opener.document.inputMain.GntWetl_P.value ;'
print '    document.optMain.GntWetl_B.value = opener.document.inputMain.GntWetl_B.value ;'
print '    document.optMain.GntFeed_N.value = opener.document.inputMain.GntFeed_N.value ;'
print '    document.optMain.GntFeed_P.value = opener.document.inputMain.GntFeed_P.value ;'
print '    document.optMain.GntFeed_B.value = opener.document.inputMain.GntFeed_B.value ;'
print '    document.optMain.GntUser_N.value = opener.document.inputMain.GntUser_N.value ;'
print '    document.optMain.GntUser_P.value = opener.document.inputMain.GntUser_P.value ;'
print '    document.optMain.GntUser_B.value = opener.document.inputMain.GntUser_B.value ;'

#----Step8
for i in range(1,numWSD+1) :
  for j in range(1,10) :
    tmpStr = '    document.optMain.dist_' + str(j) + str('%02i'%i) + '.value = opener.document.inputMain.dist_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step9
for i in range(1,numWSD+1) :
  for j in range(1,5) :
    tmpStr = '    document.optMain.IrrVal_' + str(j) + str('%02i'%i) + '.value = opener.document.inputMain.IrrVal_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step8,9  Total Area
for i in range(1,numWSD+1) :
  tmpStr = '    document.optMain.UrbanArea_' + str('%02i'%i) + '.value = opener.document.inputMain.LuseAreaWSD_1' + str('%02i'%i) + '.value ;' 
  print tmpStr
  tmpStr = '    document.optMain.CropTotArea_' + str('%02i'%i) + '.value = opener.document.inputMain.LuseAreaWSD_2' + str('%02i'%i) + '.value ;'
  print tmpStr

print '  }'       # init

#----Step8, UrbanTotal
for i in range(1,numWSD+1) :
  tmpStr = '  function UrbanTotal_' + str('%02i'%i) + '() {'
  print tmpStr
  for j in range(1,10) :
    tmpStr = '    var area' + str(j) + ' = document.optMain.dist_' + str(j) + str('%02i'%i) + '.value * 1.0 ;'
    print tmpStr
  print '    var totArea = area1 + area2 + area3 + area4 + area5 + area6 + area7 + area8 + area9 ;' 
  tmpStr = '    document.optMain.TotalUrban_' + str('%02i'%i) + '.value = totArea ;'
  print tmpStr
  print '}'       # Urban Total

#----returnVal
print '  function returnVal() {'
#----Step5
for i in range(1,numWSD+1) :
  tmpStr = '    opener.document.inputMain.HSG_' + str('%02i'%i) + '[0].value = document.optMain.HSG_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilN_' + str('%02i'%i) + '.value = document.optMain.SoilN_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilP_' + str('%02i'%i) + '.value = document.optMain.SoilP_' + str('%02i'%i) + '.value ;'
  print tmpStr
  tmpStr = '    opener.document.inputMain.SoilB_' + str('%02i'%i) + '.value = document.optMain.SoilB_' + str('%02i'%i) + '.value '; 
  print tmpStr

#----Step6, Step6a, Step7, Step7a
print '    opener.document.inputMain.CN_urban_A.value = document.optMain.CN_urban_A.value ;'
print '    opener.document.inputMain.CN_urban_B.value = document.optMain.CN_urban_B.value ;'
print '    opener.document.inputMain.CN_urban_C.value = document.optMain.CN_urban_C.value ;'
print '    opener.document.inputMain.CN_urban_D.value = document.optMain.CN_urban_D.value ;'
print '    opener.document.inputMain.CN_crop_A.value = document.optMain.CN_crop_A.value ;'
print '    opener.document.inputMain.CN_crop_B.value = document.optMain.CN_crop_B.value ;'
print '    opener.document.inputMain.CN_crop_C.value = document.optMain.CN_crop_C.value ;'
print '    opener.document.inputMain.CN_crop_D.value = document.optMain.CN_crop_D.value ;'
print '    opener.document.inputMain.CN_past_A.value = document.optMain.CN_past_A.value ;'
print '    opener.document.inputMain.CN_past_B.value = document.optMain.CN_past_B.value ;'
print '    opener.document.inputMain.CN_past_C.value = document.optMain.CN_past_C.value ;'
print '    opener.document.inputMain.CN_past_D.value = document.optMain.CN_past_D.value ;'
print '    opener.document.inputMain.CN_frst_A.value = document.optMain.CN_frst_A.value ;'
print '    opener.document.inputMain.CN_frst_B.value = document.optMain.CN_frst_B.value ;'
print '    opener.document.inputMain.CN_frst_C.value = document.optMain.CN_frst_C.value ;'
print '    opener.document.inputMain.CN_frst_D.value = document.optMain.CN_frst_D.value ;'
print '    opener.document.inputMain.CN_wetl_A.value = document.optMain.CN_wetl_A.value ;'
print '    opener.document.inputMain.CN_wetl_B.value = document.optMain.CN_wetl_B.value ;'
print '    opener.document.inputMain.CN_wetl_C.value = document.optMain.CN_wetl_C.value ;'
print '    opener.document.inputMain.CN_wetl_D.value = document.optMain.CN_wetl_D.value ;'
print '    opener.document.inputMain.CN_user_A.value = document.optMain.CN_user_A.value ;'
print '    opener.document.inputMain.CN_user_B.value = document.optMain.CN_user_B.value ;'
print '    opener.document.inputMain.CN_user_C.value = document.optMain.CN_user_C.value ;'
print '    opener.document.inputMain.CN_user_D.value = document.optMain.CN_user_D.value ;'

print '    opener.document.inputMain.CN_comm_A.value = document.optMain.CN_comm_A.value ;'
print '    opener.document.inputMain.CN_comm_B.value = document.optMain.CN_comm_B.value ;'
print '    opener.document.inputMain.CN_comm_C.value = document.optMain.CN_comm_C.value ;'
print '    opener.document.inputMain.CN_comm_D.value = document.optMain.CN_comm_D.value ;'
print '    opener.document.inputMain.CN_indu_A.value = document.optMain.CN_indu_A.value ;'
print '    opener.document.inputMain.CN_indu_B.value = document.optMain.CN_indu_B.value ;'
print '    opener.document.inputMain.CN_indu_C.value = document.optMain.CN_indu_C.value ;'
print '    opener.document.inputMain.CN_indu_D.value = document.optMain.CN_indu_D.value ;'
print '    opener.document.inputMain.CN_inst_A.value = document.optMain.CN_inst_A.value ;'
print '    opener.document.inputMain.CN_inst_B.value = document.optMain.CN_inst_B.value ;'
print '    opener.document.inputMain.CN_inst_C.value = document.optMain.CN_inst_C.value ;'
print '    opener.document.inputMain.CN_inst_D.value = document.optMain.CN_inst_D.value ;'
print '    opener.document.inputMain.CN_tran_A.value = document.optMain.CN_tran_A.value ;'
print '    opener.document.inputMain.CN_tran_B.value = document.optMain.CN_tran_B.value ;'
print '    opener.document.inputMain.CN_tran_C.value = document.optMain.CN_tran_C.value ;'
print '    opener.document.inputMain.CN_tran_D.value = document.optMain.CN_tran_D.value ;'
print '    opener.document.inputMain.CN_mult_A.value = document.optMain.CN_mult_A.value ;'
print '    opener.document.inputMain.CN_mult_B.value = document.optMain.CN_mult_B.value ;'
print '    opener.document.inputMain.CN_mult_C.value = document.optMain.CN_mult_C.value ;'
print '    opener.document.inputMain.CN_mult_D.value = document.optMain.CN_mult_D.value ;'
print '    opener.document.inputMain.CN_sing_A.value = document.optMain.CN_sing_A.value ;'
print '    opener.document.inputMain.CN_sing_B.value = document.optMain.CN_sing_B.value ;'
print '    opener.document.inputMain.CN_sing_C.value = document.optMain.CN_sing_C.value ;'
print '    opener.document.inputMain.CN_sing_D.value = document.optMain.CN_sing_D.value ;'
print '    opener.document.inputMain.CN_urcu_A.value = document.optMain.CN_urcu_A.value ;'
print '    opener.document.inputMain.CN_urcu_B.value = document.optMain.CN_urcu_B.value ;'
print '    opener.document.inputMain.CN_urcu_C.value = document.optMain.CN_urcu_C.value ;'
print '    opener.document.inputMain.CN_urcu_D.value = document.optMain.CN_urcu_D.value ;'
print '    opener.document.inputMain.CN_vade_A.value = document.optMain.CN_vade_A.value ;'
print '    opener.document.inputMain.CN_vade_B.value = document.optMain.CN_vade_B.value ;'
print '    opener.document.inputMain.CN_vade_C.value = document.optMain.CN_vade_C.value ;'
print '    opener.document.inputMain.CN_vade_D.value = document.optMain.CN_vade_D.value ;'
print '    opener.document.inputMain.CN_open_A.value = document.optMain.CN_open_A.value ;'
print '    opener.document.inputMain.CN_open_B.value = document.optMain.CN_open_B.value ;'
print '    opener.document.inputMain.CN_open_C.value = document.optMain.CN_open_C.value ;'
print '    opener.document.inputMain.CN_open_D.value = document.optMain.CN_open_D.value ;'

print '    opener.document.inputMain.ntLcrop_1_N.value = document.optMain.ntLcrop_1_N.value ;'
print '    opener.document.inputMain.ntLcrop_1_P.value = document.optMain.ntLcrop_1_P.value ;'
print '    opener.document.inputMain.ntLcrop_1_B.value = document.optMain.ntLcrop_1_B.value ;'
print '    opener.document.inputMain.ntLcrop_2_N.value = document.optMain.ntLcrop_2_N.value ;'
print '    opener.document.inputMain.ntLcrop_2_P.value = document.optMain.ntLcrop_2_P.value ;'
print '    opener.document.inputMain.ntLcrop_2_B.value = document.optMain.ntLcrop_2_B.value ;'
print '    opener.document.inputMain.ntMcrop_1_N.value = document.optMain.ntMcrop_1_N.value ;'
print '    opener.document.inputMain.ntMcrop_1_P.value = document.optMain.ntMcrop_1_P.value ;'
print '    opener.document.inputMain.ntMcrop_1_B.value = document.optMain.ntMcrop_1_B.value ;'
print '    opener.document.inputMain.ntMcrop_2_N.value = document.optMain.ntMcrop_2_N.value ;'
print '    opener.document.inputMain.ntMcrop_2_P.value = document.optMain.ntMcrop_2_P.value ;'
print '    opener.document.inputMain.ntMcrop_2_B.value = document.optMain.ntMcrop_2_B.value ;'
print '    opener.document.inputMain.ntHcrop_1_N.value = document.optMain.ntHcrop_1_N.value ;'
print '    opener.document.inputMain.ntHcrop_1_P.value = document.optMain.ntHcrop_1_P.value ;'
print '    opener.document.inputMain.ntHcrop_1_B.value = document.optMain.ntHcrop_1_B.value ;'
print '    opener.document.inputMain.ntHcrop_2_N.value = document.optMain.ntHcrop_2_N.value ;'
print '    opener.document.inputMain.ntHcrop_2_P.value = document.optMain.ntHcrop_2_P.value ;'
print '    opener.document.inputMain.ntHcrop_2_B.value = document.optMain.ntHcrop_2_B.value ;'
print '    opener.document.inputMain.ntPast_N.value = document.optMain.ntPast_N.value ;'
print '    opener.document.inputMain.ntPast_P.value = document.optMain.ntPast_P.value ;'
print '    opener.document.inputMain.ntPast_B.value = document.optMain.ntPast_B.value ;'
print '    opener.document.inputMain.ntFrst_N.value = document.optMain.ntFrst_N.value ;'
print '    opener.document.inputMain.ntFrst_P.value = document.optMain.ntFrst_P.value ;'
print '    opener.document.inputMain.ntFrst_B.value = document.optMain.ntFrst_B.value ;'
print '    opener.document.inputMain.ntWetl_N.value = document.optMain.ntWetl_N.value ;'
print '    opener.document.inputMain.ntWetl_P.value = document.optMain.ntWetl_P.value ;'
print '    opener.document.inputMain.ntWetl_B.value = document.optMain.ntWetl_B.value ;'
print '    opener.document.inputMain.ntUser_N.value = document.optMain.ntUser_N.value ;'
print '    opener.document.inputMain.ntUser_P.value = document.optMain.ntUser_P.value ;'
print '    opener.document.inputMain.ntUser_B.value = document.optMain.ntUser_B.value ;'

print '    opener.document.inputMain.GntUrbn_N.value = document.optMain.GntUrbn_N.value ;'
print '    opener.document.inputMain.GntUrbn_P.value = document.optMain.GntUrbn_P.value ;'
print '    opener.document.inputMain.GntUrbn_B.value = document.optMain.GntUrbn_B.value ;'
print '    opener.document.inputMain.GntCrop_N.value = document.optMain.GntCrop_N.value ;'
print '    opener.document.inputMain.GntCrop_P.value = document.optMain.GntCrop_P.value ;'
print '    opener.document.inputMain.GntCrop_B.value = document.optMain.GntCrop_B.value ;'
print '    opener.document.inputMain.GntPast_N.value = document.optMain.GntPast_N.value ;'
print '    opener.document.inputMain.GntPast_P.value = document.optMain.GntPast_P.value ;'
print '    opener.document.inputMain.GntPast_B.value = document.optMain.GntPast_B.value ;'
print '    opener.document.inputMain.GntFrst_N.value = document.optMain.GntFrst_N.value ;'
print '    opener.document.inputMain.GntFrst_P.value = document.optMain.GntFrst_P.value ;'
print '    opener.document.inputMain.GntFrst_B.value = document.optMain.GntFrst_B.value ;'
print '    opener.document.inputMain.GntWetl_N.value = document.optMain.GntWetl_N.value ;'
print '    opener.document.inputMain.GntWetl_P.value = document.optMain.GntWetl_P.value ;'
print '    opener.document.inputMain.GntWetl_B.value = document.optMain.GntWetl_B.value ;'
print '    opener.document.inputMain.GntFeed_N.value = document.optMain.GntFeed_N.value ;'
print '    opener.document.inputMain.GntFeed_P.value = document.optMain.GntFeed_P.value ;'
print '    opener.document.inputMain.GntFeed_B.value = document.optMain.GntFeed_B.value ;'
print '    opener.document.inputMain.GntUser_N.value = document.optMain.GntUser_N.value ;'
print '    opener.document.inputMain.GntUser_P.value = document.optMain.GntUser_P.value ;'
print '    opener.document.inputMain.GntUser_B.value = document.optMain.GntUser_B.value ;'

#----Step8
for i in range(1,numWSD+1) :
  for j in range(1,10) :
    tmpStr = '    opener.document.inputMain.dist_' + str(j) + str('%02i'%i) + '.value = document.optMain.dist_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

#----Step9
for i in range(1,numWSD+1) :
  for j in range(1,5) :
    tmpStr = '    opener.document.inputMain.IrrVal_' + str(j) + str('%02i'%i) + '.value = document.optMain.IrrVal_' + str(j) + str('%02i'%i) + '.value ;'
    print tmpStr

print '  alert("Updated") ;'
print '  self.close();'
print '  }'       # returnVal
print '</script>'

print '</head>'
print '<body onLoad="init()"> '
print '<form name=optMain><br>'

#----Step5
print '  <hr> <div style = "color:blue; font-weight: bold;">Step 5. Select average soil hydrologic group (SHG), SHG A = highest infiltration and SHG D = lowest infiltration </div>'

print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Watershed</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Soil N Conc. %</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Soil P Conc. %</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Soil BOD Conc. %</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">W', i,'</td>'
  tmpStr = '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><select name=HSG_' + str('%02i'%i) + '><option value="1">A<option value="2">B<option value="3">C<option value="4">D</select></td>'
  print tmpStr
  tmpStr = '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilN_' + str('%02i'%i) + ' value=0.080></td>' 
  print tmpStr
  tmpStr = '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilP_' + str('%02i'%i) + ' value=0.080></td>'
  print tmpStr
  tmpStr = '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=SoilB_' + str('%02i'%i) + ' value=0.080></td>'
  print tmpStr
  print '  </tr>'
print '</table>'

#----Step6
print '  <hr><div style = "color:blue; font-weight: bold;">Step 6. Reference runoff curve number</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Landuse</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG A</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG B</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG C</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG D</td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_A value=83></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_B value=89></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_C value=92></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urban_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Cropland</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_A value=67></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_B value=78></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_C value=85></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_crop_D value=89></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Pastureland</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_A value=49></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_B value=69></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_C value=79></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_past_D value=84></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Forest</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_A value=39></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_B value=60></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_C value=73></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_frst_D value=79></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">User Defined</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_A value=50></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_B value=70></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_C value=80></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_D value=85></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Water</td>'

print '      <td style = "text-align:right; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><span style="text-align:right;border-width:0px;font-size:9pt">0</span></td>'
print '      <td style = "text-align:right; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><span style="text-align:right;border-width:0px;font-size:9pt">0</span></td>'
print '      <td style = "text-align:right; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><span style="text-align:right;border-width:0px;font-size:9pt">0</span></td>'
print '      <td style = "text-align:right; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><span style="text-align:right;border-width:0px;font-size:9pt">0</span></td>'
#print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_A value=0></td>'
#print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_B value=0></td>'
#print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_C value=0></td>'
#print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_user_D value=0></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Wetlands</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_wetl_A value=77></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_wetl_B value=77></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_wetl_C value=84></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_wetl_D value=90></td>'
print '    </tr>'
print '  </table>'


#----Step6a
print '  <hr><div style = "color:blue; font-weight: bold;">Step 6a. Detailed urban reference runoff curve number</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG A</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG B</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG C</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">SHG D</td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Commercial</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_A value=89></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_B value=92></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_C value=94></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_comm_D value=95></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Industrial</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_indu_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Institutional</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_inst_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Transportation</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_tran_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Multi-Family</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_mult_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Single-Family</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_sing_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban-Cultivated</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_urcu_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Vacant-Developed</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_vade_D value=93></td>'
print '    </tr>'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Open Space</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_A value=81></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_B value=88></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_C value=91></td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CN_open_D value=93></td>'
print '    </tr>'
print '  </table>'


#----Step7
print '  <hr><div style = "color:blue; font-weight: bold;">7. Nutrient concentration in runoff (mg/l)</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Landuse</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">N</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">P</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">BOD</td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">L-Cropland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_N value=1.9></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_P value=0.3></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_1_B value=4.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">L-Cropland w/ manure</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_N value=8.1></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_P value=2.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntLcrop_2_B value=12.3></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">M-Cropland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_N value=2.9></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_P value=0.4></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_1_B value=6.1></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">M-Cropland w/ manure</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_N value=12.2></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_P value=3.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntMcrop_2_B value=18.5></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">H-Cropland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_N value=4.4></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_P value=0.5></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_1_B value=9.2></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">H-Cropland w/ manure</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_N value=18.3></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_P value=4.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntHcrop_2_B value=24.6></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Pastureland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_N value=4.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_P value=0.3></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntPast_B value=13.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Forest</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_N value=0.2></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_P value=0.1></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntFrst_B value=0.5></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Wetlands</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntWetl_N value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntWetl_P value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntWetl_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">User Defined</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_N value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_P value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=ntUser_B value=0.0></td>'
print '        </tr>'
print '  </table>'


#----Step7a
print '  <hr><div style = "color:blue; font-weight: bold;">7a. Nutrient concentration in shallow groundwater (mg/l)</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Landuse</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">N</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">P</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">BOD</td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_N value=1.5></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_P value=0.063></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUrbn_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Cropland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_N value=1.44></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_P value=0.063></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntCrop_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Pastureland</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_N value=1.44></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_P value=0.063></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntPast_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Forest</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_N value=0.11></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_P value=0.009></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFrst_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Wetlands</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntWetl_N value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntWetl_P value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntWetl_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Feedlot</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_N value=6.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_P value=0.007></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntFeed_B value=0.0></td>'
print '        </tr>'
print '        <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">User-Defined</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_N value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_P value=0.0></td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=GntUser_B value=0.0></td>'
print '        </tr>'
print '  </table>'


#----Step8
print '  <hr><div style = "color:blue; font-weight: bold;">8. Input or modify urban land use distribution</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Watershed</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban Area (ac)</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Commercial %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Industrial %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Institutional %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Transportation %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Multi-Family %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Single-Family %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Urban-Cultivated %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Vacant (developed) %</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Open Space %</td>'
print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Total % Area</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">W', i,'</td>'
  tmpStr = '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=UrbanArea_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  for j in range(1,10) :
    print '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">'
    tmpStr = '    <input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=dist_' + str(j) + str('%02i'%i)
    tmpStr = tmpStr + ' onChange="javascript:UrbanTotal_' + str('%02i'%i) + '()" value=0.0></td>'
    print tmpStr
  tmpStr = '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=TotalUrban_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  print '  </tr>'
print '  </table>'


#----Step9
print '  <hr><div style = "color:blue; font-weight: bold;">9. Input irrigation area (ac) and irrigation amount (in)</div>'
print '  <table style="border:1px solid black; margin: 0 auto;">'
print '    <tr>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Watershed</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Total Cropland (ac)</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Cropland: Acres Irrigated</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Water Depth (in) per Irrigation - Before BMP</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Water Depth (in) per Irrigation - After BMP</td>'
print '          <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">Irrigation Frequency (#/Year)</td>'
print '        </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  print '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">W',i,'</td>'
  tmpStr = '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=CropTotArea_' + str('%02i'%i) + ' readonly></td>'
  print tmpStr
  for j in range(1,5) :
    tmpStr = '    <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;">'
    tmpStr = tmpStr + '<input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 name=IrrVal_' + str(j) + str('%02i'%i) + ' value=0></td>' 
    print tmpStr
  print '  </tr>'
print '  </table>'

print '  <br><br>'
print '  <div style="text-align:center;" ><input style="WIDTH:200px;height:30px;CURSOR:hand" type=button value="Update" onClick="javascript:returnVal()"></div><br><br>'


print '</form>'
print '</body>'



print '</html>'















