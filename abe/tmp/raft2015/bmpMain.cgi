#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, find 'Table1', 'Table2',...
# to jump, find 'BMPinputs', 'ubForm', 'JavaScript'

#----S input----------------------------------------------------------------------------------------------------
ystimeldc = str(form.getvalue('ystimeldc'))
allPct = str(form.getvalue('allPct'))

numWSD = int(form.getvalue('numWSD'))
numGLY = int(form.getvalue('numGLY'))
numSTR = int(form.getvalue('numSTR'))
ystime = str(form.getvalue('ystime'))
status = int(form.getvalue('status'))
numWSD = numWSD + 1               # loop starts at 1 not 0
path = './tmp/' + ystime + '/'

#print numWSD, numGLY, numSTR, ystime, status

#----------------------------------------------------------------------------------Table1
swsOpt = form.getvalue('swsOpt')
if ( swsOpt == 'on' or swsOpt == 'chcecked' ) :
  swsOpt = 1 
else :
  swsOpt = 4
LuseAreaWSD = [0.0] * 7
for i in range(1,len(LuseAreaWSD)) :                              # i = row(1-6), j = wsd num(1-10)
  LuseAreaWSD[i] = [0.0] * numWSD
  for j in range(1,len(LuseAreaWSD[i])) :
    tmpVal = form.getvalue('LuseAreaWSD_' + str(i) + str('%02i' % int(j)))
    tmpVal = str(tmpVal)
    if ( tmpVal == 'None' or tmpVal == '' ) :
      LuseAreaWSD[i][j] = 0.0
    else :
      LuseAreaWSD[i][j] = float(tmpVal)
