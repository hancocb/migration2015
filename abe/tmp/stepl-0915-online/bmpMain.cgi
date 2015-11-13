#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>"
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, find 'Table1', 'Table2',...
# to jump, find 'BMPinputs', 'ubForm', 'JavaScript'

def isFloat(string):
  try:
    ret = float(string)
  except:
    ret = 0
  return ret

def isInt(string):
  try:
    ret = int(string)
  except:
    ret = 0
  return ret

def isStr(string):
  try:
    ret = str(string);
  except:
    ret = 0
  return ret

#----S input----------------------------------------------------------------------------------------------------
#rerun = 0
ystimeldc = isStr(form.getvalue('ystimeldc'))
allPct = isStr(form.getvalue('allPct'))

numWSD = isInt(form.getvalue('numWSD'))
numGLY = isInt(form.getvalue('numGLY'))
numSTR = isInt(form.getvalue('numSTR'))
ystime = isStr(form.getvalue('ystime'))
status = isInt(form.getvalue('status'))
rerun = isInt(form.getvalue('rerun'))
numWSD = numWSD + 1								# loop starts at 1 not 0
path = './tmp/' + ystime + '/'

if rerun == 3:
  status = isInt(form.getvalue('simLog'))
  rerun = 2
elif rerun == 2:
  simDir = glob.glob(path + 'sim_*')
  status = isInt(len(simDir))