TAreaWSD = [0.0] * numWSD
PctFeedlot = [0.0] * numWSD 
for i in range(1,len(TAreaWSD)) :
  tmpVal = str(form.getvalue('TAreaWSD_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    TAreaWSD[i] = 0.0
  else :
    TAreaWSD[i] = float(tmpVal)
  tmpVal = str(form.getvalue('PctFeedlot_' + str('%02i'%i)))
  PctFeedlot[i] = float(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', LuseAreaWSD[1][i], '-', LuseAreaWSD[2][i], '-', LuseAreaWSD[3][i], '-', LuseAreaWSD[4][i], '-', LuseAreaWSD[5][i], '-', LuseAreaWSD[6][i], '=', TAreaWSD[i]
#print '<hr>'
#for i in range(1,numWSD) :
#  print '<li>', PctFeedlot[i]

#----------------------------------------------------------------------------------Table2
Anm = [0.0] * 10
for i in range(1,10) :
  Anm[i] = [0.0] * numWSD 
  for j in range(1,numWSD) :
    tmpVal = str(form.getvalue('Animals_' + str(i) + str('%02i' % int(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Anm[i][j] = 0.0
    else :
      Anm[i][j] = float(tmpVal)
for i in range(1,numWSD) :
  tmpVal = str(form.getvalue('NumMonManure_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    Anm[9][i] = 0.0
  else :
    Anm[9][i] = float(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', Anm[1][i], '-', Anm[2][i], '-', Anm[3][i], '-', Anm[4][i], '-', Anm[5][i], '-', Anm[6][i], '-', Anm[7][i], '-', Anm[8][i], '-', Anm[9][i]

#----------------------------------------------------------------------------------Table3
NumSpSys = [0.0] * numWSD
PpSpSys = [0.0] * numWSD 
SpFailRate = [0.0] * numWSD 
NumPpDrtDc = [0.0] * numWSD 
RdcDrtDc = [0.0] * numWSD 
for i in range(1,len(NumSpSys)) :
  tmpVal = str(form.getvalue('NumSpSys_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    NumSpSys[i] = 0.0
  else :
    NumSpSys[i] = float(tmpVal)
  tmpVal = str(form.getvalue('PpSpSys_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    PpSpSys[i] = 0.0
  else :
    PpSpSys[i] = float(tmpVal)
  tmpVal = str(form.getvalue('SpFailRate_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    SpFailRate[i] = 0.0
  else :
    SpFailRate[i] = float(tmpVal)
  tmpVal = str(form.getvalue('NumPpDrtDc_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    NumPpDrtDc[i] = 0.0
  else :
    NumPpDrtDc[i] = float(tmpVal)
  tmpVal = str(form.getvalue('RdcDrtDc_' + str('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    RdcDrtDc[i] = 0.0
  else :
    RdcDrtDc[i] = float(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', NumSpSys[i], PpSpSys[i], SpFailRate[i], NumPpDrtDc[i], RdcDrtDc[i]

#----------------------------------------------------------------------------------Table4
usleCropland = [0.0] * 6
uslePasture = [0.0] * 6
usleForest = [0.0] * 6
usleUser = [0.0] * 6
for i in range(1,len(usleUser)) :
  usleCropland[i] = [0.0] * numWSD
  uslePasture[i] = [0.0] * numWSD 
  usleForest[i] = [0.0] * numWSD 
  usleUser[i] = [0.0] * numWSD 
  for j in range(1,len(usleUser[i])) :
    tmpVal_1 = str(form.getvalue('usleCropland_' + str(i) + str('%02i' % int(j))))
    tmpVal_2 = str(form.getvalue('uslePasture_' + str(i) + str('%02i' % int(j))))
    tmpVal_3 = str(form.getvalue('usleForest_' + str(i) + str('%02i' % int(j))))
    tmpVal_4 = str(form.getvalue('usleUser_' + str(i) + str('%02i' % int(j))))
    if ( tmpVal_1 == 'None' or tmpVal_1 == '' ) :
      usleCropland[i][j] = 0.0
    else :
      usleCropland[i][j] = float(tmpVal_1)
    if ( tmpVal_2 == 'None' or tmpVal_2 == '' ) :
      uslePasture[i][j] = 0.0
    else :
      uslePasture[i][j] = float(tmpVal_2)
    if ( tmpVal_3 == 'None' or tmpVal_3 == '' ) :
      usleForest[i][j] = 0.0
    else :
      usleForest[i][j] = float(tmpVal_3)
    if ( tmpVal_4 == 'None' or tmpVal_4 == '' ) :
      usleUser[i][j] = 0.0
    else :
      usleUser[i][j] = float(tmpVal_4)

#for i in range(1,numWSD) :
#  print '<li>', usleCropland[1][i], '-', usleCropland[2][i], '-', usleCropland[3][i], '-', usleCropland[4][i], '-', usleCropland[5][i]
#  print '<li>', uslePasture[1][i], '-', uslePasture[2][i], '-', uslePasture[3][i], '-', uslePasture[4][i], '-', uslePasture[5][i]
#  print '<li>', usleForest[1][i], '-', usleForest[2][i], '-', usleForest[3][i], '-', usleForest[4][i], '-', usleForest[5][i]
#  print '<li>', usleUser[1][i], '-', usleUser[2][i], '-', usleUser[3][i], '-', usleUser[4][i], '-', usleUser[5][i]

#----------------------------------------------------------------------------------Table5
HSG = [0] * numWSD 
SoilN = [0.0] * numWSD 
SoilP = [0.0] * numWSD 
SoilB = [0.0] * numWSD 
for i in range(1,len(HSG)) :
  tmpVal_1 = str(form.getvalue('HSG_' + str('%02i'%i)))
  tmpVal_2 = str(form.getvalue('SoilN_' + str('%02i'%i)))
  tmpVal_3 = str(form.getvalue('SoilP_' + str('%02i'%i)))
  tmpVal_4 = str(form.getvalue('SoilB_' + str('%02i'%i)))
  if ( tmpVal_1 == 'None' or tmpVal_1 == '' ) :
    HSG[i] = int(0)
  else :
    HSG[i] = int(tmpVal_1)
  if ( tmpVal_2 == 'None' or tmpVal_2 == '' ) :
    SoilN[i] = float(0)
  else :
    SoilN[i] = float(tmpVal_2)
  if ( tmpVal_3 == 'None' or tmpVal_3 == '' ) :
    SoilP[i] = float(0)
  else :
    SoilP[i] = float(tmpVal_3)
  if ( tmpVal_4 == 'None' or tmpVal_4 == '' ) :
    SoilB[i] = float(0)
  else :
    SoilB[i] = float(tmpVal_4)

#for i in range(1,numWSD) :
#  print '<li>', HSG[i], SoilN[i], SoilP[i], SoilB[i]

#----------------------------------------------------------------------------------Table6
CN = [0.0] * 6                                                                  # CN : general CN
for i in range(len(CN)) :
  CN[i] = [0.0] * 5

CN[1][1] = float(form.getvalue('CN_urban_A'))
CN[1][2] = float(form.getvalue('CN_urban_B'))
CN[1][3] = float(form.getvalue('CN_urban_C'))
CN[1][4] = float(form.getvalue('CN_urban_D'))
CN[2][1] = float(form.getvalue('CN_crop_A'))
CN[2][2] = float(form.getvalue('CN_crop_B'))
CN[2][3] = float(form.getvalue('CN_crop_C'))
CN[2][4] = float(form.getvalue('CN_crop_D'))
CN[3][1] = float(form.getvalue('CN_past_A'))
CN[3][2] = float(form.getvalue('CN_past_B'))
CN[3][3] = float(form.getvalue('CN_past_C'))
CN[3][4] = float(form.getvalue('CN_past_D'))
CN[4][1] = float(form.getvalue('CN_frst_A'))
CN[4][2] = float(form.getvalue('CN_frst_B'))
CN[4][3] = float(form.getvalue('CN_frst_C'))
CN[4][4] = float(form.getvalue('CN_frst_D'))
CN[5][1] = float(form.getvalue('CN_user_A'))
CN[5][2] = float(form.getvalue('CN_user_B'))
CN[5][3] = float(form.getvalue('CN_user_C'))
CN[5][4] = float(form.getvalue('CN_user_D'))

#----------------------------------------------------------------------------------Table6a
CNu = [0.0] * 10                                                                # CNu : detailed urban CN
for i in range(len(CNu)) :
  CNu[i] = [0.0] * 5

CNu[1][1] = float(form.getvalue('CN_comm_A'))
CNu[1][2] = float(form.getvalue('CN_comm_B'))
CNu[1][3] = float(form.getvalue('CN_comm_C'))
CNu[1][4] = float(form.getvalue('CN_comm_D'))
CNu[2][1] = float(form.getvalue('CN_indu_A'))
CNu[2][2] = float(form.getvalue('CN_indu_B'))
CNu[2][3] = float(form.getvalue('CN_indu_C'))
CNu[2][4] = float(form.getvalue('CN_indu_D'))
CNu[3][1] = float(form.getvalue('CN_inst_A'))
CNu[3][2] = float(form.getvalue('CN_inst_B'))
CNu[3][3] = float(form.getvalue('CN_inst_C'))
CNu[3][4] = float(form.getvalue('CN_inst_D'))
CNu[4][1] = float(form.getvalue('CN_tran_A'))
CNu[4][2] = float(form.getvalue('CN_tran_B'))
CNu[4][3] = float(form.getvalue('CN_tran_C'))
CNu[4][4] = float(form.getvalue('CN_tran_D'))
CNu[5][1] = float(form.getvalue('CN_mult_A'))
CNu[5][2] = float(form.getvalue('CN_mult_B'))
CNu[5][3] = float(form.getvalue('CN_mult_C'))
CNu[5][4] = float(form.getvalue('CN_mult_D'))
CNu[6][1] = float(form.getvalue('CN_sing_A'))
CNu[6][2] = float(form.getvalue('CN_sing_B'))
CNu[6][3] = float(form.getvalue('CN_sing_C'))
CNu[6][4] = float(form.getvalue('CN_sing_D'))
CNu[7][1] = float(form.getvalue('CN_urcu_A'))
CNu[7][2] = float(form.getvalue('CN_urcu_B'))
CNu[7][3] = float(form.getvalue('CN_urcu_C'))
CNu[7][4] = float(form.getvalue('CN_urcu_D'))
CNu[8][1] = float(form.getvalue('CN_vade_A'))
CNu[8][2] = float(form.getvalue('CN_vade_B'))
CNu[8][3] = float(form.getvalue('CN_vade_C'))
CNu[8][4] = float(form.getvalue('CN_vade_D'))
CNu[9][1] = float(form.getvalue('CN_open_A'))
CNu[9][2] = float(form.getvalue('CN_open_B'))
CNu[9][3] = float(form.getvalue('CN_open_C'))
CNu[9][4] = float(form.getvalue('CN_open_D'))

#----------------------------------------------------------------------------------Table7
Rnt = [0.0] * 10                                                        # Nutrient in Runoff
for i in range(len(Rnt)) :
  Rnt[i] = [0.0] * 4

Rnt[1][1] = float(form.getvalue('ntLcrop_1_N'))
Rnt[1][2] = float(form.getvalue('ntLcrop_1_P'))
Rnt[1][3] = float(form.getvalue('ntLcrop_1_B'))
Rnt[2][1] = float(form.getvalue('ntLcrop_2_N'))
Rnt[2][2] = float(form.getvalue('ntLcrop_2_P'))
Rnt[2][3] = float(form.getvalue('ntLcrop_2_B'))
Rnt[3][1] = float(form.getvalue('ntMcrop_1_N'))
Rnt[3][2] = float(form.getvalue('ntMcrop_1_P'))
Rnt[3][3] = float(form.getvalue('ntMcrop_1_B'))
Rnt[4][1] = float(form.getvalue('ntMcrop_2_N'))
Rnt[4][2] = float(form.getvalue('ntMcrop_2_P'))
Rnt[4][3] = float(form.getvalue('ntMcrop_2_B'))
Rnt[5][1] = float(form.getvalue('ntHcrop_1_N'))
Rnt[5][2] = float(form.getvalue('ntHcrop_1_P'))
Rnt[5][3] = float(form.getvalue('ntHcrop_1_B'))
Rnt[6][1] = float(form.getvalue('ntHcrop_2_N'))
Rnt[6][2] = float(form.getvalue('ntHcrop_2_P'))
Rnt[6][3] = float(form.getvalue('ntHcrop_2_B'))
Rnt[7][1] = float(form.getvalue('ntPast_N'))
Rnt[7][2] = float(form.getvalue('ntPast_P'))
Rnt[7][3] = float(form.getvalue('ntPast_B'))
Rnt[8][1] = float(form.getvalue('ntFrst_N'))
Rnt[8][2] = float(form.getvalue('ntFrst_P'))
Rnt[8][3] = float(form.getvalue('ntFrst_B'))
Rnt[9][1] = float(form.getvalue('ntUser_N'))
Rnt[9][2] = float(form.getvalue('ntUser_P'))
Rnt[9][3] = float(form.getvalue('ntUser_B'))

#----------------------------------------------------------------------------------Table7a
Gnt = [0.0] * 7                                                         # Nutrient in Groundwater
for i in range(len(Gnt)) :
  Gnt[i] = [0.0] * 4

Gnt[1][1] = float(form.getvalue('GntUrbn_N'))
Gnt[1][2] = float(form.getvalue('GntUrbn_P'))
Gnt[1][3] = float(form.getvalue('GntUrbn_B'))
Gnt[2][1] = float(form.getvalue('GntCrop_N'))
Gnt[2][2] = float(form.getvalue('GntCrop_P'))
Gnt[2][3] = float(form.getvalue('GntCrop_B'))
Gnt[3][1] = float(form.getvalue('GntPast_N'))
Gnt[3][2] = float(form.getvalue('GntPast_P'))
Gnt[3][3] = float(form.getvalue('GntPast_B'))
Gnt[4][1] = float(form.getvalue('GntFrst_N'))
Gnt[4][2] = float(form.getvalue('GntFrst_P'))
Gnt[4][3] = float(form.getvalue('GntFrst_B'))
Gnt[5][1] = float(form.getvalue('GntFeed_N'))
Gnt[5][2] = float(form.getvalue('GntFeed_P'))
Gnt[5][3] = float(form.getvalue('GntFeed_B'))
Gnt[6][1] = float(form.getvalue('GntUser_N'))
Gnt[6][2] = float(form.getvalue('GntUser_P'))
Gnt[6][3] = float(form.getvalue('GntUser_B'))

#----------------------------------------------------------------------------------Table8
dist = [0.0] * 11         #  9 %, sum %
for i in range(1,len(dist)) :
  dist[i] = [0.0] * numWSD
for i in range(1,len(dist)-1) :
  for j in range(1,len(dist[i])) :
    tmpVal = str(form.getvalue('dist_' + str(i) + str('%02i' % int(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      dist[i][j] = 0.0
    else :
      dist[i][j] = float(tmpVal)
for i in range(1,numWSD) :
  dist[10][i] = dist[1][i] + dist[2][i] + dist[3][i] + dist[4][i] + dist[5][i] + dist[6][i] + dist[7][i] + dist[8][i] + dist[9][i] 

#for i in range(1,numWSD) :
#  print '<li>', dist[1][i], dist[2][i], dist[3][i], dist[4][i], dist[5][i], dist[6][i], dist[7][i], dist[8][i], dist[9][i], dist[10][i]

#----------------------------------------------------------------------------------Table9
IrrVal = [0.0] * 5
for i in range(1,len(IrrVal)) :
  IrrVal[i] = [0.0] * numWSD
  for j in range(1,len(IrrVal[i])) :
    tmpVal = str(form.getvalue('IrrVal_' + str(i) + str('%02i' % int(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      IrrVal[i][j] = 0.0
    else :
      IrrVal[i][j] = float(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', IrrVal[1][i], IrrVal[2][i], IrrVal[3][i], IrrVal[4][i]

#----------------------------------------------------------------------------------
#----Reference soil infiltration fraction for precipitation, "Land&Rain" sheet: GW1 table
gwOpt = form.getvalue('gwOpt')
if ( gwOpt == 'on' or gwOpt == 'checked' ) :
  gwOpt = int(1)
else : 
  gwOpt = int(4) 
gwInft = [0.0] * 6
for i in range(1,6) :
  gwInft[i] = [0.0] * 5
  for j in range(1,len(gwInft[i])) :
    tmpVal = str(form.getvalue('gwInft_' + str(i) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' or 2 < int(gwOpt) ) :
      gwInft[i][j] = 0.0
    else :
      gwInft[i][j] = float(tmpVal)

#----Wildlife density in cropland, "Animal" sheet: Table 2
WildLife = [0] * 6
for i in range(1,len(WildLife)) :
  tmpVal = str(form.getvalue('WildLife_' + str(i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    WildLife[i] = 0.0
  else :
    WildLife[i] = tmpVal

#----Reference, "Reference" sheet: Modified from ASAE, 1998
Reference = [0.0] * 14
for i in range(1,14) :
  Reference[i] = [0.0] * 5
  for j in range(1,len(Reference[i])) :
    tmpVal = str(form.getvalue('Reference_' + str('%02i' % int(i)) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Reference[i][j] = 0.0
    else :
      Reference[i][j] = float(tmpVal)

#----Septic, "Septic" sheet: values between Table 1 and 2
Septic = [0.0] * 8
Septic[0] = form.getvalue('Septic_11')
Septic[1] = form.getvalue('Septic_21')
Septic[2] = form.getvalue('Septic_31')
Septic[3] = form.getvalue('Septic_41')
Septic[4] = form.getvalue('Septic_12')
Septic[5] = form.getvalue('Septic_22')
Septic[6] = form.getvalue('Septic_32')
Septic[7] = form.getvalue('Septic_42')

#----Feedlot, "Feedlot" sheet: Table (B51-F61)
Feedlot = [0.0] * 12
for i in range(1,len(Feedlot)) :
  Feedlot[i] = [0.0] * 5
  for j in range(1,5) :
    tmpVal = str(form.getvalue('Feedlot_' + str('%02i' % int(i)) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Feedlot[i][j] = '%.3f' % float(0.0)
    else :
      Feedlot[i][j] = '%.3f' % float(tmpVal)

#----Gully DB 1, "Gully&Streambank" sheet: Table (AC2-AD11, AH2-AH5)
GullyDB = [0.0] * 13
for i in range(1,11) :
  GullyDB[i] = [0.0] * 3
  for j in range(1,3) :
    tmpVal = str(form.getvalue('GullyDB_' + str('%02i' % int(i)) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GullyDB[i][j] = '%.4f' % float(0.0)
    else :
      GullyDB[i][j] = '%.4f' % float(tmpVal)
GullyDB[11] = [0.0] * 2
GullyDB[12] = [0.0] * 2
GullyDB[11][0] = str(form.getvalue('GullyDB_111'))
GullyDB[11][1] = str(form.getvalue('GullyDB_121'))
GullyDB[12][0] = str(form.getvalue('GullyDB_131'))
GullyDB[12][1] = str(form.getvalue('GullyDB_141'))
if ( GullyDB[11][0] == 'None' or GullyDB[11][0] == '' ) :
  GullyDB[11][0] = '%.4f' % float(0.0)
else :
  GullyDB[11][0] = '%.4f' % float(GullyDB[11][0])
if ( GullyDB[11][1] == 'None' or GullyDB[11][1] == '' ) :
  GullyDB[11][1] = '%.4f' % float(0.0)
else :
  GullyDB[11][1] = '%.4f' % float(GullyDB[11][1])
if ( GullyDB[12][0] == 'None' or GullyDB[12][0] == '' ) :
  GullyDB[12][0] = '%.4f' % float(0.0)
else :
  GullyDB[12][0] = '%.4f' % float(GullyDB[12][0])
if ( GullyDB[12][1] == 'None' or GullyDB[12][1] == '' ) :
  GullyDB[12][1] = '%.4f' % float(0.0)
else :
  GullyDB[12][1] = '%.4f' % float(GullyDB[12][1])

numGLY = int(form.getvalue('numGLY'))
numSTR = int(form.getvalue('numSTR'))
GS1 = [0.0] * (numGLY+1) 
for i in range(1,numGLY+1) :
  GS1[i] = [0.0] * 10           # 9 values for gully
  for j in range(1,10) :
    tmpVal = str(form.getvalue('GS1_' + str('%02i' % int(i)) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GS1[i][j] = float(0) 
    else :
      GS1[i][j] = float(tmpVal)

GS2 = [0.0] * (numSTR + 1)
for i in range(1,numSTR+1) :
  GS2[i] = [0.0] * 8
  for j in range(1,8) :
    tmpVal = str(form.getvalue('GS2_' + str('%02i' % int(i)) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GS2[i][j] = float(0.0)
    else :
      GS2[i][j] = float(tmpVal)

for i in range(1,numGLY+1) :
  GS1[i][1] = int(GS1[i][1])
  GS1[i][2] = int(GS1[i][2])
  GS1[i][9] = int(GS1[i][9])
for i in range(1,numSTR+1) :
  GS2[i][1] = int(GS2[i][1])
  GS2[i][2] = int(GS2[i][2])
  GS2[i][5] = int(GS2[i][5])
  GS2[i][7] = int(GS2[i][7])

#for i in range(1,numGLY+1) :
#  print '<li>', GS1[i][1], GS1[i][2], GS1[i][3], GS1[i][4], GS1[i][5], GS1[i][6], GS1[i][7], GS1[i][8], GS1[i][9]
#print '<hr>' 
#for i in range(1,numSTR+1) :
#  print '<li>', GS2[i][1], GS2[i][2], GS2[i][3], GS2[i][4], GS2[i][5], GS2[i][6], GS2[i][7]

#--make inpFiles
inpPath = path + 'inp/'
mkINPdir = 'mkdir ' + str(inpPath)
chmod777 = 'chmod 777 ' + str(inpPath)
os.system(mkINPdir)
os.system(chmod777)

##--myOptPar.pys
#cpOptFile = 'cp ' + path + 'myOptPar.pys ' + inpPath + '.'
#os.system(cpOptFile)


#--mainINP.txt
mainINP = open(inpPath + 'mainINP.txt','w')
mainINP.write(str(numWSD-1) + '\t' + str(swsOpt) + '\n')
mainINP.write('----------------------------------------------------\n')
for i in range(1,numWSD) :                                                    # Table 1
  for j in range(1,7) :
    LuseAreaWSD[j][i] = '%.2f' % float(LuseAreaWSD[j][i])
    mainINP.write(str(LuseAreaWSD[j][i]) + '\t')
  PctFeedlot[i] = '%.2f' % float(PctFeedlot[i])
  TAreaWSD[i] = '%.2f' % float(TAreaWSD[i])
  mainINP.write(str(PctFeedlot[i]) + '\t')
  mainINP.write(str(TAreaWSD[i]) + '\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 2
  for j in range(1,10) :
    Anm[j][i] = int(Anm[j][i])
    mainINP.write(str(Anm[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 3
  NumSpSys[i] = '%.2f' % float(NumSpSys[i])
  PpSpSys[i] = '%.2f' % float(PpSpSys[i])
  SpFailRate[i] = '%.2f' % float(SpFailRate[i])
  NumPpDrtDc[i] = '%.2f' % float(NumPpDrtDc[i])
  RdcDrtDc[i] = '%.2f' % float(RdcDrtDc[i])
  mainINP.write(str(NumSpSys[i]) + '\t')
  mainINP.write(str(PpSpSys[i]) + '\t')
  mainINP.write(str(SpFailRate[i]) + '\t')
  mainINP.write(str(NumPpDrtDc[i]) + '\t')
  mainINP.write(str(RdcDrtDc[i]) + '\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 4
  for j in range(1,6) :
    usleCropland[j][i] = '%.4f' % float(usleCropland[j][i])
    mainINP.write(str(usleCropland[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('\n')
for i in range(1,numWSD) :
  for j in range(1,6) :
    uslePasture[j][i] = '%.4f' % float(uslePasture[j][i])
    mainINP.write(str(uslePasture[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('\n')
for i in range(1,numWSD) :
  for j in range(1,6) :
    usleForest[j][i] = '%.4f' % float(usleForest[j][i])
    mainINP.write(str(usleForest[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('\n')
for i in range(1,numWSD) :
  for j in range(1,6) :
    usleUser[j][i] = '%.4f' % float(usleUser[j][i])
    mainINP.write(str(usleUser[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 5
  HSG[i] = int(HSG[i])
  SoilN[i] = '%.3f' % float(SoilN[i])
  SoilP[i] = '%.3f' % float(SoilP[i])
  SoilB[i] = '%.3f' % float(SoilB[i])
  mainINP.write(str(HSG[i]) + '\t' + str(SoilN[i]) + '\t' + str(SoilP[i]) + '\t' + str(SoilB[i]) + '\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,6) :                                                           # Table 6
  for j in range(1,5) :
    CN[i][j] = '%.2f' % float(CN[i][j])
    mainINP.write(str(CN[i][j]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,10) :                                                          # Table 6a
  for j in range(1,5) :
    CNu[i][j] = '%.2f' % float(CNu[i][j])
    mainINP.write(str(CNu[i][j]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,10) :                                                          # Table 7
  for j in range(1,4) :
    Rnt[i][j] = '%.3f' % float(Rnt[i][j])
    mainINP.write(str(Rnt[i][j]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,7) :                                                           # Table 7a
  for j in range(1,4) :
    Gnt[i][j] = '%.3f' % float(Gnt[i][j])
    mainINP.write(str(Gnt[i][j]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 8
  mainINP.write(str(LuseAreaWSD[1][i]) + '\t')
  tmpVal = 0.0
  for j in range(1,10) :
    dist[j][i] = '%.2f' % float(dist[j][i])
    tmpVal = float(tmpVal) + float(dist[j][i])
    mainINP.write(str(dist[j][i]) + '\t')
  mainINP.write(str('%.2f' % float(tmpVal)))
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')

for i in range(1,numWSD) :                                                    # Table 9
  mainINP.write(str(LuseAreaWSD[2][i]) + '\t')
  for j in range(1,5) :
    IrrVal[j][i] = '%.2f' % float(IrrVal[j][i])
    mainINP.write(str(IrrVal[j][i]) + '\t')
  mainINP.write('\n')
mainINP.write('----------------------------------------------------\n')
mainINP.close()

#--LandRain_GW1.txt
gwInftFile = open(inpPath + 'LandRain_GW1.txt','w')
gwInftFile.write('A\tB\tC\tD\tSHG\n')
for i in range(1,6) :
  for j in range(1,5) :
    gwInft[i][j] = '%.3f' % float(gwInft[i][j])
    gwInftFile.write(str(gwInft[i][j]) + '\t')
  gwInftFile.write('\n')
gwInftFile.close()

#--WildLife.txt
WildLifeFile = open(inpPath + 'WildLife.txt','w')
for i in range(1,6) :
  WildLife[i] = '%.2f' % float(WildLife[i])
  WildLifeFile.write(str(WildLife[i]) + '\n')
WildLifeFile.close()

#--Reference.txt
ReferenceFile = open(inpPath + 'Reference.txt','w')
ReferenceFile.write('Typical Animal Mass,lb  BOD,lb/day/1000lb animal        BOD per Animal,lb/day   BOD per Animal,lb/yr \n')
for i in range(1,14) :
  for j in range(1,5) :
    Reference[i][j] = '%.2f' % float(Reference[i][j])
    ReferenceFile.write(str(Reference[i][j]) + '\t')
  ReferenceFile.write('\n')
ReferenceFile.close()

#--Septic.txt
SepticFile = open(inpPath + 'Septic.txt','w')
SepticFile.write(str(Septic[0]) + '\n')
SepticFile.write(str(Septic[1]) + '\n')
SepticFile.write(str(Septic[2]) + '\n')
SepticFile.write(str(Septic[3]) + '\n')
SepticFile.write(str(Septic[4]) + '\n')
SepticFile.write(str(Septic[5]) + '\n')
SepticFile.write(str(Septic[6]) + '\n')
SepticFile.write(str(Septic[7]) + '\n')
SepticFile.close()

#--Feedlot.txt
FeedlotFile = open(inpPath + 'Feedlot.txt','w')
FeedlotFile.write('N\tP\tBOD\tCOD\tAnimal\n')
for i in range(1,12) :
  for j in range(1,5) :
    FeedlotFile.write(str(Feedlot[i][j]) + '\t')
  FeedlotFile.write('\n')
FeedlotFile.close()

#--Gully.txt
GullyFile = open(inpPath + 'Gully.txt','w')
for i in range(1,11) :
  for j in range(1,3) :
    GullyFile.write(str(GullyDB[i][j]) + '\t')
  GullyFile.write('\n')
GullyFile.write('-----------------------\n')
GullyFile.write(str(GullyDB[11][0]) + '\n' + str(GullyDB[11][1]) + '\n')
GullyFile.write(str(GullyDB[12][0]) + '\n' + str(GullyDB[12][1]) + '\n')
GullyFile.write('-----------------------\n')
GullyFile.write(str(numGLY) + '\n')
for i in range(1,numGLY+1) :
  for j in range(1,10) :
    GullyFile.write(str(GS1[i][j]) + '\t')
  GullyFile.write('\n')
GullyFile.write('-----------------------\n')
GullyFile.write(str(numSTR) + '\n')
for i in range(1,numSTR+1) :
  for j in range(1,8) :
    GullyFile.write(str(GS2[i][j]) + '\t')
  GullyFile.write('\n')
GullyFile.close()


#--Calculate Annual Direct Runoff Depth (mm)------------------E--

ch777 = 'chmod 777 ' + str(inpPath) + '*.*'
os.system(ch777)
ch777 = 'chmod 777 ' + str(path) + 'cligen/*.*'
os.system(ch777)
ch777 = 'chmod 777 ' + str(path) + 'cligen'
os.system(ch777)
#rmtmp = 'rm -rf ./tmp/1' 
#os.system(rmtmp)
#----E input----------------------------------------------------------------------------------------------------

print '<html>'
print '<head><title>Web-based STEPL</title></head>'
print '<body onLoad="BMP_LDC();"><br>'

print '<center><img src="./img/STEPL_WEB_title.jpg" width=400></center><br><br>'

#------------------------------------S Button to Open cal_1.cgi-------------------------------------------------
print '<center><hr>'
print '<table border=0 width=900>'
print '  <tr>'
print '    <td align=left>'
print '      <font color=tomato size=5 face="Times New Roman">Options:'
tmpStr = '      <input type=button style=\'width:200;height:30;cursor:hand\' value=\'Auto-Calibration\''
tmpStr += ' onClick="javascript:window.open(\'./calopt1.cgi?ystime=' + str(ystime)
tmpStr += '&ystimeldc=' + ystimeldc + '\');"> &nbsp; &nbsp;'
print tmpStr
if ( ystimeldc[0] == '2' and numWSD <= 2 ) :        # only single watershed
  bmpOptBtn = '      <input type=button style=\'width:200;height:30;cursor:hand\' value=\'BMP Optimization-Single\''
  bmpOptBtn += ' onClick="javascript:window.open(\'./bmpopt1.cgi?ystime=' + str(ystime)
  bmpOptBtn += '&ystimeldc=' + ystimeldc + '&allPct=' + allPct + '\');"> &nbsp; &nbsp;'
#  print bmpOptBtn
bmpOptBtn2 = '      <input type=button style=\'width:200;height:30;cursor:hand\' value=\'BMP Optimization\''
bmpOptBtn2 += ' onClick="javascript:window.open(\'./multibmp1.cgi?ystime=' + str(ystime)
bmpOptBtn2 += '&ystimeldc=' + ystimeldc + '&allPct=' + allPct + '\');">'
print bmpOptBtn2
print '    </td>'
print '  </tr>'
print '</table>'

print '<hr>' 
#------------------------------------E Button to Open cal_1.cgi-------------------------------------------------
#----S use of BMP_LDC.txt---------------------------------------------------------------------------------------
#if ( ystimeldc[0] == '2' ) :               # if from LDC
if ( ystimeldc[0] == '7' ) :                                                           # to skip here 
  bmpSgtFile = open('../pldc/tmp/' + ystimeldc + '/BMP_LDC.txt','r')
  bmpSgt = bmpSgtFile.readlines()
  bmpSgtFile.close()

  bmpDBFile = open('./BMPlist.txt','r')
  tmpStr = bmpDBFile.readline()
  bmpInfo = bmpDBFile.readlines()
  bmpDBFile.close()
  for i in range(len(bmpInfo)) :
    bmpInfo[i] = bmpInfo[i].split('\t')

  effArr = [''] * len(bmpSgt)
  for i in range(len(bmpSgt)) :
    bmpSgt[i] = bmpSgt[i].replace('\r','')
    bmpSgt[i] = bmpSgt[i].replace('\n','')
    bmpSgt[i] = bmpSgt[i].split('\t')
    tmpStr_1 = bmpSgt[i][2].replace(' ','')
    for j in range(len(bmpInfo)) :              # to find efficiencies
      tmpStr_2 = bmpInfo[j][1].replace(' ','')
      if ( str(bmpInfo[j][0]) == str(bmpSgt[i][0]) and tmpStr_1 == tmpStr_2 ) :
        tmpStr = str(bmpInfo[j][-1])              # 1_6 : luse_BMP
  if ( int(tmpStr[0]) < 6 ) :             # if not urban
    tmpStr += '_' + str(float(bmpInfo[j][2])*float(bmpSgt[i][3])/100.0)
    tmpStr += '_' + str(float(bmpInfo[j][3])*float(bmpSgt[i][3])/100.0)
    tmpStr += '_' + str(float(bmpInfo[j][4])*float(bmpSgt[i][3])/100.0)
    tmpStr += '_' + str(float(bmpInfo[j][5])*float(bmpSgt[i][3])/100.0)
  else :                    # if urban
    tmpStr += '_' + str(bmpInfo[j][2]) + '_' + str(bmpInfo[j][3])
    tmpStr += '_' + str(bmpInfo[j][4]) + '_' + str(bmpInfo[j][5])
    tmpStr += '_' + str(bmpSgt[i][3])
  effArr[i] = tmpStr
  effArr[i] = effArr[i].replace('\r','')
  effArr[i] = effArr[i].replace('\n','')
# print '<li>', bmpSgt[i], '::', bmpInfo[j][2], bmpInfo[j][3], bmpInfo[j][4], bmpInfo[j][5], bmpInfo[j][-1]
#  for i in range(len(effArr)) :
#    print '<li>--', effArr[i]

#  print '<br><input type=button style=\'width:200;height:30;cursor:hand\' value=\'Apply Suggested BMPs\' onClick="javascript:BMP_LDC();">' 


#----E use of BMP_LDC.txt---------------------------------------------------------------------------------------

#----------------S BMPinputs------------------------------------------------------------------------------------
print '<form name=bmpMain method="POST" action="./run_1.cgi" target="new1">'
LdcLnkStr = '  <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
print LdcLnkStr

print '<center>'
print '<table border=0 width=900>'
print '  <tr>'
print '    <td align=left><b><font color=tomato size=5 face="Times New Roman">Set BMPs</font></b></td>'
print '  </tr>'
print '</table>'

tmpStr = '<input type=hidden name=ystime value="' + str(ystime) + '">'
print tmpStr
tmpStr = '<input type=hidden name=numWSD value="' + str(numWSD) + '">'
print tmpStr

#----CROP
print '  <table border=1 width=870>'
print '    <tr>'
print '      <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>CROPLAND</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>N</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BOD</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Sediment</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMPs</td>'
print '      <td align=center bgcolor=#BDBDBD><b>% Area BMP Applied</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + str(i)
  print '    <tr>'
  print '      <td align=center>', tmpStr, '</td>'
  for j in range(1,5) :
    tmpName = 'BMP_1_' + str('%02i' % int(i)) + str(j)
    print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_1_' + str('%02i' % int(i)) + '5'
  tmpJava = 'CropBMP_' + str('%02i' % int(i)) + '();'
  print '      <td align=center><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'
  print '                     <option value=1>No BMP'
  print '                     <option value=2>Combined BMPs-Calculated'
  print '                     <option value=3>Contour Farming'
  print '                     <option value=4>Diversion'
  print '                     <option value=5>Filter strip'
  print '                     <option value=6>Reduced Tillage Systems'
  print '                     <option value=7>Streambank stabilization and fencing'
  print '                     <option value=8>Terrace'
  print '                   </select>'
  print '      </td>'
  tmpName = 'name=BMP_1_' + str('%02i' % int(i)) + '6'
  print '    <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 ', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  print '      </td>'
  print '    </tr>'
print '  </table><br>'

#----PAST
print '  <table border=1 width=870>'
print '    <tr>'
print '      <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>PASTLAND</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>N</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BOD</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Sediment</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMPs</td>'
print '      <td align=center bgcolor=#BDBDBD><b>% Area BMP Applied</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + str(i)
  print '<tr>'
  print '  <td align=center>', tmpStr, '</td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '1'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '2'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '3'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '4'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '5'
  tmpJava = 'PastBMP_' + str('%02i' % int(i)) + '();'
  print '  <td align=center><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'
  print '                     <option value=1>No BMP'
  print '                     <option value=2>Combined BMPs-Calculated'
  print '                     <option value=3>User'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_2_' + str('%02i' % int(i)) + '6'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  print '  </td>'
  print '</tr>'
print '  </table><br>'

#----FRST
print '  <table border=1 width=870>'
print '    <tr>'
print '      <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>FOREST</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>N</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BOD</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Sediment</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMPs</td>'
print '      <td align=center bgcolor=#BDBDBD><b>% Area BMP Applied</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + str(i)
  print '<tr>'
  print '  <td align=center>', tmpStr, '</td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '1'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '2'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '3'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '4'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '5'
  tmpJava = 'FrstBMP_' + str('%02i' % int(i)) + '();'
  print '  <td align=center><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'
  print '                     <option value=1>No BMP'
  print '                     <option value=2>Combined BMPs-Calculated'
  print '                     <option value=3>Road dry seeding'
  print '                     <option value=4>Road grass and legume seeding'
  print '                     <option value=5>Road grass and legume seeding-New'
  print '                     <option value=6>Road hydro mulch'
  print '                     <option value=7>Road straw mulch'
  print '                     <option value=8>Road tree planting'
  print '                     <option value=9>Site preparation/hydro mulch/seed/fertilizer'
  print '                     <option value=10>Site preparation/hydro mulch/seed/fertilizer/transplants'
  print '                     <option value=11>Site preparation/steep slope seeder/transplant'
  print '                     <option value=12>Site preparation/straw/crimp seed/fertilizer/transplant'
  print '                     <option value=13>Site preparation/straw/crimp/net'
  print '                     <option value=14>Site preparation/straw/net/seed/fertilizer/transplant'
  print '                     <option value=15>Site preparation/straw/polymer/seed/fertilizer/transplant'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_3_' + str('%02i' % int(i)) + '6'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  print '  </td>'
  print '</tr>'
print '  </table><br>'

#----USER
print '  <table border=1 width=870>'
print '    <tr>'
print '      <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>USER DEFINED</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>N</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BOD</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Sediment</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMPs</td>'
print '      <td align=center bgcolor=#BDBDBD><b>% Area BMP Applied</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + str(i)
  print '<tr>'
  print '  <td align=center>', tmpStr, '</td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '1'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '2'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '3'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '4'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '5'
  tmpJava = 'UserBMP_' + str('%02i' % int(i)) + '();'
  print '  <td align=center><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'
  print '                     <option value=1>No BMP'
  print '                     <option value=2>Combined BMPs-Calculated'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_4_' + str('%02i' % int(i)) + '6'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  print '  </td>'
  print '</tr>'
print '  </table><br>'

#----FEED
print '  <table border=1 width=870>'
print '    <tr>'
print '      <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>FEEDLOT</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>N</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BOD</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Sediment</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMPs</td>'
print '      <td align=center bgcolor=#BDBDBD><b>% Area BMP Applied</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + str(i)
  print '<tr>'
  print '  <td align=center>', tmpStr, '</td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '1'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '2'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '3'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '4'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '5'
  tmpJava = 'FeedBMP_' + str('%02i' % int(i)) + '();'
  print '  <td align=center><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'
  print '                     <option value=1>No BMP'
  print '                     <option value=2>Diversion'
  print '                     <option value=3>Filter strip'
  print '                     <option value=4>Runoff Mgmt System'
  print '                     <option value=5>Solids Separation Basin'
  print '                     <option value=6>Solids Separation Basin w/Infilt Bed'
  print '                     <option value=7>Terrace'
  print '                     <option value=8>Waste Mgmt System'
  print '                     <option value=9>Waste Storage Facility'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_5_' + str('%02i' % int(i)) + '6'
  print '  <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  print '  </td>'
  print '</tr>'
print '  </table><br>'

print '<table width=870 border=1>'
print '  <tr>'
print '    <td align=center colspan=7><font color=blue>BMPs and efficiencies for different pollutants on <b>Urban</td>'
print '  </tr>'
print '  <tr>'
print '    <td align=center>'
tmpStr = '    <input type=button style=\'width:200;height:30;cursor:hand\' value=\'Urban BMPs\''
tmpStr = tmpStr + ' onClick="javascript:window.open(\'./urBMP.cgi?numWSD=' + str(numWSD)
tmpStr = tmpStr + '\',\'UrbanBMP\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=600,width=980\');">'
print tmpStr
print '    </td>'
print '  </tr>'
print '</table><br><hr>'

#----Urban Conc.
print '<input type=hidden name=UrbnConc_11 value=2.0><input type=hidden name=UrbnConc_12 value=2.5><input type=hidden name=UrbnConc_13 value=1.8>'
print '<input type=hidden name=UrbnConc_14 value=3.0><input type=hidden name=UrbnConc_15 value=2.2><input type=hidden name=UrbnConc_16 value=2.2>'
print '<input type=hidden name=UrbnConc_17 value=1.9><input type=hidden name=UrbnConc_18 value=1.5><input type=hidden name=UrbnConc_19 value=1.5>'
print '<input type=hidden name=UrbnConc_21 value=0.2><input type=hidden name=UrbnConc_22 value=0.4><input type=hidden name=UrbnConc_23 value=0.3>'
print '<input type=hidden name=UrbnConc_24 value=0.5><input type=hidden name=UrbnConc_25 value=0.4><input type=hidden name=UrbnConc_26 value=0.4>'
print '<input type=hidden name=UrbnConc_27 value=0.3><input type=hidden name=UrbnConc_28 value=0.2><input type=hidden name=UrbnConc_29 value=0.2>'
print '<input type=hidden name=UrbnConc_31 value=9.3><input type=hidden name=UrbnConc_32 value=9.0><input type=hidden name=UrbnConc_33 value=7.8>'
print '<input type=hidden name=UrbnConc_34 value=9.3><input type=hidden name=UrbnConc_35 value=10.0><input type=hidden name=UrbnConc_36 value=10.0>'
print '<input type=hidden name=UrbnConc_37 value=4.0><input type=hidden name=UrbnConc_38 value=4.0><input type=hidden name=UrbnConc_39 value=4.0>'
print '<input type=hidden name=UrbnConc_41 value=75.0><input type=hidden name=UrbnConc_42 value=120.0><input type=hidden name=UrbnConc_43 value=67.0>'
print '<input type=hidden name=UrbnConc_44 value=150.0><input type=hidden name=UrbnConc_45 value=100.0><input type=hidden name=UrbnConc_46 value=100.0>'
print '<input type=hidden name=UrbnConc_47 value=150.0><input type=hidden name=UrbnConc_48 value=70.0><input type=hidden name=UrbnConc_49 value=70.0>'

#----Urban BMPs
# 1: area, 2: N, 3: P, 4: BOD, 5: TSS -> k ,  BMP_k_0ij
for k in range(1,6) : 
  for i in range(1,numWSD) :
    for j in range(1,10) :    # 9 distribution
      tmpStr = '<input type=hidden size=4 name=UrbanBMP_' + str(k) + '_' + str('%02i'%i) + str(j) + ' value=0.0>'
      print tmpStr

#----Urban BMPs info, just to keep the information of Urban info. not for cgi
for i in range(1,numWSD) :
  for j in range(1,10) :
    InfoStr = '<input type=hidden size=4 name=UrbanBMPinfo_' + str('%02i'%i) + str(j) + ' value=0>'
    print InfoStr



print '<center><br><br><input style="WIDTH:200;height:30;CURSOR:hand" type=submit value="Next"><br><br></center>'

print '</form>'
#----------------E BMPinputs------------------------------------------------------------------------------------
#------------------------------S BMP_ListForm.txt---------------------------------------------------------------
bmpListFile = open('./BMP_ListForm.txt','r')
bmpList = bmpListFile.readlines()
bmpListFile.close()
for i in range(len(bmpList)) :
  bmpList[i] = bmpList[i].replace('\n','')
  print bmpList[i]
#------------------------------E BMP_ListForm.txt---------------------------------------------------------------
#----S ubForm---------------------------------------------------------------------------------------------------
print '<form name=ubForm>'    # for urBMP.cgi
for i in range(1,numWSD) :
  for j in range(1,10) :    # 9 distribution percent values
    tmpStr = '<input type=hidden name=ubDis_' + str('%02i'%i) + str(j) + ' value="' + str(dist[j][i]) + '" size=2>'
    print tmpStr
for i in range(1,numWSD) :
  tmpStr = '<input type=hidden name=ubArea_' + str('%02i'%i) + ' value="' + str(LuseAreaWSD[1][i]) + '" size=2>'
  print tmpStr

print '</form>'
#----E ubForm---------------------------------------------------------------------------------------------------
print '<center><hr>'
print '<font size=2>'
print '  <font color=gray>'
print '    Copyright &copy; 2012, Purdue University and Kangwon National University, all rights reserved. <br>'
print '    Purdue University is an equal access/equal opportunity university.<br>'
print '  </font>'
print '  Contact <a href=mailto:engelb@purdue.edu>Dr. Bernie Engel</a>'
print '  for more details if you need any help for STEPL WEB.'
print '  <br>'
print '  Programmed by <a href=mailto:parkyounshik@gmail.com>Youn Shik Park</a>, Purdue University Research Assistant'
print '</font><br>'
print '</body>'
#----S JavaScript-----------------------------------------------------------------------------------------------
print '<script language="JavaScript">'
for i in range(1,numWSD) :
  tmpStr = 'function CropBMP_' + str('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_1_' + str('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_1_' + str('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_1_' + str('%02i'%i) + str(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,9) :         # 8 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_1_' + str('%02i'%i) + '5.selectedIndex == \'' + str(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_1_' + str('%02i'%i) + str(k) + '.value = document.BMP_List.CROP_' + str('%02i'%j) + str(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function PastBMP_' + str('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_2_' + str('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_2_' + str('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_2_' + str('%02i'%i) + str(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,4) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_2_' + str('%02i'%i) + '5.selectedIndex == \'' + str(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_2_' + str('%02i'%i) + str(k) + '.value = document.BMP_List.PAST_' + str('%02i'%j) + str(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function FrstBMP_' + str('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_3_' + str('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_3_' + str('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_3_' + str('%02i'%i) + str(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,16) :         # 15 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_3_' + str('%02i'%i) + '5.selectedIndex == \'' + str(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_3_' + str('%02i'%i) + str(k) + '.value = document.BMP_List.FRST_' + str('%02i'%j) + str(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function UserBMP_' + str('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_4_' + str('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_4_' + str('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_4_' + str('%02i'%i) + str(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,3) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_4_' + str('%02i'%i) + '5.selectedIndex == \'' + str(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_4_' + str('%02i'%i) + str(k) + '.value = document.BMP_List.USER_' + str('%02i'%j) + str(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function FeedBMP_' + str('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_5_' + str('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_5_' + str('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_5_' + str('%02i'%i) + str(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,10) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_5_' + str('%02i'%i) + '5.selectedIndex == \'' + str(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_5_' + str('%02i'%i) + str(k) + '.value = document.BMP_List.FEED_' + str('%02i'%j) + str(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'


#---- BMP by LDC
print 'function BMP_LDC() {'
if ( ystimeldc[0] == '7' ) :              # to skip here
#if ( ystimeldc[0] == '2' ) :
  for i in range(len(effArr)) :
    effArr[i] = effArr[i].split('_')
      # effArr: 'luse code', 'BMP code', 'N eff', 'P eff', 'B eff', 'S eff', 'area suggested %'
    if ( int(effArr[i][0]) < 6 ) :        # excluding Urban
      for j in range(1,numWSD) :
        bmpStr = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '5.value = ' + str(effArr[i][1]) + ';'
        N_Str = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '1.value = ' + str(effArr[i][2]) + ';'
        P_Str = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '2.value = ' + str(effArr[i][3]) + ';'
        B_Str = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '3.value = ' + str(effArr[i][4]) + ';'
        S_Str = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '4.value = ' + str(effArr[i][5]) + ';'
        areaStr = '  document.bmpMain.BMP_' + str(effArr[i][0]) + '_' + str('%02i'%j) + '6.value = ' + str(effArr[i][6]) + ';'
        print bmpStr
        print N_Str
        print P_Str
        print B_Str
        print S_Str
        print areaStr
    else :              # Urban
      # UrbanBMP_k_ij, k: 1 for area, 2 for N, 3 for P, 4 for BOD, 5 for S
      #          o: watershed
      #          j: 9 dist. of urban
      SgtPct = float(effArr[i][6])        # percentage to apply
      for o in range(1,numWSD) :        # wsd
        for j in range(1,10) :          # 9 dist. of urban
          tmpVal_1 = float(LuseAreaWSD[1][o])
          tmpVal_2 = float(dist[j][o])
          tmpVal_3 = float(effArr[i][6])
          tmpVal_4 = tmpVal_1 * tmpVal_2 / 100.0 * tmpVal_3 / 100.0
          jsStrArea = '  document.bmpMain.UrbanBMP_1_' + str('%02i'%o) + str(j) + '.value = ' + str(tmpVal_4) + ';'
          jsStrN = '  document.bmpMain.UrbanBMP_2_' + str('%02i'%o) + str(j) + '.value = ' + str(effArr[i][2]) + ';'
          jsStrP = '  document.bmpMain.UrbanBMP_3_' + str('%02i'%o) + str(j) + '.value = ' + str(effArr[i][3]) + ';'
          jsStrB = '  document.bmpMain.UrbanBMP_4_' + str('%02i'%o) + str(j) + '.value = ' + str(effArr[i][4]) + ';'
          jsStrS = '  document.bmpMain.UrbanBMP_5_' + str('%02i'%o) + str(j) + '.value = ' + str(effArr[i][5]) + ';'
          print jsStrArea
          print jsStrN
          print jsStrP
          print jsStrB
          print jsStrS
                
          # UrbanBMPinfo
          jsStrBMPinfo = '  document.bmpMain.UrbanBMPinfo_' + str('%02i'%o) + str(j) + '.value = "' + str(effArr[i][1]) + '" ;'
          print jsStrBMPinfo


print '}'

print '</script>'
#----E JavaScript-----------------------------------------------------------------------------------------------






















print '</html>'