if rerun == 2:
  simDir = glob.glob(path + 'sim_*')
  status = isInt(len(simDir))
  simDir = 'sim_' + isStr('%03i'%status)

  table1list = [[0 for i in range(numWSD)] for i in range(6)]
  table2list = [[0 for i in range(numWSD)] for i in range(6)]
  table3list = [[0 for i in range(numWSD)] for i in range(6)]
  table4list = [[0 for i in range(numWSD)] for i in range(6)]
  table5list = [[0 for i in range(numWSD)] for i in range(6)]

  table6list = [[0 for i in range(numWSD)] for i in range(6)]

  tableurban = [[0 for i in range(numWSD)] for i in range(9)]
  tableUbBMP = [[[0 for i in range(5)] for i in range(numWSD)] for i in range(9)]

  try:
    bmpInputFile = open( path + simDir + '/BMPs.txt', 'r' )
    #--------------------table 1------------------------------------------------------------
    bmpInputFile.readline()
    for i in range(0, numWSD-1):
      table1list[i] = bmpInputFile.readline().split('\t')
    bmpInputFile.readline()
    #--------------------table 2------------------------------------------------------------
    bmpInputFile.readline()
    for i in range(0, numWSD-1):
      table2list[i] = bmpInputFile.readline().split('\t')
    bmpInputFile.readline()
    #--------------------table 3------------------------------------------------------------
    bmpInputFile.readline()
    for i in range(0, numWSD-1): 
      table3list[i] = bmpInputFile.readline().split('\t')
    bmpInputFile.readline()
    #--------------------table 4------------------------------------------------------------
    bmpInputFile.readline()
    for i in range(0, numWSD-1): 
      table4list[i] = bmpInputFile.readline().split('\t')
    bmpInputFile.readline()
    #--------------------table 5------------------------------------------------------------
    bmpInputFile.readline()
    for i in range(0, numWSD-1): 
      table5list[i] = bmpInputFile.readline().split('\t')
    bmpInputFile.readline()

    #--------------------table 6------------------------------------------------------------
    #bmpInputFile.readline()
    #for i in range(0, numWSD-1): 
    #  table6list[i] = bmpInputFile.readline().split('\t')
    #bmpInputFile.readline()

    #--------------------urbanTable------------------------------------------------------------
    bmpInputFile.readline()
    bmpInputFile.readline()
    bmpInputFile.readline()
    bmpInputFile.readline()
    bmpInputFile.readline()
    #--------------------urbanBMPTable------------------------------------------------------------
    for k in range(0,5) : 
      for i in range(0,numWSD-1) :
        tableUbBMP[k][i] = bmpInputFile.readline().split('\t')
      bmpInputFile.readline()

    bmpInputFile.close()
  except:
    for i in range(0, numWSD):
      table1list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table2list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table3list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table4list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table5list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]

      table6list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]

      tableurban[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      for k in range(0,5) : 
        for i in range(0,numWSD-1) :
          tableUbBMP[k][i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]


#print numWSD, numGLY, numSTR, ystime, status

#----------------------------------------------------------------------------------Table1
swsOpt = isStr(form.getvalue('swsOpt'))
if ( swsOpt == 'on' or swsOpt == 'chcecked' ) :
  swsOpt = 1 
else :
  swsOpt = 4
LuseAreaWSD = [0.0] * 8
for i in range(1,len(LuseAreaWSD)) : 	 		                        # i = row(1-6), j = wsd num(1-10)
  LuseAreaWSD[i] = [0.0] * numWSD
  for j in range(1,len(LuseAreaWSD[i])) :
    tmpVal = isStr(form.getvalue('LuseAreaWSD_' + isStr(i) + isStr('%02i' % isInt(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      LuseAreaWSD[i][j] = 0.0
    else :
      LuseAreaWSD[i][j] = isFloat(tmpVal)
TAreaWSD = [0.0] * numWSD
PctFeedlot = [0.0] * numWSD 
for i in range(1,len(TAreaWSD)) :
  tmpVal = isStr(form.getvalue('TAreaWSD_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    TAreaWSD[i] = 0.0
  else :
    TAreaWSD[i] = isFloat(tmpVal)
  tmpVal = isStr(form.getvalue('PctFeedlot_' + isStr('%02i'%i)))
  PctFeedlot[i] = isFloat(tmpVal)

#for k in range(0,5) : 
#        for i in range(0,numWSD-1) :
#         print '<li>', tableUbBMP[k][i][0], '-', tableUbBMP[k][i][1], '-', tableUbBMP[k][i][2], '-', tableUbBMP[k][i][3], '-', tableUbBMP[k][i][4], '-', tableUbBMP[k][i][5], '-', tableUbBMP[k][i][6], '-', tableUbBMP[k][i][7], '-', tableUbBMP[k][i][8], '-'
#print '<hr>'
#for i in range(1,numWSD) :
#  print '<li>', PctFeedlot[i]

#----------------------------------------------------------------------------------Table2
Anm = [0.0] * 10
for i in range(1,10) :
  Anm[i] = [0.0] * numWSD 
  for j in range(1,numWSD) :
    tmpVal = isStr(form.getvalue('Animals_' + isStr(i) + isStr('%02i' % isInt(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Anm[i][j] = 0.0
    else :
      Anm[i][j] = isFloat(tmpVal)
for i in range(1,numWSD) :
  tmpVal = isStr(form.getvalue('NumMonManure_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    Anm[9][i] = 0.0
  else :
    Anm[9][i] = isFloat(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', Anm[1][i], '-', Anm[2][i], '-', Anm[3][i], '-', Anm[4][i], '-', Anm[5][i], '-', Anm[6][i], '-', Anm[7][i], '-', Anm[8][i], '-', Anm[9][i]

#----------------------------------------------------------------------------------Table3
NumSpSys = [0.0] * numWSD
PpSpSys = [0.0] * numWSD 
SpFailRate = [0.0] * numWSD 
NumPpDrtDc = [0.0] * numWSD 
RdcDrtDc = [0.0] * numWSD 
for i in range(1,len(NumSpSys)) :
  tmpVal = isStr(form.getvalue('NumSpSys_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    NumSpSys[i] = 0.0
  else :
    NumSpSys[i] = isFloat(tmpVal)
  tmpVal = isStr(form.getvalue('PpSpSys_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    PpSpSys[i] = 0.0
  else :
    PpSpSys[i] = isFloat(tmpVal)
  tmpVal = isStr(form.getvalue('SpFailRate_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    SpFailRate[i] = 0.0
  else :
    SpFailRate[i] = isFloat(tmpVal)
  tmpVal = isStr(form.getvalue('NumPpDrtDc_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    NumPpDrtDc[i] = 0.0
  else :
    NumPpDrtDc[i] = isFloat(tmpVal)
  tmpVal = isStr(form.getvalue('RdcDrtDc_' + isStr('%02i'%i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    RdcDrtDc[i] = 0.0
  else :
    RdcDrtDc[i] = isFloat(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', NumSpSys[i], PpSpSys[i], SpFailRate[i], NumPpDrtDc[i], RdcDrtDc[i]

#----------------------------------------------------------------------------------Table4
usleCropland = [0.0] * 6
uslePasture = [0.0] * 6
usleForest = [0.0] * 6
usleUser = [0.0] * 6

usleWetlands = [0.0] * 6

for i in range(1,len(usleUser)) :
  usleCropland[i] = [0.0] * numWSD
  uslePasture[i] = [0.0] * numWSD 
  usleForest[i] = [0.0] * numWSD 
  usleUser[i] = [0.0] * numWSD 
  usleWetlands[i] = [0.0] * numWSD
  for j in range(1,len(usleUser[i])) :
    tmpVal_1 = isStr(form.getvalue('usleCropland_' + isStr(i) + isStr('%02i' % isInt(j))))
    tmpVal_2 = isStr(form.getvalue('uslePasture_' + isStr(i) + isStr('%02i' % isInt(j))))
    tmpVal_3 = isStr(form.getvalue('usleForest_' + isStr(i) + isStr('%02i' % isInt(j))))
    tmpVal_4 = isStr(form.getvalue('usleUser_' + isStr(i) + isStr('%02i' % isInt(j))))
    tmpVal_5 = isStr(form.getvalue('usleWetlands_' + isStr(i) + isStr('%02i' % isInt(j))))

    if ( tmpVal_1 == 'None' or tmpVal_1 == '' ) :
      usleCropland[i][j] = 0.0
    else :
      usleCropland[i][j] = isFloat(tmpVal_1)
    if ( tmpVal_2 == 'None' or tmpVal_2 == '' ) :
      uslePasture[i][j] = 0.0
    else :
      uslePasture[i][j] = isFloat(tmpVal_2)
    if ( tmpVal_3 == 'None' or tmpVal_3 == '' ) :
      usleForest[i][j] = 0.0
    else :
      usleForest[i][j] = isFloat(tmpVal_3)
    if ( tmpVal_4 == 'None' or tmpVal_4 == '' ) :
      usleUser[i][j] = 0.0
    else :
      usleUser[i][j] = isFloat(tmpVal_4)
    if ( tmpVal_5 == 'None' or tmpVal_5 == '' ) :
      usleWetlands[i][j] = 0.0
    else :
      usleWetlands[i][j] = isFloat(tmpVal_5)     

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
  tmpVal_1 = isStr(form.getvalue('HSG_' + isStr('%02i'%i)))
  tmpVal_2 = isStr(form.getvalue('SoilN_' + isStr('%02i'%i)))
  tmpVal_3 = isStr(form.getvalue('SoilP_' + isStr('%02i'%i)))
  tmpVal_4 = isStr(form.getvalue('SoilB_' + isStr('%02i'%i)))
  if ( tmpVal_1 == 'None' or tmpVal_1 == '' ) :
    HSG[i] = isInt(0)
  else :
    HSG[i] = isInt(tmpVal_1)
  if ( tmpVal_2 == 'None' or tmpVal_2 == '' ) :
    SoilN[i] = isFloat(0)
  else :
    SoilN[i] = isFloat(tmpVal_2)
  if ( tmpVal_3 == 'None' or tmpVal_3 == '' ) :
    SoilP[i] = isFloat(0)
  else :
    SoilP[i] = isFloat(tmpVal_3)
  if ( tmpVal_4 == 'None' or tmpVal_4 == '' ) :
    SoilB[i] = isFloat(0)
  else :
    SoilB[i] = isFloat(tmpVal_4)

#for i in range(1,numWSD) :
#  print '<li>', HSG[i], SoilN[i], SoilP[i], SoilB[i]

#----------------------------------------------------------------------------------Table6
CN = [0.0] * 7                                                                  # CN : general CN
for i in range(len(CN)) :
  CN[i] = [0.0] * 5

CN[1][1] = isFloat(form.getvalue('CN_urban_A'))
CN[1][2] = isFloat(form.getvalue('CN_urban_B'))
CN[1][3] = isFloat(form.getvalue('CN_urban_C'))
CN[1][4] = isFloat(form.getvalue('CN_urban_D'))
CN[2][1] = isFloat(form.getvalue('CN_crop_A'))
CN[2][2] = isFloat(form.getvalue('CN_crop_B'))
CN[2][3] = isFloat(form.getvalue('CN_crop_C'))
CN[2][4] = isFloat(form.getvalue('CN_crop_D'))
CN[3][1] = isFloat(form.getvalue('CN_past_A'))
CN[3][2] = isFloat(form.getvalue('CN_past_B'))
CN[3][3] = isFloat(form.getvalue('CN_past_C'))
CN[3][4] = isFloat(form.getvalue('CN_past_D'))
CN[4][1] = isFloat(form.getvalue('CN_frst_A'))
CN[4][2] = isFloat(form.getvalue('CN_frst_B'))
CN[4][3] = isFloat(form.getvalue('CN_frst_C'))
CN[4][4] = isFloat(form.getvalue('CN_frst_D'))
CN[5][1] = isFloat(form.getvalue('CN_user_A'))
CN[5][2] = isFloat(form.getvalue('CN_user_B'))
CN[5][3] = isFloat(form.getvalue('CN_user_C'))
CN[5][4] = isFloat(form.getvalue('CN_user_D'))

CN[6][1] = isFloat(form.getvalue('CN_wetl_A'))
CN[6][2] = isFloat(form.getvalue('CN_wetl_B'))
CN[6][3] = isFloat(form.getvalue('CN_wetl_C'))
CN[6][4] = isFloat(form.getvalue('CN_wetl_D'))

#----------------------------------------------------------------------------------Table6a
CNu = [0.0] * 10                                                                # CNu : detailed urban CN
for i in range(len(CNu)) :
  CNu[i] = [0.0] * 5

CNu[1][1] = isFloat(form.getvalue('CN_comm_A'))
CNu[1][2] = isFloat(form.getvalue('CN_comm_B'))
CNu[1][3] = isFloat(form.getvalue('CN_comm_C'))
CNu[1][4] = isFloat(form.getvalue('CN_comm_D'))
CNu[2][1] = isFloat(form.getvalue('CN_indu_A'))
CNu[2][2] = isFloat(form.getvalue('CN_indu_B'))
CNu[2][3] = isFloat(form.getvalue('CN_indu_C'))
CNu[2][4] = isFloat(form.getvalue('CN_indu_D'))
CNu[3][1] = isFloat(form.getvalue('CN_inst_A'))
CNu[3][2] = isFloat(form.getvalue('CN_inst_B'))
CNu[3][3] = isFloat(form.getvalue('CN_inst_C'))
CNu[3][4] = isFloat(form.getvalue('CN_inst_D'))
CNu[4][1] = isFloat(form.getvalue('CN_tran_A'))
CNu[4][2] = isFloat(form.getvalue('CN_tran_B'))
CNu[4][3] = isFloat(form.getvalue('CN_tran_C'))
CNu[4][4] = isFloat(form.getvalue('CN_tran_D'))
CNu[5][1] = isFloat(form.getvalue('CN_mult_A'))
CNu[5][2] = isFloat(form.getvalue('CN_mult_B'))
CNu[5][3] = isFloat(form.getvalue('CN_mult_C'))
CNu[5][4] = isFloat(form.getvalue('CN_mult_D'))
CNu[6][1] = isFloat(form.getvalue('CN_sing_A'))
CNu[6][2] = isFloat(form.getvalue('CN_sing_B'))
CNu[6][3] = isFloat(form.getvalue('CN_sing_C'))
CNu[6][4] = isFloat(form.getvalue('CN_sing_D'))
CNu[7][1] = isFloat(form.getvalue('CN_urcu_A'))
CNu[7][2] = isFloat(form.getvalue('CN_urcu_B'))
CNu[7][3] = isFloat(form.getvalue('CN_urcu_C'))
CNu[7][4] = isFloat(form.getvalue('CN_urcu_D'))
CNu[8][1] = isFloat(form.getvalue('CN_vade_A'))
CNu[8][2] = isFloat(form.getvalue('CN_vade_B'))
CNu[8][3] = isFloat(form.getvalue('CN_vade_C'))
CNu[8][4] = isFloat(form.getvalue('CN_vade_D'))
CNu[9][1] = isFloat(form.getvalue('CN_open_A'))
CNu[9][2] = isFloat(form.getvalue('CN_open_B'))
CNu[9][3] = isFloat(form.getvalue('CN_open_C'))
CNu[9][4] = isFloat(form.getvalue('CN_open_D'))

#----------------------------------------------------------------------------------Table7
Rnt = [0.0] * 11                                                        # Nutrient in Runoff
for i in range(len(Rnt)) :
  Rnt[i] = [0.0] * 4

Rnt[1][1] = isFloat(form.getvalue('ntLcrop_1_N'))
Rnt[1][2] = isFloat(form.getvalue('ntLcrop_1_P'))
Rnt[1][3] = isFloat(form.getvalue('ntLcrop_1_B'))
Rnt[2][1] = isFloat(form.getvalue('ntLcrop_2_N'))
Rnt[2][2] = isFloat(form.getvalue('ntLcrop_2_P'))
Rnt[2][3] = isFloat(form.getvalue('ntLcrop_2_B'))
Rnt[3][1] = isFloat(form.getvalue('ntMcrop_1_N'))
Rnt[3][2] = isFloat(form.getvalue('ntMcrop_1_P'))
Rnt[3][3] = isFloat(form.getvalue('ntMcrop_1_B'))
Rnt[4][1] = isFloat(form.getvalue('ntMcrop_2_N'))
Rnt[4][2] = isFloat(form.getvalue('ntMcrop_2_P'))
Rnt[4][3] = isFloat(form.getvalue('ntMcrop_2_B'))
Rnt[5][1] = isFloat(form.getvalue('ntHcrop_1_N'))
Rnt[5][2] = isFloat(form.getvalue('ntHcrop_1_P'))
Rnt[5][3] = isFloat(form.getvalue('ntHcrop_1_B'))
Rnt[6][1] = isFloat(form.getvalue('ntHcrop_2_N'))
Rnt[6][2] = isFloat(form.getvalue('ntHcrop_2_P'))
Rnt[6][3] = isFloat(form.getvalue('ntHcrop_2_B'))
Rnt[7][1] = isFloat(form.getvalue('ntPast_N'))
Rnt[7][2] = isFloat(form.getvalue('ntPast_P'))
Rnt[7][3] = isFloat(form.getvalue('ntPast_B'))
Rnt[8][1] = isFloat(form.getvalue('ntFrst_N'))
Rnt[8][2] = isFloat(form.getvalue('ntFrst_P'))
Rnt[8][3] = isFloat(form.getvalue('ntFrst_B'))
Rnt[9][1] = isFloat(form.getvalue('ntUser_N'))
Rnt[9][2] = isFloat(form.getvalue('ntUser_P'))
Rnt[9][3] = isFloat(form.getvalue('ntUser_B'))

Rnt[10][1] = isFloat(form.getvalue('ntWetl_N'))
Rnt[10][2] = isFloat(form.getvalue('ntWetl_P'))
Rnt[10][3] = isFloat(form.getvalue('ntWetl_B'))

#----------------------------------------------------------------------------------Table7a
Gnt = [0.0] * 8                                                         # Nutrient in Groundwater
for i in range(len(Gnt)) :
  Gnt[i] = [0.0] * 4

Gnt[1][1] = isFloat(form.getvalue('GntUrbn_N'))
Gnt[1][2] = isFloat(form.getvalue('GntUrbn_P'))
Gnt[1][3] = isFloat(form.getvalue('GntUrbn_B'))
Gnt[2][1] = isFloat(form.getvalue('GntCrop_N'))
Gnt[2][2] = isFloat(form.getvalue('GntCrop_P'))
Gnt[2][3] = isFloat(form.getvalue('GntCrop_B'))
Gnt[3][1] = isFloat(form.getvalue('GntPast_N'))
Gnt[3][2] = isFloat(form.getvalue('GntPast_P'))
Gnt[3][3] = isFloat(form.getvalue('GntPast_B'))
Gnt[4][1] = isFloat(form.getvalue('GntFrst_N'))
Gnt[4][2] = isFloat(form.getvalue('GntFrst_P'))
Gnt[4][3] = isFloat(form.getvalue('GntFrst_B'))
Gnt[5][1] = isFloat(form.getvalue('GntFeed_N'))
Gnt[5][2] = isFloat(form.getvalue('GntFeed_P'))
Gnt[5][3] = isFloat(form.getvalue('GntFeed_B'))
Gnt[6][1] = isFloat(form.getvalue('GntUser_N'))
Gnt[6][2] = isFloat(form.getvalue('GntUser_P'))
Gnt[6][3] = isFloat(form.getvalue('GntUser_B'))


Gnt[7][1] = isFloat(form.getvalue('GntWetl_N'))
Gnt[7][2] = isFloat(form.getvalue('GntWetl_P'))
Gnt[7][3] = isFloat(form.getvalue('GntWetl_B'))

#----------------------------------------------------------------------------------Table8
dist = [0.0] * 11					#  9 %, sum %
for i in range(1,len(dist)) :
  dist[i] = [0.0] * numWSD
for i in range(1,len(dist)-1) :
  for j in range(1,len(dist[i])) :
    tmpVal = isStr(form.getvalue('dist_' + isStr(i) + isStr('%02i' % isInt(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      dist[i][j] = 0.0
    else :
      dist[i][j] = isFloat(tmpVal)
for i in range(1,numWSD) :
  dist[10][i] = dist[1][i] + dist[2][i] + dist[3][i] + dist[4][i] + dist[5][i] + dist[6][i] + dist[7][i] + dist[8][i] + dist[9][i] 

#for i in range(1,numWSD) :
#  print '<li>', dist[1][i], dist[2][i], dist[3][i], dist[4][i], dist[5][i], dist[6][i], dist[7][i], dist[8][i], dist[9][i], dist[10][i]

#----------------------------------------------------------------------------------Table9
IrrVal = [0.0] * 5
for i in range(1,len(IrrVal)) :
  IrrVal[i] = [0.0] * numWSD
  for j in range(1,len(IrrVal[i])) :
    tmpVal = isStr(form.getvalue('IrrVal_' + isStr(i) + isStr('%02i' % isInt(j))))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      IrrVal[i][j] = 0.0
    else :
      IrrVal[i][j] = isFloat(tmpVal)

#for i in range(1,numWSD) :
#  print '<li>', IrrVal[1][i], IrrVal[2][i], IrrVal[3][i], IrrVal[4][i]

#----------------------------------------------------------------------------------
#----Reference soil infiltration fraction for precipitation, "Land&Rain" sheet: GW1 table
gwOpt = form.getvalue('gwOpt')
if ( gwOpt == 'on' or gwOpt == 'checked' ) :
  gwOpt = isInt(1)
else : 
  gwOpt = isInt(4) 
gwInft = [0.0] * 6
for i in range(1,6) :
  gwInft[i] = [0.0] * 5
  for j in range(1,len(gwInft[i])) :
    tmpVal = isStr(form.getvalue('gwInft_' + isStr(i) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' or 2 < isInt(gwOpt) ) :
      gwInft[i][j] = 0.0
    else :
      gwInft[i][j] = isFloat(tmpVal)

#----Wildlife density in cropland, "Animal" sheet: Table 2
WildLife = [0] * 6
for i in range(1,len(WildLife)) :
  tmpVal = isStr(form.getvalue('WildLife_' + isStr(i)))
  if ( tmpVal == 'None' or tmpVal == '' ) :
    WildLife[i] = 0.0
  else :
    WildLife[i] = tmpVal

#----Reference, "Reference" sheet: Modified from ASAE, 1998
Reference = [0.0] * 14
for i in range(1,14) :
  Reference[i] = [0.0] * 5
  for j in range(1,len(Reference[i])) :
    tmpVal = isStr(form.getvalue('Reference_' + isStr('%02i' % isInt(i)) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Reference[i][j] = 0.0
    else :
      Reference[i][j] = isFloat(tmpVal)

#----Septic, "Septic" sheet: values between Table 1 and 2
Septic = [0.0] * 8
Septic[0] = isStr(form.getvalue('Septic_11'))
Septic[1] = isStr(form.getvalue('Septic_21'))
Septic[2] = isStr(form.getvalue('Septic_31'))
Septic[3] = isStr(form.getvalue('Septic_41'))
Septic[4] = isStr(form.getvalue('Septic_12'))
Septic[5] = isStr(form.getvalue('Septic_22'))
Septic[6] = isStr(form.getvalue('Septic_32'))
Septic[7] = isStr(form.getvalue('Septic_42'))

#----Feedlot, "Feedlot" sheet: Table (B51-F61)
Feedlot = [0.0] * 12
for i in range(1,len(Feedlot)) :
  Feedlot[i] = [0.0] * 5
  for j in range(1,5) :
    tmpVal = isStr(form.getvalue('Feedlot_' + isStr('%02i' % isInt(i)) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      Feedlot[i][j] = '%.3f' % isFloat(0.0)
    else :
      Feedlot[i][j] = '%.3f' % isFloat(tmpVal)

#----Gully DB 1, "Gully&Streambank" sheet: Table (AC2-AD11, AH2-AH5)
GullyDB = [0.0] * 13
for i in range(1,11) :
  GullyDB[i] = [0.0] * 3
  for j in range(1,3) :
    tmpVal = isStr(form.getvalue('GullyDB_' + isStr('%02i' % isInt(i)) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GullyDB[i][j] = '%.4f' % isFloat(0.0)
    else :
      GullyDB[i][j] = '%.4f' % isFloat(tmpVal)
GullyDB[11] = [0.0] * 2
GullyDB[12] = [0.0] * 2
GullyDB[11][0] = isStr(form.getvalue('GullyDB_111'))
GullyDB[11][1] = isStr(form.getvalue('GullyDB_121'))
GullyDB[12][0] = isStr(form.getvalue('GullyDB_131'))
GullyDB[12][1] = isStr(form.getvalue('GullyDB_141'))
if ( GullyDB[11][0] == 'None' or GullyDB[11][0] == '' ) :
  GullyDB[11][0] = '%.4f' % isFloat(0.0)
else :
  GullyDB[11][0] = '%.4f' % isFloat(GullyDB[11][0])
if ( GullyDB[11][1] == 'None' or GullyDB[11][1] == '' ) :
  GullyDB[11][1] = '%.4f' % isFloat(0.0)
else :
  GullyDB[11][1] = '%.4f' % isFloat(GullyDB[11][1])
if ( GullyDB[12][0] == 'None' or GullyDB[12][0] == '' ) :
  GullyDB[12][0] = '%.4f' % isFloat(0.0)
else :
  GullyDB[12][0] = '%.4f' % isFloat(GullyDB[12][0])
if ( GullyDB[12][1] == 'None' or GullyDB[12][1] == '' ) :
  GullyDB[12][1] = '%.4f' % isFloat(0.0)
else :
  GullyDB[12][1] = '%.4f' % isFloat(GullyDB[12][1])

numGLY = isInt(form.getvalue('numGLY'))
numSTR = isInt(form.getvalue('numSTR'))
GS1 = [0.0] * (numGLY+1) 
for i in range(1,numGLY+1) :
  GS1[i] = [0.0] * 10						# 9 values for gully
  for j in range(1,10) :
    tmpVal = isStr(form.getvalue('GS1_' + isStr('%02i' % isInt(i)) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GS1[i][j] = isFloat(0) 
    else :
      GS1[i][j] = isFloat(tmpVal)

GS2 = [0.0] * (numSTR + 1)
for i in range(1,numSTR+1) :
  GS2[i] = [0.0] * 8
  for j in range(1,8) :
    tmpVal = isStr(form.getvalue('GS2_' + isStr('%02i' % isInt(i)) + isStr(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      GS2[i][j] = isFloat(0.0)
    else :
      GS2[i][j] = isFloat(tmpVal)

for i in range(1,numGLY+1) :
  GS1[i][1] = isInt(GS1[i][1])
  GS1[i][2] = isInt(GS1[i][2])
  GS1[i][9] = isInt(GS1[i][9])
for i in range(1,numSTR+1) :
  GS2[i][1] = isInt(GS2[i][1])
  GS2[i][2] = isInt(GS2[i][2])
  GS2[i][5] = isInt(GS2[i][5])
  GS2[i][7] = isInt(GS2[i][7])

#for i in range(1,numGLY+1) :
#  print '<li>', GS1[i][1], GS1[i][2], GS1[i][3], GS1[i][4], GS1[i][5], GS1[i][6], GS1[i][7], GS1[i][8], GS1[i][9]
#print '<hr>' 
#for i in range(1,numSTR+1) :
#  print '<li>', GS2[i][1], GS2[i][2], GS2[i][3], GS2[i][4], GS2[i][5], GS2[i][6], GS2[i][7]

#--make inpFiles
inpPath = path + 'inp/'
mkINPdir = 'mkdir ' + isStr(inpPath)
chmod777 = 'chmod 777 ' + isStr(inpPath)
os.system(mkINPdir)
os.system(chmod777)

##--myOptPar.pys
#cpOptFile = 'cp ' + path + 'myOptPar.pys ' + inpPath + '.'
#os.system(cpOptFile)


#--mainINP.txt
try:
  mainINPWSD = [0.0] * numWSD

  for i in range(1, numWSD):
    mainINPWSD[i] = open(inpPath + 'mainINP' + str(i) + '.txt', 'w')
    mainINPWSD[i].write('1' + '\t' + isStr(swsOpt) + '\n')
    mainINPWSD[i].write('----------------------------------------------------\n')

  mainINP = open(inpPath + 'mainINP.txt','w')
  mainINP.write(isStr(numWSD-1) + '\t' + isStr(swsOpt) + '\n')
  mainINP.write('----------------------------------------------------\n')
  for i in range(1,numWSD) :                                                    # Table 1
    for j in range(1,7) :
      LuseAreaWSD[j][i] = '%.2f' % isFloat(LuseAreaWSD[j][i])
      mainINP.write(isStr(LuseAreaWSD[j][i]) + '\t')
      mainINPWSD[i].write(isStr(LuseAreaWSD[j][i]) + '\t')
    PctFeedlot[i] = '%.2f' % isFloat(PctFeedlot[i])
    TAreaWSD[i] = '%.2f' % isFloat(TAreaWSD[i])
    mainINP.write(isStr(PctFeedlot[i]) + '\t')
    mainINPWSD[i].write(isStr(PctFeedlot[i]) + '\t')
    mainINP.write(isStr(TAreaWSD[i]) + '\n')
    mainINPWSD[i].write(isStr(TAreaWSD[i]) + '\n')
    mainINPWSD[i].write('----------------------------------------------------\n')
  mainINP.write('----------------------------------------------------\n')

  for i in range(1,numWSD) :                                                    # Table 2
    for j in range(1,10) :
      Anm[j][i] = isInt(Anm[j][i])
      mainINP.write(isStr(Anm[j][i]) + '\t')
      mainINPWSD[i].write(isStr(Anm[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n')
    mainINPWSD[i].write('----------------------------------------------------\n')

  mainINP.write('----------------------------------------------------\n')

  for i in range(1,numWSD) :                                                    # Table 3
    NumSpSys[i] = '%.2f' % isFloat(NumSpSys[i])
    PpSpSys[i] = '%.2f' % isFloat(PpSpSys[i])
    SpFailRate[i] = '%.2f' % isFloat(SpFailRate[i])
    NumPpDrtDc[i] = '%.2f' % isFloat(NumPpDrtDc[i])
    RdcDrtDc[i] = '%.2f' % isFloat(RdcDrtDc[i])
    mainINP.write(isStr(NumSpSys[i]) + '\t')
    mainINP.write(isStr(PpSpSys[i]) + '\t')
    mainINP.write(isStr(SpFailRate[i]) + '\t')
    mainINP.write(isStr(NumPpDrtDc[i]) + '\t')
    mainINP.write(isStr(RdcDrtDc[i]) + '\n')

    mainINPWSD[i].write(isStr(NumSpSys[i]) + '\t')
    mainINPWSD[i].write(isStr(PpSpSys[i]) + '\t')
    mainINPWSD[i].write(isStr(SpFailRate[i]) + '\t')
    mainINPWSD[i].write(isStr(NumPpDrtDc[i]) + '\t')
    mainINPWSD[i].write(isStr(RdcDrtDc[i]) + '\n')
    mainINPWSD[i].write('----------------------------------------------------\n')
  
  mainINP.write('----------------------------------------------------\n')

  for i in range(1,numWSD) :                                                    # Table 4
    for j in range(1,6) :
      usleCropland[j][i] = '%.4f' % isFloat(usleCropland[j][i])
      mainINP.write(isStr(usleCropland[j][i]) + '\t')
      mainINPWSD[i].write(isStr(usleCropland[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n\n')
  mainINP.write('\n')
  for i in range(1,numWSD) :
    for j in range(1,6) :
      uslePasture[j][i] = '%.4f' % isFloat(uslePasture[j][i])
      mainINP.write(isStr(uslePasture[j][i]) + '\t')
      mainINPWSD[i].write(isStr(uslePasture[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n\n')
  mainINP.write('\n')
  for i in range(1,numWSD) :
    for j in range(1,6) :
      usleForest[j][i] = '%.4f' % isFloat(usleForest[j][i])
      mainINP.write(isStr(usleForest[j][i]) + '\t')
      mainINPWSD[i].write(isStr(usleForest[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n\n')
  mainINP.write('\n')
  for i in range(1,numWSD) :
    for j in range(1,6) :
      usleUser[j][i] = '%.4f' % isFloat(usleUser[j][i])
      mainINP.write(isStr(usleUser[j][i]) + '\t')
      mainINPWSD[i].write(isStr(usleUser[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n')
    mainINPWSD[i].write('----------------------------------------------------\n')
  mainINP.write('----------------------------------------------------\n')

  for i in range(1,numWSD) :                                                    # Table 5
    HSG[i] = isInt(HSG[i])
    SoilN[i] = '%.3f' % isFloat(SoilN[i])
    SoilP[i] = '%.3f' % isFloat(SoilP[i])
    SoilB[i] = '%.3f' % isFloat(SoilB[i])
    mainINP.write(isStr(HSG[i]) + '\t' + isStr(SoilN[i]) + '\t' + isStr(SoilP[i]) + '\t' + isStr(SoilB[i]) + '\n')
    mainINPWSD[i].write(isStr(HSG[i]) + '\t' + isStr(SoilN[i]) + '\t' + isStr(SoilP[i]) + '\t' + isStr(SoilB[i]) + '\n')
    mainINPWSD[i].write('----------------------------------------------------\n')
  mainINP.write('----------------------------------------------------\n')

  for i in range(1,6) :                                                           # Table 6
    for j in range(1,5) :
      CN[i][j] = '%.2f' % isFloat(CN[i][j])
      mainINP.write(isStr(CN[i][j]) + '\t')
    mainINP.write('\n')    
  mainINP.write('----------------------------------------------------\n')


  for k in range(1, numWSD) :
    for i in range(1,6) :                                                           # Table 6
      for j in range(1,5) :
        CN[i][j] = '%.2f' % isFloat(CN[i][j])
        mainINPWSD[k].write(isStr(CN[i][j]) + '\t')
      mainINPWSD[k].write('\n')    
    mainINPWSD[k].write('----------------------------------------------------\n')


  for i in range(1,10) :                                                          # Table 6a
    for j in range(1,5) :
      CNu[i][j] = '%.2f' % isFloat(CNu[i][j])
      mainINP.write(isStr(CNu[i][j]) + '\t')
    mainINP.write('\n')
  mainINP.write('----------------------------------------------------\n')

  for k in range(1, numWSD) :
    for i in range(1,10) :                                                           # Table 6a
      for j in range(1,5) :
        CNu[i][j] = '%.2f' % isFloat(CNu[i][j])
        mainINPWSD[k].write(isStr(CNu[i][j]) + '\t')
      mainINPWSD[k].write('\n')    
    mainINPWSD[k].write('----------------------------------------------------\n')


  for i in range(1,10) :                                                          # Table 7
    for j in range(1,4) :
      Rnt[i][j] = '%.3f' % isFloat(Rnt[i][j])
      mainINP.write(isStr(Rnt[i][j]) + '\t')
    mainINP.write('\n')
  mainINP.write('----------------------------------------------------\n')

  for k in range(1, numWSD) :
    for i in range(1,10) :                                                           # Table 7a
      for j in range(1,4) :
        Rnt[i][j] = '%.3f' % isFloat(Rnt[i][j])
        mainINPWSD[k].write(isStr(Rnt[i][j]) + '\t')
      mainINPWSD[k].write('\n')    
    mainINPWSD[k].write('----------------------------------------------------\n')

  for i in range(1,7) :                                                           # Table 7a
    for j in range(1,4) :
      Gnt[i][j] = '%.3f' % isFloat(Gnt[i][j])
      mainINP.write(isStr(Gnt[i][j]) + '\t')
    mainINP.write('\n')    
  mainINP.write('----------------------------------------------------\n')

  for k in range(1, numWSD) :
    for i in range(1,7) :                                                           # Table 6
      for j in range(1,4) :
        mainINPWSD[k].write(isStr(Gnt[i][j]) + '\t')
      mainINPWSD[k].write('\n')    
    mainINPWSD[k].write('----------------------------------------------------\n')


  for i in range(1,numWSD) :                                                    # Table 8
    mainINP.write(isStr(LuseAreaWSD[1][i]) + '\t')
    mainINPWSD[i].write(isStr(LuseAreaWSD[1][i]) + '\t')
    tmpVal = 0.0
    for j in range(1,10) :
      dist[j][i] = '%.2f' % isFloat(dist[j][i])
      tmpVal = isFloat(tmpVal) + isFloat(dist[j][i])
      mainINP.write(isStr(dist[j][i]) + '\t')
      mainINPWSD[i].write(isStr(dist[j][i]) + '\t')
    mainINP.write(isStr('%.2f' % isFloat(tmpVal)))
    mainINP.write('\n')
    mainINPWSD[i].write(isStr('%.2f' % isFloat(tmpVal)))
    mainINPWSD[i].write('\n')
    mainINPWSD[i].write('----------------------------------------------------\n')  
  mainINP.write('----------------------------------------------------\n')

  for i in range(1,numWSD) :                                                    # Table 9
    mainINP.write(isStr(LuseAreaWSD[2][i]) + '\t')
    mainINPWSD[i].write(isStr(LuseAreaWSD[2][i]) + '\t')
    for j in range(1,5) :
      IrrVal[j][i] = '%.2f' % isFloat(IrrVal[j][i])
      mainINP.write(isStr(IrrVal[j][i]) + '\t')
      mainINPWSD[i].write(isStr(IrrVal[j][i]) + '\t')
    mainINP.write('\n')
    mainINPWSD[i].write('\n')
    mainINPWSD[i].write('----------------------------------------------------\n')
    mainINPWSD[i].close()
  mainINP.write('----------------------------------------------------\n')
  mainINP.close()
except:
  mainINP = 0

#--LandRain_GW1.txt
try:
  gwInftFile = open(inpPath + 'LandRain_GW1.txt','w')
  gwInftFile.write('A\tB\tC\tD\tSHG\n')
  for i in range(1,6) :
    for j in range(1,5) :
      gwInft[i][j] = '%.3f' % isFloat(gwInft[i][j])
      gwInftFile.write(isStr(gwInft[i][j]) + '\t')
    gwInftFile.write('\n')
  gwInftFile.close()
except:
  gwInftFile = 0

#--WildLife.txt
try: 
  WildLifeFile = open(inpPath + 'WildLife.txt','w')
  for i in range(1,6) :
    WildLife[i] = '%.2f' % isFloat(WildLife[i])
    WildLifeFile.write(isStr(WildLife[i]) + '\n')
  WildLifeFile.close()
except:
  Wildlife = 0
  
#--Reference.txt
try:
  ReferenceFile = open(inpPath + 'Reference.txt','w')
  ReferenceFile.write('Typical Animal Mass,lb  BOD,lb/day/1000lb animal        BOD per Animal,lb/day   BOD per Animal,lb/yr \n')
  for i in range(1,14) :
    for j in range(1,5) :
      Reference[i][j] = '%.2f' % isFloat(Reference[i][j])
      ReferenceFile.write(isStr(Reference[i][j]) + '\t')
    ReferenceFile.write('\n')
  ReferenceFile.close()
except:
  ReferenceFile = 0
  
#--Septic.txt
try:
  SepticFile = open(inpPath + 'Septic.txt','w')
  SepticFile.write(isStr(0]) + '\n')
  SepticFile.write(isStr(Septic[1]) + '\n')
  SepticFile.write(isStr(Septic[2]) + '\n')
  SepticFile.write(isStr(Septic[3]) + '\n')
  SepticFile.write(isStr(Septic[4]) + '\n')
  SepticFile.write(isStr(Septic[5]) + '\n')
  SepticFile.write(isStr(Septic[6]) + '\n')
  SepticFile.write(isStr(Septic[7]) + '\n')
  SepticFile.close()
except:
  SepticFile = 0
  
#--Feedlot.txt
try:
  FeedlotFile = open(inpPath + 'Feedlot.txt','w')
  FeedlotFile.write('N\tP\tBOD\tCOD\tAnimal\n')
  for i in range(1,12) :
    for j in range(1,5) :
      FeedlotFile.write(isStr(Feedlot[i][j]) + '\t')
    FeedlotFile.write('\n')
  FeedlotFile.close()
except:
  FeedlotFile = 0
  
#--Gully.txt
try:
  GullyFile = open(inpPath + 'Gully.txt','w')
  for i in range(1,11) :
    for j in range(1,3) :
      GullyFile.write(isStr(GullyDB[i][j]) + '\t')
    GullyFile.write('\n')
  GullyFile.write('-----------------------\n')
  GullyFile.write(isStr(GullyDB[11][0]) + '\n' + isStr(GullyDB[11][1]) + '\n')
  GullyFile.write(isStr(GullyDB[12][0]) + '\n' + isStr(GullyDB[12][1]) + '\n')
  GullyFile.write('-----------------------\n')
  GullyFile.write(isStr(numGLY) + '\n')
  for i in range(1,numGLY+1) :
    for j in range(1,10) :
      GullyFile.write(isStr(GS1[i][j]) + '\t')
    GullyFile.write('\n')
  GullyFile.write('-----------------------\n')
  GullyFile.write(isStr(numSTR) + '\n')
  for i in range(1,numSTR+1) :
    for j in range(1,8) :
      GullyFile.write(isStr(GS2[i][j]) + '\t')
    GullyFile.write('\n')
  GullyFile.close()
except:
  GullyFile = 0
  

#--Calculate Annual Direct Runoff Depth (mm)------------------E--

ch777 = 'chmod 777 ' + isStr(inpPath) + '*.*'
os.system(ch777)
ch777 = 'chmod 777 ' + isStr(path) + 'cligen/*.*'
os.system(ch777)
ch777 = 'chmod 777 ' + isStr(path) + 'cligen'
os.system(ch777)
#rmtmp = 'rm -rf ./tmp/1' 
#os.system(rmtmp)
#----E input----------------------------------------------------------------------------------------------------

print '<html>'
print '<head><title>Web-based STEPL</title><meta charset="UTF-8"></head>'
#print '<head><title>', simDir ,'</title><meta charset="UTF-8"></head>'
print '<body onLoad="BMP_LDC();"><br>'

print '<div style="text-align:center"><img src="./img/STEPL_WEB_title.jpg" style="width:400px" alt=""></div><br>'
print '<div style="text-align:center; width:900px; margin: 0 auto; text-align:left;">STEPL WEB has two sources of nutrient loads (N, P, and BOD). The first source is the nutrient loads from landuses, which are computed by pollutant coefficients and annual direct runoff and shallow groundwater contribution. The second source is nutrient loads in sediment, which are computed by soil nutrient concentrations and sediment load. <br><br> Therefore, CNs and soil infiltration fractions should be calibrated for annual direct runoff and annual shallow groundwater so that nutrient loads are correctly computed. Since sediment load is computed by USLE and SDR, the SDR can be calibrated for sediment load.  Pollutant coefficients also need to be calibrated for nutrient loads.</div><br><br>'

#------------------------------------S Button to Open cal_1.cgi-------------------------------------------------
print '<hr>'
print '<table style="width:900px; border:0; margin: 0 auto; text-align=left;">'
print '  <tr>'
print '    <td style="text-align:left; vertical-align:top; padding:5px;">'
print '      <span style="color:tomato; font-family:Times New Roman; font-size:1.5em;">Options:</span></td>'
tmpStr = '   <td style="text-align:left; vertical-align: top; padding:5px "> <input type=button style=\'width:200;height:30;cursor:hand\' value=\'Auto-Calibration\''
tmpStr += ' onClick="javascript:window.open(\'./calopt1.cgi?ystime=' + isStr(ystime)
tmpStr += '&amp;ystimeldc=' + ystimeldc + '\');"></td> '
tmpStr += '<td style="padding:5px"><a href="./P.4.5.html" onclick="window.open(this.href, \'targetwindow\', \'status=no,toolbar=no,width=600px,height=400px\'); return false;">How does Calibration work?</a><br> <span style="color:red; font-style:italic;"> *User must provide Annual Runoff, Annual Baseflow, and Annual load of one or more NPS contaminents. </span><br><span>&nbsp;</span></td>'
tmpStr += '</tr>'
print tmpStr
if ( ystimeldc[0] == '2' and numWSD <= 2 ) :				# only single watershed
  bmpOptBtn = '      <input type=button style=\'width:200;height:30;cursor:hand\' value=\'BMP Optimization-Single\''
  bmpOptBtn += ' onClick="javascript:window.open(\'./bmpopt1.cgi?ystime=' + isStr(ystime)
  bmpOptBtn += '&amp;ystimeldc=' + ystimeldc + '&amp;allPct=' + allPct + '\');"> &nbsp; &nbsp;'
#  print bmpOptBtn
bmpOptBtn2 = ' <tr><td></td><td style="text-align:left; vertical-align: top; padding:5px;"> <input type=button style=\'width:200;height:30;cursor:hand\' value=\'BMP Optimization\''
bmpOptBtn2 += ' onClick="javascript:window.open(\'./multibmp1.cgi?ystime=' + isStr(ystime) + '&numWSD=' + str(numWSD)
bmpOptBtn2 += '&amp;ystimeldc=' + ystimeldc + '&amp;allPct=' + allPct + '\');"> '
bmpOptBtn2 += ' <a href="javascript:alert(\'some video\');"><span>'
bmpOptBtn2 += 'show me how'
bmpOptBtn2 += ' </span><a>'
bmpOptBtn2 += '</td>'

print bmpOptBtn2
print '    </td>'
print '<td  style="padding:5px">'
print 'Purdue STEPL WEB establishes a priority list of BMPs based on implementation cost per mass of pollutant reduction, and then the model performs iterative simulations to identify the most cost-effective BMP implementation plans. The model can import BMP scenarios from the Purdue Load Duration Curve Tool [https://engineering.purdue.edu/mapserve/ldc/] in order to focus on BMPs that are appropriate to address problems in a specific flow regime.'
print '<br><br>Purdue STEPL WEB estimates BMP implementation cost based on establishment, maintenance, and opportunity costs using a cost function (equation 5.12; Arabi et al., 2006). The model computes the costs per unit of pollutant mass reduction for BMPs and establishes a priority list of BMPs to apply based on the cost per unit mass of pollutant reduction. '
print '<br><br><span>c<sub>t</sub> = c<sub>0</sub> &middot; (1 + s)<sup>td</sup> + c<sub>0</sub>   &middot; rm  &middot; [&sum;<sup style="">N</sup><sub style="position: relative; left: -0.6em;"">i=2</sub> (1 + s)<sup>(i - 1)</sup>] <span style="float:right">Eq. 5.12</span>'
print '<br>Where, c<sub>t</sub> is BMP implementation cost, c<sub>0</sub> is establishment cost, rm is ratio of annual maintenance cost to establishment cost, s is interest rate, and td is BMP design life.'
print '<br><br>Since estimated annual cost of BMP implementation in a watershed is computed by BMP cost per unit area and applied area of BMP (AREABMP), both BMP cost and AREABMP need to be considered when identifying the most cost-effective BMP implementation. In other words, the BMP with least cost per unit mass reduction (i.e. dollars per ton of reduction) needs to be identified and applied, and then AREABMP needs to be minimized as long as the estimated reduction meets the required reduction. In addition, use of a BMP on 100% of landuse area may not be possible. For instance, it may not be possible to apply a BMP to 90% of cropland, if the BMP is already applied on 30% of cropland. In this circumstance, the BMP could only be applied to a maximum of 70% of cropland area.'
print '</td>'
print '  </tr>'
print '</table>'
print '<p style="text-align:center;"> <a target="_blank" href="http://docs.lib.purdue.edu/dissertations/AAI3636487/">Park Thesis</a> | <a target="_blank" href="https://engineering.purdue.edu/mapserve/ldc/STEPL/referenceList.html">References</a> </p>'
print '<hr>' 
#------------------------------------E Button to Open cal_1.cgi-------------------------------------------------
#----S use of BMP_LDC.txt---------------------------------------------------------------------------------------
#if ( ystimeldc[0] == '2' ) :								# if from LDC
if ( ystimeldc[0] == '7' ) :  
  try:                                                         # to skip here 
    bmpSgtFile = open('../pldc/tmp/' + ystimeldc + '/BMP_LDC.txt','r')
    bmpSgt = bmpSgtFile.readlines()
    bmpSgtFile.close()
  except:
    bmpSgtFile = 0
  try:
    bmpDBFile = open('./BMPlist.txt','r')
    tmpStr = bmpDBFile.readline()
    bmpInfo = bmpDBFile.readlines()
    bmpDBFile.close()
  except:
    bmpDBFile = 0
    
  for i in range(len(bmpInfo)) :
    bmpInfo[i] = bmpInfo[i].split('\t')

  effArr = [''] * len(bmpSgt)
  for i in range(len(bmpSgt)) :
    bmpSgt[i] = bmpSgt[i].replace('\r','')
    bmpSgt[i] = bmpSgt[i].replace('\n','')
    bmpSgt[i] = bmpSgt[i].split('\t')
    tmpStr_1 = bmpSgt[i][2].replace(' ','')
    for j in range(len(bmpInfo)) : 							# to find efficiencies
      tmpStr_2 = bmpInfo[j][1].replace(' ','')
      if ( isStr(bmpInfo[j][0]) == isStr(bmpSgt[i][0]) and tmpStr_1 == tmpStr_2 ) :
        tmpStr = isStr(bmpInfo[j][-1])							# 1_6 : luse_BMP
      	if ( isInt(tmpStr[0]) < 6 ) :							# if not urban
      	  tmpStr += '_' + isStr(isFloat(bmpInfo[j][2])*isFloat(bmpSgt[i][3])/100.0)
      	  tmpStr += '_' + isStr(isFloat(bmpInfo[j][3])*isFloat(bmpSgt[i][3])/100.0)
      	  tmpStr += '_' + isStr(isFloat(bmpInfo[j][4])*isFloat(bmpSgt[i][3])/100.0)
      	  tmpStr += '_' + isStr(isFloat(bmpInfo[j][5])*isFloat(bmpSgt[i][3])/100.0)
        else :										# if urban
      	  tmpStr += '_' + isStr(bmpInfo[j][2]) + '_' + isStr(bmpInfo[j][3])
      	  tmpStr += '_' + isStr(bmpInfo[j][4]) + '_' + isStr(bmpInfo[j][5])
          tmpStr += '_' + isStr(bmpSgt[i][3])
	effArr[i] = tmpStr
	effArr[i] = effArr[i].replace('\r','')
	effArr[i] = effArr[i].replace('\n','')
#	print '<li>', bmpSgt[i], '::', bmpInfo[j][2], bmpInfo[j][3], bmpInfo[j][4], bmpInfo[j][5], bmpInfo[j][-1]
#  for i in range(len(effArr)) :
#    print '<li>--', effArr[i]

#  print '<br><input type=button style=\'width:200;height:30;cursor:hand\' value=\'Apply Suggested BMPs\' onClick="javascript:BMP_LDC();">' 


#----E use of BMP_LDC.txt---------------------------------------------------------------------------------------

#----------------S BMPinputs------------------------------------------------------------------------------------
print '<form name=bmpMain method="POST" action="./run_1.cgi" target="new1">'
LdcLnkStr = '  <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
print LdcLnkStr

#print '<center>'
print '<table style="width:900px; border:0; margin:0 auto">'
print '  <tr>'
print '    <td style="text-align:left"><span style="font-weight:bold; color:tomato; font-size:1.5em; font-family:Times New Roman">Set BMPs</span>'
print '    <span style=" text-align:left; font-size:0.82em; color:red;" >&nbsp;&nbsp;*BMP for at least ONE Landuse must be selected.</span> </td> '
print '  </tr>'
print '</table>'

tmpStr = '<input type=hidden name=ystime value="' + isStr(ystime) + '">'
print tmpStr
tmpStr = '<input type=hidden name=numWSD value="' + isStr(numWSD) + '">'
print tmpStr

#----CROP
print '  <table border=1 style="width:870px; margin:0 auto">'
print '    <tr>'
print '      <td style="text-align:center" colspan=8><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">CROPLAND</span></div></td>'
print '    </tr>'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Avaliable Area</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">% Area BMP Applied</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">N</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">P</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BOD</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Sediment</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '    <tr>'
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  #Avaliable Area
  tmpStr = LuseAreaWSD[2][i]
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  tmpName = 'BMP_1_' + isStr('%02i' % isInt(i)) + '5'
  tmpName_1 = tmpName
  tmpJava = 'CropBMP_' + isStr('%02i' % isInt(i)) + '();'
  print '      <td style="text-align:center;"><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'

  #Default to NO BMP if area == 0
  if rerun != 2:
    if float(LuseAreaWSD[2][i]) == 0:
      print '                     <option value=1 selected="selected">No BMP'
    else:
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
    tmpName = 'name=BMP_1_' + isStr('%02i' % isInt(i)) + '6'
  else:
    print '                     <option value=1',
    if isInt(isFloat(table1list[i-1][5])) == 1:
      print 'selected="selected"'
    print '>No BMP'
    print '                     <option value=2',
    if isInt(isFloat(table1list[i-1][5])) == 2:
      print 'selected="selected"'
    print'>Combined BMPs-Calculated'
    print '                     <option value=3',
    if isInt(isFloat(table1list[i-1][5])) == 3:
      print 'selected="selected"'
    print'>Contour Farming'
    print '                     <option value=4',
    if isInt(isFloat(table1list[i-1][5])) == 4:
      print 'selected="selected"'
    print'>Diversion'
    print '                     <option value=5',
    if isInt(isFloat(table1list[i-1][5])) == 5:
      print 'selected="selected"'
    print'>Filter strip'
    print '                     <option value=6',
    if isInt(isFloat(table1list[i-1][5])) == 6:
      print 'selected="selected"'
    print'>Reduced Tillage Systems'
    print '                     <option value=7',
    if isInt(isFloat(table1list[i-1][5])) == 7:
      print 'selected="selected"'
    print'>Streambank stabilization and fencing'
    print '                     <option value=8',
    if isInt(isFloat(table1list[i-1][5])) == 8:
      print 'selected="selected"'
    print'>Terrace'
    print '                   </select>'
    print '      </td>'
    tmpName = 'name=BMP_1_' + isStr('%02i' % isInt(i)) + '6'

  if rerun == 2:
    print '    <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 ', tmpName, ' value=', isStr(isFloat(table1list[i-1][4])) ,' onChange="', tmpJava, '"></td>'
    print '      </td>'
    for j in range(1,5) :
      tmpName = 'BMP_1_' + isStr('%02i' % isInt(i)) + isStr(j)
      print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table1list[i-1][j-1])) ,'></td>'
  else:
    print '    <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 ', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
    print '      </td>'
    for j in range(1,5) :
      tmpName = 'BMP_1_' + isStr('%02i' % isInt(i)) + isStr(j)
      print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  
  print '    </tr>'
print '  </table><br>'

#----PAST
print '  <table border=1 style="width:870px; margin: 0 auto">'
print '    <tr>'
print '      <td style="text-align:center;" colspan=8><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">PASTLAND</span></div></td>'
print '    </tr>'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Avaliable Area</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">% Area BMP Applied</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">N</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">P</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BOD</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Sediment</td>'

print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '<tr>'
  print '  <td style="text-align:center;">', tmpStr, '</td>'

  #Avaliable Area
  tmpStr = LuseAreaWSD[3][i]
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '5'
  tmpName_2 = tmpName
  tmpJava = 'PastBMP_' + isStr('%02i' % isInt(i)) + '();'
  print '  <td style="text-align:center;"><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'

  if rerun != 2:
    #Default to NO BMP if area == 0
    if float(LuseAreaWSD[3][i]) == 0:
      print '                     <option value=1 selected="selected">No BMP'
    else:
      print '                     <option value=1>No BMP'

    print '                     <option value=2>Combined BMPs-Calculated'
    print '                     <option value=3>User'
    print '                   </select>'
  else:
    print '                     <option value=1'
    if isInt(isFloat(table2list[i-1][5])) == 1:
      print 'selected="selected"'
    print '>No BMP'
    print '                     <option value=2'
    if isInt(isFloat(table2list[i-1][5])) == 2:
      print 'selected="selected"'
    print '>Combined BMPs-Calculated'
    print '                     <option value=3'
    if isInt(isFloat(table2list[i-1][5])) == 3:
      print 'selected="selected"'
    print '>User'
    print '                   </select>'

  print '  </td>'
  tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '6'

  if rerun == 2:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=', isStr(isFloat(table2list[i-1][4])) ,'onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table2list[i-1][0])) ,'></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table2list[i-1][1])) ,'></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table2list[i-1][2])) ,'></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table2list[i-1][3])) ,'></td>'
  else:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_2_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
 
  print '</tr>'
print '  </table><br>'

#----FRST
print '  <table border=1 style="width:870px; margin:0 auto">'
print '    <tr>'
print '      <td style="text-align:center;" colspan=8><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">FOREST</span></div></td>'
print '    </tr>'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Avaliable Area</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">% Area BMP Applied</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">N</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">P</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BOD</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Sediment</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '<tr>'
  print '  <td style="text-align:center;">', tmpStr, '</td>'

  #Avaliable Area
  tmpStr = LuseAreaWSD[4][i]
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '5'
  tmpName_3 = tmpName
  tmpJava = 'FrstBMP_' + isStr('%02i' % isInt(i)) + '();'
  print '  <td style="text-align:center;"><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'

  #Default to NO BMP if area == 0
  if rerun != 2:
    if float(LuseAreaWSD[4][i]) == 0:
      print '                     <option value=1 selected="selected">No BMP'
    else:
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
  else:
    print '                     <option value=1',
    if isInt(isFloat(table3list[i-1][5])) == 1:
      print 'selected="selected"',
    print '>No BMP'
    print '                     <option value=2'
    if isInt(isFloat(table3list[i-1][5])) == 2:
      print 'selected="selected"'
    print '>Combined BMPs-Calculated'
    print '                     <option value=3'
    if isInt(isFloat(table3list[i-1][5])) == 3:
      print 'selected="selected"'
    print '>Road dry seeding'
    print '                     <option value=4'
    if isInt(isFloat(table3list[i-1][5])) == 4:
      print 'selected="selected"'
    print '>Road grass and legume seeding'
    print '                     <option value=5'
    if isInt(isFloat(table3list[i-1][5])) == 5:
      print 'selected="selected"'
    print '>Road grass and legume seeding-New'
    print '                     <option value=6'
    if isInt(isFloat(table3list[i-1][5])) == 6:
      print 'selected="selected"'
    print '>Road hydro mulch'
    print '                     <option value=7'
    if isInt(isFloat(table3list[i-1][5])) == 7:
      print 'selected="selected"'
    print '>Road straw mulch'
    print '                     <option value=8'
    if isInt(isFloat(table3list[i-1][5])) == 8:
      print 'selected="selected"'
    print '>Road tree planting'
    print '                     <option value=9'
    if isInt(isFloat(table3list[i-1][5])) == 9:
      print 'selected="selected"'
    print '>Site preparation/hydro mulch/seed/fertilizer'
    print '                     <option value=10'
    if isInt(isFloat(table3list[i-1][5])) == 10:
      print 'selected="selected"'
    print '>Site preparation/hydro mulch/seed/fertilizer/transplants'
    print '                     <option value=11'
    if isInt(isFloat(table3list[i-1][5])) == 11:
      print 'selected="selected"'
    print '>Site preparation/steep slope seeder/transplant'
    print '                     <option value=12'
    if isInt(isFloat(table3list[i-1][5])) == 12:
      print 'selected="selected"'
    print '>Site preparation/straw/crimp seed/fertilizer/transplant'
    print '                     <option value=13'
    if isInt(isFloat(table3list[i-1][5])) == 13:
      print 'selected="selected"'
    print '>Site preparation/straw/crimp/net'
    print '                     <option value=14'
    if isInt(isFloat(table3list[i-1][5])) == 14:
      print 'selected="selected"'
    print '>Site preparation/straw/net/seed/fertilizer/transplant'
    print '                     <option value=15'
    if isInt(isFloat(table3list[i-1][5])) == 15:
      print 'selected="selected"'
    print '>Site preparation/straw/polymer/seed/fertilizer/transplant'

  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '6'

  if rerun == 2:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=', isStr(isFloat(table3list[i-1][4])) ,' onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table3list[i-1][0])) ,'></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table3list[i-1][1])) ,'></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table3list[i-1][2])) ,'></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table3list[i-1][3])) ,'></td>'
    print '</tr>'
  else:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_3_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    print '</tr>'
  
print '  </table><br>'



#----USER
print '  <table border=1 style="width:870px; margin: 0 auto">'
print '    <tr>'
print '      <td style="text-align:center;" colspan=8><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">USER DEFINED</span></div></td>'
print '    </tr>'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Avaliable Area</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">% Area BMP Applied</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">N</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">P</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BOD</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Sediment</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '<tr>'
  print '  <td style="text-align:center;">', tmpStr, '</td>'

  #Avaliable Area
  tmpStr = LuseAreaWSD[5][i]
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '5'
  tmpName_4 = tmpName
  tmpJava = 'UserBMP_' + isStr('%02i' % isInt(i)) + '();'
  print '  <td style="text-align:center;"><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'

  if rerun != 2:
    #Default to NO BMP if area == 0
    if float(LuseAreaWSD[5][i]) == 0:
      print '                     <option value=1 selected="selected">No BMP'
    else:
      print '                     <option value=1>No BMP'

    print '                     <option value=2>Combined BMPs-Calculated'
  else:
    print '                     <option value=1'
    if isInt(isFloat(table4list[i-1][5])) == 1:
      print 'selected="selected"'
    print '>No BMP'
    print '                     <option value=2'
    if isInt(isFloat(table4list[i-1][5])) == 2:
      print 'selected="selected"'
    print '>Combined BMPs-Calculated'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '6'

  if rerun == 2:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=', isStr(isFloat(table4list[i-1][4])) ,'onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table4list[i-1][0])) ,'></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table4list[i-1][1])) ,'></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table4list[i-1][2])) ,'></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', isStr(isFloat(table4list[i-1][3])) ,'></td>'
    print '</tr>'
  else:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
    print '  </td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '1'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '2'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '3'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    tmpName = 'BMP_4_' + isStr('%02i' % isInt(i)) + '4'
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
    print '</tr>'
print '  </table><br>'

#----FEED
print '  <table border=1 style="width:870px; margin:0 auto">'
print '    <tr>'
print '      <td style="text-align:center;" colspan=8><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">FEEDLOT</span></div></td>'
print '    </tr>'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Avaliable Area</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">% Area BMP Applied</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">N</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">P</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BOD</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Sediment</td>'
print '    </tr>'
for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '<tr>'
  print '  <td style="text-align:center;">', tmpStr, '</td>'

  #Avaliable Area
  tmpStr = LuseAreaWSD[6][i]
  print '      <td style="text-align:center;">', tmpStr, '</td>'

  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '5'
  tmpName_5 = tmpName
  tmpJava = 'FeedBMP_' + isStr('%02i' % isInt(i)) + '();'
  print '  <td style="text-align:center"><select name=', tmpName, ' onChange="', tmpJava, '">'
  print '                     <option value=0>Select'

  if rerun != 2:
    #Default to NO BMP if area == 0
    if float(LuseAreaWSD[6][i]) == 0:
      print '                     <option value=1 selected="selected">No BMP'
    else:
      print '                     <option value=1>No BMP'

    print '                     <option value=2>Diversion'
    print '                     <option value=3>Filter strip'
    print '                     <option value=4>Runoff Mgmt System'
    print '                     <option value=5>Solids Separation Basin'
    print '                     <option value=6>Solids Separation Basin w/Infilt Bed'
    print '                     <option value=7>Terrace'
    print '                     <option value=8>Waste Mgmt System'
    print '                     <option value=9>Waste Storage Facility'
  else:
    print '                     <option value=1'
    if isInt(isFloat(table5list[i-1][5])) == 1:
      print 'selected="selected"'
    print '>No BMP'
    print '                     <option value=2'
    if isInt(isFloat(table5list[i-1][5])) == 2:
      print 'selected="selected"'
    print '>Diversion'
    print '                     <option value=3'
    if isInt(isFloat(table5list[i-1][5])) == 3:
      print 'selected="selected"'
    print '>Filter strip'
    print '                     <option value=4'
    if isInt(isFloat(table5list[i-1][5])) == 4:
      print 'selected="selected"'
    print '>Runoff Mgmt System'
    print '                     <option value=5'
    if isInt(isFloat(table5list[i-1][5])) == 5:
      print 'selected="selected"'
    print '>Solids Separation Basin'
    print '                     <option value=6'
    if isInt(isFloat(table5list[i-1][5])) == 6:
      print 'selected="selected"'
    print '>Solids Separation Basin w/Infilt Bed'
    print '                     <option value=7'
    if isInt(isFloat(table5list[i-1][5])) == 7:
      print 'selected="selected"'
    print '>Terrace'
    print '                     <option value=8'
    if isInt(isFloat(table5list[i-1][5])) == 8:
      print 'selected="selected"'
    print '>Waste Mgmt System'
    print '                     <option value=9'
    if isInt(isFloat(table5list[i-1][5])) == 9:
      print 'selected="selected"'
    print '>Waste Storage Facility'
  print '                   </select>'
  print '  </td>'
  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '6'

  if rerun == 2:
    print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=', isStr(isFloat(table5list[i-1][4])) ,'onChange="', tmpJava, '"></td>'
  else:
    print '  <td style="text-align:center"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=10 name=', tmpName, ' value=100.0', ' onChange="', tmpJava, '"></td>'
  
  print '  </td>'
  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '1'
  print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '2'
  print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '3'
  print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'BMP_5_' + isStr('%02i' % isInt(i)) + '4'
  print '  <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  print '</tr>'
print '  </table><br>'


print '<table style="width:870px; margin:0 auto" border=1>'
print '  <tr>'
print '    <td style="text-align:center;" colspan=12><div style="color:blue;">BMPs and efficiencies for different pollutants on <span style="font-weight:bold">Urban</span></div></td>'
print '  </tr>'

print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">BMPs</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Commercial</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Industrial</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Institutional</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Transportation</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Multi-Family</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Single-Family</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Urban-Cultivated</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Vacant (developed)</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-weight:bold">Open Space</td>'

print '    </tr>'

for i in range(1,numWSD) :
  tmpStr = 'W' + isStr(i)
  print '<tr>'
  print '  <td style="text-align:center;">', tmpStr, '</td>'

  if rerun != 2:
    #Default to NO BMP if area == 0
    if float(LuseAreaWSD[1][i]) == 0:
      print '                     <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=urBMP_' + str(i), 'value="No BMP" readonly></td>'
    else:
      print '                     <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt;" size=4 name=urBMP_' + str(i), 'value="Select BMP" readonly></td>' 

    for j in range(1,10) :
      tmpName = 'UrbanBMP_1_0' + str('%02i' % int(i)) + str(j) 
      tmpStr = ' onClick="javascript:window.open(\'./urBMP.cgi?numWSD=' + isStr(numWSD)
      tmpStr = tmpStr + '\',\'UrbanBMP\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=600,width=980\');"'
      print '    <td align=center>'
      print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0', tmpStr, ' >'
      print '    </td>'
  else:
    #Default to NO BMP if area == 0
    if float(LuseAreaWSD[1][i]) == 0:
      print '                     <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=urBMP_' + str(i), 'value="No BMP" readonly></td>'
    else:
      flag = 0
      for j in range(1,10):
        if tableUbBMP[0][i-1][j-1] * 1 != 0:
          flag = 1
      if flag == 0:
        print '                     <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt;" size=4 name=urBMP_' + str(i), 'value="Select BMP" readonly></td>' 
      else:
        print '                     <td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt;" size=4 name=urBMP_' + str(i), 'value="Selected" readonly></td>' 
      

    for j in range(1,10) :
      tmpName = 'UrbanBMP_1_0' + str('%02i' % int(i)) + str(j) 
      tmpStr = ' onClick="javascript:window.open(\'./urBMP.cgi?numWSD=' + isStr(numWSD)
      tmpStr = tmpStr + '\',\'UrbanBMP\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=600,width=980\');"'
      print '    <td align=center>'
      print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=', isStr(isFloat(tableUbBMP[0][i-1][j-1])) ,'', tmpStr, ' >'
      print '    </td>'

  print '  </tr>'


print '  <tr>'
print '    <td style="text-align:center" colspan=12>'
tmpStr = '    <input type=button style=\'width:200;height:30;cursor:hand\' value=\'Set Urban BMPs\''
tmpStr = tmpStr + ' onClick="javascript:window.open(\'./urBMP.cgi?numWSD=' + isStr(numWSD)
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
# 1: area, 2: N, 3: P, 4: BOD, 5: TSS -> k , 	BMP_k_0ij
for k in range(1,6) : 
  for i in range(1,numWSD) :
    for j in range(1,10) : 		# 9 distribution
      if rerun != 2:
        tmpStr = '<input type=hidden size=4 name=UrbanBMP_' + isStr(k) + '_' + isStr('%02i'%i) + isStr(j) + ' value=0.0>'
      else:
        #tmpStr = '<input type=hidden size=4 name=UrbanBMP_' + isStr(k) + '_' + isStr('%02i'%i) + isStr(j) + ' value=0.0>'
        tmpStr = '<input type=hidden size=4 name=UrbanBMP_' + isStr(k) + '_' + isStr('%02i'%i) + isStr(j) + ' value='+ isStr(isFloat(tableUbBMP[k-1][i-1][j-1])) +'>'
      print tmpStr

#----Urban BMPs info, just to keep the information of Urban info. not for cgi
for i in range(1,numWSD) :
  for j in range(1,10) :
    InfoStr = '<input type=hidden size=4 name=UrbanBMPinfo_' + isStr('%02i'%i) + isStr(j) + ' value=0>'
    print InfoStr



print '<div style="text-align:center"><br><input style="WIDTH:200;height:30;CURSOR:hand" type=button onClick="complete()" value="Next"><br><br></div>'

print '</form>'
#----------------E BMPinputs------------------------------------------------------------------------------------
#------------------------------S BMP_ListForm.txt---------------------------------------------------------------
try:
  bmpListFile = open('./BMP_ListForm.txt','r')
except:
  bmpListFile = 0
bmpList = bmpListFile.readlines()
bmpListFile.close()
for i in range(len(bmpList)) :
  bmpList[i] = bmpList[i].replace('\n','')
  print bmpList[i]
#------------------------------E BMP_ListForm.txt---------------------------------------------------------------
#----S ubForm---------------------------------------------------------------------------------------------------
print '<form name=ubForm>'		# for urBMP.cgi
for i in range(1,numWSD) :
  for j in range(1,10) :		# 9 distribution percent values
    tmpStr = '<input type=hidden name=ubDis_' + isStr('%02i'%i) + isStr(j) + ' value="' + isStr(dist[j][i]) + '" size=2>'
    print tmpStr
for i in range(1,numWSD) :
  tmpStr = '<input type=hidden name=ubArea_' + isStr('%02i'%i) + ' value="' + isStr(LuseAreaWSD[1][i]) + '" size=2>'
  print tmpStr

print '</form>'

# 20150617
#----E ubForm---------------------------------------------------------------------------------------------------
print '<div style="text-align:center"><hr>'
print '<div style="font-size:0.82em">'
print '  <div style="color:gray">'
print '    Copyright &copy; 2015, Purdue University and Kangwon National University, all rights reserved. <br>'
print '    Purdue University is an equal access/equal opportunity university.<br>'
print '  </div>'
print '  Contact <a href=mailto:engelb@purdue.edu>Dr. Bernie Engel</a>'
print '  or <a href=mailto:theller@purdue.edu>Larry Theller</a> for more details if you need any help with STEPL WEB.'
print '  <br>'
print '  This implementation of the classic EPA model was designed by Dr. <a href=mailto:ysparkwithyou@gmail.com>Youn Shik Park</a>, Assistant Professor, Kongju National University, South-Korea.'
print '  <br>Programmatic support from US EPA, Illinois-Indiana Sea Grant,  and US Army Corp of Engineers.'
print '</div></div><br>'



#----S JavaScript-----------------------------------------------------------------------------------------------
print '<script language="JavaScript">'
for i in range(1,numWSD) :
  tmpStr = 'function CropBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_1_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_1_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_1_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,9) :         # 8 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_1_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_1_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.CROP_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function PastBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_2_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_2_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_2_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,4) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_2_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_2_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.PAST_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function FrstBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_3_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_3_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_3_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,16) :         # 15 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_3_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_3_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.FRST_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function UserBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_4_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_4_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_4_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,3) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_4_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_4_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.USER_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function FeedBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_5_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_5_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_5_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,10) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_5_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_5_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.FEED_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'

for i in range(1,numWSD) :
  tmpStr = 'function WetlBMP_' + isStr('%02i'%i) + '() {'
  print tmpStr
  tmpStr = '  var myRatio = document.bmpMain.BMP_6_' + isStr('%02i'%i) + '6.value * 0.01 ;'
  print tmpStr
  tmpStr = '  if ( document.bmpMain.BMP_6_' + isStr('%02i'%i) + '5.selectedIndex == \'0\' ) {'
  print tmpStr
  for j in range(1,5) :         # set "0"
    tmpStr = '    document.bmpMain.BMP_6_' + isStr('%02i'%i) + isStr(j) + '.value = 0.0 ;'
    print tmpStr
  for j in range(1,3) :         # 3 bmps for cropland
    tmpStr = '  } else if ( document.bmpMain.BMP_6_' + isStr('%02i'%i) + '5.selectedIndex == \'' + isStr(j) + '\' ) {' 
    print tmpStr
    for k in range(1,5) :     # N, P, BMD, Sed.
      tmpStr = '    document.bmpMain.BMP_6_' + isStr('%02i'%i) + isStr(k) + '.value = document.BMP_List.WETL_' + isStr('%02i'%j) + isStr(k) + '.value * myRatio ;'
      print tmpStr
  print '  }'
  print '}'


#---- BMP by LDC
print 'function BMP_LDC() {'
if ( ystimeldc[0] == '7' ) :							# to skip here
#if ( ystimeldc[0] == '2' ) :
  for i in range(len(effArr)) :
    effArr[i] = effArr[i].split('_')
			# effArr: 'luse code', 'BMP code', 'N eff', 'P eff', 'B eff', 'S eff', 'area suggested %'
    if ( isInt(effArr[i][0]) < 6 ) : 				# excluding Urban
      for j in range(1,numWSD) :
        bmpStr = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '5.value = ' + isStr(effArr[i][1]) + ';'
        N_Str = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '1.value = ' + isStr(effArr[i][2]) + ';'
        P_Str = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '2.value = ' + isStr(effArr[i][3]) + ';'
        B_Str = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '3.value = ' + isStr(effArr[i][4]) + ';'
        S_Str = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '4.value = ' + isStr(effArr[i][5]) + ';'
        areaStr = '  document.bmpMain.BMP_' + isStr(effArr[i][0]) + '_' + isStr('%02i'%j) + '6.value = ' + isStr(effArr[i][6]) + ';'
        print bmpStr
        print N_Str
        print P_Str
        print B_Str
        print S_Str
        print areaStr
    else :							# Urban
      # UrbanBMP_k_ij, k: 1 for area, 2 for N, 3 for P, 4 for BOD, 5 for S
      #		       o: watershed
      #		       j: 9 dist. of urban
      SgtPct = isFloat(effArr[i][6])				# percentage to apply
      for o in range(1,numWSD) :				# wsd
	for j in range(1,10) :					# 9 dist. of urban
	  tmpVal_1 = isFloat(LuseAreaWSD[1][o])
	  tmpVal_2 = isFloat(dist[j][o])
	  tmpVal_3 = isFloat(effArr[i][6])
	  tmpVal_4 = tmpVal_1 * tmpVal_2 / 100.0 * tmpVal_3 / 100.0
	  jsStrArea = '  document.bmpMain.UrbanBMP_1_' + isStr('%02i'%o) + isStr(j) + '.value = ' + isStr(tmpVal_4) + ';'
          jsStrN = '  document.bmpMain.UrbanBMP_2_' + isStr('%02i'%o) + isStr(j) + '.value = ' + isStr(effArr[i][2]) + ';'
	  jsStrP = '  document.bmpMain.UrbanBMP_3_' + isStr('%02i'%o) + isStr(j) + '.value = ' + isStr(effArr[i][3]) + ';'
	  jsStrB = '  document.bmpMain.UrbanBMP_4_' + isStr('%02i'%o) + isStr(j) + '.value = ' + isStr(effArr[i][4]) + ';'
	  jsStrS = '  document.bmpMain.UrbanBMP_5_' + isStr('%02i'%o) + isStr(j) + '.value = ' + isStr(effArr[i][5]) + ';'
	  print jsStrArea
	  print jsStrN
	  print jsStrP
	  print jsStrB
	  print jsStrS
          
	  # UrbanBMPinfo
          jsStrBMPinfo = '  document.bmpMain.UrbanBMPinfo_' + isStr('%02i'%o) + isStr(j) + '.value = "' + isStr(effArr[i][1]) + '" ;'
	  print jsStrBMPinfo


print '}'

print 'function complete() {   '
print ' var flag = 0;'
for i in range(1,numWSD) :
  print ' if ( document.bmpMain.urBMP_' + str(i) + '.value == "Select BMP" )'
  print '   flag = 1; '
print ' if( ( document.bmpMain.' + tmpName_1 + '.value * 1 == 0 ) || ( document.bmpMain.' + tmpName_2  + '.value * 1 == 0 ) '
print '   || ( document.bmpMain.' + tmpName_3 + '.value * 1 == 0 ) || ( document.bmpMain.' + tmpName_4 + '.value * 1 == 0 ) '
print '   || ( document.bmpMain.' + tmpName_5 + '.value * 1  == 0 )  || ( flag == 1 ) ) '
#print ' if (flag == 1) '
print '   alert( "Please select a BMP" ); '
#print ' alert(document.bmpMain.' + tmpName_6 + '.value * 1) '
print ' else '
print '    document.bmpMain.submit();'
print '}   '

print '</script>'
#----E JavaScript-----------------------------------------------------------------------------------------------









print '</body>'
print '</html>'


