#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob, locale
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
ystimeldc = str(form.getvalue('ystimeldc'))
allPct = float(form.getvalue('allPct'))
sltWQname = str(form.getvalue('sltWQname'))
numWSD = int(form.getvalue('numWSD'))
rankArr = str(form.getvalue('rankArrAll'))

rankArr = rankArr.split('____')
rankArr.pop(-1)

maxAreaPct = [0.0] * 6
for i in range(len(maxAreaPct)) :
  tmpStr1 = str(form.getvalue('maxAreaPct_' + str(i)))
  if ( tmpStr1 != '' and tmpStr1[0] != 'N' and tmpStr1[0] != 'n' ) :
    maxAreaPct[i] = int(tmpStr1)

#---get UrbnConc, BMPs.txt
BMPset_2 = [0.0] * 5
for i in range(1,5) :
  BMPset_2[i] = [0.0] * 10
  for j in range(1,10) :
    tmpVal = str(form.getvalue('UrbnConc_' + str(i) + str(j)))
    if ( tmpVal == 'None' or tmpVal == '' ) :
      BMPset_2[i][j] = '%.4f' % float(0.0)
    else :
      BMPset_2[i][j] = '%.4f' % float(tmpVal)

path = './tmp/' + ystime + '/opt/'

#print '<li>', ystime
#print '<li>', ystimeldc
#print '<li>', allPct
#print '<li>', sltWQname
#print '<li>', rankArr
#print '<li>', maxAreaPct
#----E input----------------------------------------------------------------------------------------------------
#----------------S declare array--------------------------------------------------------------------------------
for i in range(len(rankArr)) :
  rankArr[i] = rankArr[i].split('__')
  rankArr[i][3] = float(rankArr[i][3])							# luse, bmp, cost, eff. N, P, B, S
  rankArr[i][4] = float(rankArr[i][4]) 
  rankArr[i][5] = float(rankArr[i][5])
  rankArr[i][6] = float(rankArr[i][6])
  #print '<li>', rankArr[i]


#---urban dist.
mainINPfile = open(path + 'mainINP.txt','r')
tmpArr1 = mainINPfile.readlines()
mainINPfile.close()

dashCnt = 0
dashLne = 1
urbnDist = ''
for i in range(len(tmpArr1)) :
  tmpArr1[i] = tmpArr1[i].replace('\r','')
  tmpArr1[i] = tmpArr1[i].replace('\n','')
  if ( 1 < len(tmpArr1[i]) and tmpArr1[i][0] == '-' ) :
    dashCnt += 1
  if ( dashCnt == 10 ) :
    dashLne = i

urbnDist = tmpArr1[dashLne] 
urbnDist = urbnDist.split('\t')

areaWSD = tmpArr1[2]
#----------------E declare array--------------------------------------------------------------------------------
#-----------------------------------S BMPset_2, urban concentration values, fixed-------------------------------
urbnConcArr = [''] * 4
for i in range(1,len(BMPset_2)) :
  urbnConcStr = ''
  for j in range(1,len(BMPset_2[i])-1) :
    urbnConcStr += str(BMPset_2[i][j]) + '\t'
  urbnConcStr += str(BMPset_2[i][-1])
  urbnConcArr[i-1] = urbnConcStr + '\n'

#for i in range(len(urbnConcArr)) :
#  print '<li>', urbnConcArr[i]

#-----------------------------------E BMPset_2, urban concentration values, fixed-------------------------------
#---S def urbn area---------------------------------------------------------------------------------------------
def urbnArea(urbnDist,ATA) : 
  urbnStr = '' 
  for j in range(1,len(urbnDist)-2) :
    tmpVal1 = float(urbnDist[j]) * float(urbnDist[0]) / 100.0 * ATA / 100.0
    tmpVal1 = '%.4f'%tmpVal1
    urbnStr += str(tmpVal1) + '\t'
  tmpVal1 = float(urbnDist[-2]) * float(urbnDist[0]) / 100.0 * ATA / 100.0
  tmpVal1 = '%.4f'%tmpVal1
  urbnStr += str(tmpVal1)

#  print '<li>aaaaaaa', urbnStr
  return urbnStr
    
#ATA = 41.96
#urbnStr = ''
#urbnStr = urbnArea(urbnDist,ATA)
#---E def urbn area---------------------------------------------------------------------------------------------
#--------------------------------------------S default myBMPset-------------------------------------------------
myBMPset = []
header = '\tN\tP\tBOD\tSediment\tAppliedArea\n'
zeroEff1 = '0.0000\t0.0000\t0.0000\t0.0000\t100.0000\n'                                       # no BMP for non-urban
zeroEff2 = '0.0000\t0.0000\t0.0000\t0.0000\t0.0000\t0.0000\t0.0000\t0.0000\t0.0000\n'         # no BMP for urban
for i in range(4) :
  myBMPset.append(header)
  myBMPset.append(zeroEff1)
  myBMPset.append('\n')
myBMPset.append(header)
myBMPset.append(zeroEff1)
myBMPset.append('------------ Followings are BMPs for Urban-------------------------------------------------\n')
for i in range(len(urbnConcArr)) :
  myBMPset.append(urbnConcArr[i])

urbnStr = urbnArea(urbnDist,100)
myBMPset.append('\n')
myBMPset.append(urbnStr + '\n')
myBMPset.append('\n')

for i in range(4) :
  myBMPset.append(zeroEff2)
  myBMPset.append('\n')

#print '<pre>'
#for i in range(len(myBMPset)) :
#  print '<li>', myBMPset[i]
#--------------------------------------------E default myBMPset-------------------------------------------------
#-----------------------S update myBMPset-----------------------------------------------------------------------
def updateBMPset(myBMPset,rankArr,urbnConcStr,urbnDist,ATA) :
  #print '<li>', rankArr[0]
  if ( rankArr[0] == 'Urban' ) :
    urbnStr = urbnArea(urbnDist,ATA)
    myBMPset[20] = urbnStr + '\n'
    nVal = ''
    pVal = ''
    bVal = ''
    sVal = ''
    for i in range(8) :
      nVal += '%.4f'%float(rankArr[3]) + '\t'
      pVal += '%.4f'%float(rankArr[4]) + '\t'
      bVal += '%.4f'%float(rankArr[5]) + '\t'
      sVal += '%.4f'%float(rankArr[6]) + '\t'
    nVal += '%.4f'%float(rankArr[3]) + '\n'
    pVal += '%.4f'%float(rankArr[4]) + '\n'
    bVal += '%.4f'%float(rankArr[5]) + '\n'
    sVal += '%.4f'%float(rankArr[6]) + '\n'

    myBMPset[22] = nVal
    myBMPset[24] = pVal
    myBMPset[26] = bVal
    myBMPset[28] = sVal

  #---update bmp eff. Cropland
  else :
    nVal = float(rankArr[3]) * float(ATA) / 100.0
    pVal = float(rankArr[4]) * float(ATA) / 100.0
    bVal = float(rankArr[5]) * float(ATA) / 100.0
    sVal = float(rankArr[6]) * float(ATA) / 100.0
    nonBMPeffStr = str('%.4f'%nVal) + '\t' + str('%.4f'%pVal) + '\t'
    nonBMPeffStr += str('%.4f'%bVal) + '\t' + str('%.4f'%sVal) + '\t' + str(int(ATA+0.5)) + '\n'

    if ( rankArr[0] == 'Cropland' ) :
      myBMPset[1] = nonBMPeffStr 
    if ( rankArr[0] == 'Forest' ) :
      myBMPset[7] = nonBMPeffStr
    elif ( rankArr[0] == 'Feedlots' ) :
      myBMPset[13] = nonBMPeffStr

  return myBMPset

#-----------------------E update myBMPset-----------------------------------------------------------------------
#---S write BMPs.txt--------------------------------------------------------------------------------------------
def writeBMPs(myBMPset,path) :
  bmp = open(path + 'BMPs.txt','w')
  for i in range(len(myBMPset)) :
#    print '<li>', i, '::', myBMPset[i]
    bmp.write(myBMPset[i]) 
  bmp.close()
#---E write BMPs.txt--------------------------------------------------------------------------------------------
#-----------------------------------------S read STEPL rst------------------------------------------------------
def readRst(path,sltWQname) :
  rstFile = open(path + 'myRST.csv','r')
  rst = rstFile.readlines()
  rstFile.close()

  clm = -4
  if ( sltWQname[0] == 'P' ) :
    clm = -3
  elif ( sltWQname[0] == 'B' ) :
    clm = -2
  elif ( sltWQname[0] == 'S' ) :
    clm = -1

  myRdc1 = rst[-1].split()
  myRdc2 = float(myRdc1[clm])
  #myRdc2 = str(myRdc1[-4]) + '__' + str(myRdc1[-3]) + '__' + str(myRdc1[-2]) + '__' + str(myRdc1[-1])
  
  return myRdc2

#-----------------------------------------E read STEPL rst------------------------------------------------------
#---S loop------------------------------------------------------------------------------------------------------
#maxAreaPct
#allPct

for i in range(len(maxAreaPct)) :
  if ( 100.0 < maxAreaPct[i] ) :
    maxAreaPct[i] = 100

rankArr_ATA = [0.0] * len(rankArr)

#---run first rankArr
upBdr = 0
for i in range(upBdr, upBdr+1) :
  myRdc = [0.0] * 20
  maxRdc = 0.0
  for j in range(10,maxAreaPct[upBdr]+5,5) :
    myBMPset = updateBMPset(myBMPset,rankArr[i],urbnConcStr,urbnDist,j)
    writeBMPs(myBMPset,path)
    os.chdir(path)
    os.system('./stepl_amc')
    os.chdir('../../../')
    myRdc[j/5-2] = readRst(path,sltWQname)
    if ( maxRdc < myRdc[j/5-2] ) :
      maxRdc = myRdc[j/5-2]
#    print '<li>', rankArr[upBdr][0], '::', j,  myRdc[j/5-2]
  for j in range(1,len(myRdc)) :
    if ( myRdc[j-1] < allPct and allPct <= myRdc[j] ) : 
      rankArr_ATA[upBdr] = ( j + 2 ) * 5
if ( maxRdc < allPct ) :
  rankArr_ATA[upBdr] = maxAreaPct[upBdr]
#print '<li>', upBdr, rankArr_ATA, maxAreaPct

#---run second rankArr, if required
if ( maxRdc < allPct and (upBdr+1) < len(rankArr) ) :
  rankArr_ATA[upBdr] = maxAreaPct[upBdr]					# previous bmp, max ATA
  upBdr += 1
  for i in range(upBdr, upBdr+1) :
    myRdc = [0.0] * 20
    maxRdc = 0.0
    for j in range(10,maxAreaPct[upBdr]+5,5) :
      myBMPset = updateBMPset(myBMPset,rankArr[i],urbnConcStr,urbnDist,j)
      writeBMPs(myBMPset,path)
      os.chdir(path)
      os.system('./stepl_amc')
      os.chdir('../../../')
      myRdc[j/5-2] = readRst(path,sltWQname)
      if ( maxRdc < myRdc[j/5-2] ) :
        maxRdc = myRdc[j/5-2]
#      print '<li>', rankArr[upBdr][0], '::', j,  myRdc[j/5-2]
    for j in range(1,len(myRdc)) :
      if ( myRdc[j-1] < allPct and allPct <= myRdc[j] ) :  
        rankArr_ATA[upBdr] = ( j + 2 ) * 5
  if ( maxRdc < allPct ) :
    rankArr_ATA[upBdr] = maxAreaPct[upBdr]
#print '<li>', upBdr, rankArr_ATA, maxAreaPct

#---run third rankArr, if required
if ( maxRdc < allPct and (upBdr+1) < len(rankArr) ) :
  rankArr_ATA[upBdr] = maxAreaPct[upBdr]                                        # previous bmp, max ATA
  upBdr += 1
  for i in range(upBdr, upBdr+1) :
    myRdc = [0.0] * 20
    maxRdc = 0.0
    for j in range(10,maxAreaPct[upBdr]+5,5) :
      myBMPset = updateBMPset(myBMPset,rankArr[i],urbnConcStr,urbnDist,j)
      writeBMPs(myBMPset,path)
      os.chdir(path)
      os.system('./stepl_amc')
      os.chdir('../../../')
      myRdc[j/5-2] = readRst(path,sltWQname)
      if ( maxRdc < myRdc[j/5-2] ) :
        maxRdc = myRdc[j/5-2]
      #print '<li>', rankArr[upBdr][0], '::', j,  myRdc[j/5-2]
    for j in range(1,len(myRdc)) :
      if ( myRdc[j-1] < allPct and allPct <= myRdc[j] ) :   
        rankArr_ATA[upBdr] = ( j + 2 ) * 5
  if ( maxRdc < allPct ) :
    rankArr_ATA[upBdr] = maxAreaPct[upBdr]

#---run fourth rankArr, if required
if ( maxRdc < allPct and (upBdr+1) < len(rankArr) ) :
  rankArr_ATA[upBdr] = maxAreaPct[upBdr]                                        # previous bmp, max ATA
  upBdr += 1
  for i in range(upBdr, upBdr+1) :
    myRdc = [0.0] * 20
    maxRdc = 0.0
    for j in range(10,maxAreaPct[upBdr]+5,5) :
      myBMPset = updateBMPset(myBMPset,rankArr[i],urbnConcStr,urbnDist,j)
      writeBMPs(myBMPset,path)
      os.chdir(path)
      os.system('./stepl_amc')
      os.chdir('../../../')
      myRdc[j/5-2] = readRst(path,sltWQname)
      if ( maxRdc < myRdc[j/5-2] ) :
        maxRdc = myRdc[j/5-2]
      #print '<li>', rankArr[upBdr][0], '::', j,  myRdc[j/5-2]
    for j in range(1,len(myRdc)) :
      if ( myRdc[j-1] < allPct and allPct <= myRdc[j] ) :   
        rankArr_ATA[upBdr] = ( j + 2 ) * 5
  if ( maxRdc < allPct ) :
    rankArr_ATA[upBdr] = maxAreaPct[upBdr]

#rankArr_ATA[0] = 65
#rankArr_ATA[1] = 50 
#upBdr = 1

#for i in range(upBdr+1) :
#  print '<li>', rankArr_ATA[i], '::::', rankArr[i]

#---E loop------------------------------------------------------------------------------------------------------
#--------------------S calculate cost---------------------------------------------------------------------------
areaWSD = areaWSD.split('\t')
rankArr_COST = [0.0] * len(rankArr)
sum_COST = 0.0

luseClm = 0
locale.setlocale(locale.LC_ALL, 'en_US')
for i in range(upBdr+1) :
  if ( rankArr[i][0] == 'Urban' ) :
    luseClm = 0 
  elif ( rankArr[i][0] == 'Cropland' ) :
    luseClm = 1
  elif ( rankArr[i][0] == 'Forest' ) :
    luseClm = 3
  elif ( rankArr[i][0] == 'Feedlots' ) :
    luseClm = 5
  else :
    print '<li> ERROR !! No Landuse Name'

  rankArr_COST[i] = float(areaWSD[luseClm]) * float(rankArr[i][7]) * float(rankArr_ATA[i]) / 100.0
  sum_COST += rankArr_COST[i]

#--------------------E calculate cost---------------------------------------------------------------------------
#---------------------------------------S bmp set opener--------------------------------------------------------
bmpUpdate = [0] * 5
for i in range(len(bmpUpdate)) :
  bmpUpdate[i] = [0] * 6

urbnConc = [0.0,0.0,0.0,0.0]
urbnATA = 0.0

for i in range(upBdr+1) :
  bmpClm = 9
  if ( rankArr[i][0] == 'Cropland' ) :
    bmpClm = 0
  elif ( rankArr[i][0] == 'Forest' ) :
    bmpClm = 1
  elif ( rankArr[i][0] == 'Feedlots' ) :
    bmpClm = 2
  elif ( rankArr[i][0] == 'Urban' ) :
    urbnATA = rankArr_ATA[i]
    urbnConc[0] = rankArr[i][3]
    urbnConc[1] = rankArr[i][4]
    urbnConc[2] = rankArr[i][5]
    urbnConc[3] = rankArr[i][6]
  if ( bmpClm < 9 ) :
    bmpUpdate[bmpClm][0] = float(rankArr[i][3]) * float(rankArr_ATA[i]) / 100.0
    bmpUpdate[bmpClm][1] = float(rankArr[i][4]) * float(rankArr_ATA[i]) / 100.0
    bmpUpdate[bmpClm][2] = float(rankArr[i][5]) * float(rankArr_ATA[i]) / 100.0
    bmpUpdate[bmpClm][3] = float(rankArr[i][6]) * float(rankArr_ATA[i]) / 100.0
    for j in range(4) :
      bmpUpdate[bmpClm][j] = '%.4f'%bmpUpdate[bmpClm][j]
    bmpUpdate[bmpClm][5] = rankArr_ATA[i]

jsStr = []
for i in range(5) :
  for j in range(6) :
    tmpStr = 'opener.document.bmpMain.BMP_' + str(i+1) + '_01' + str(j+1) + '.value = "' + str(bmpUpdate[i][j]) + '" ;'
    if ( j == 4 and 0.0 < float(bmpUpdate[i][j+1]) ) :
      tmpStr = ''
    jsStr.append(tmpStr)
#for i in range(len(jsStr)) :
#  print '<li>', jsStr[i]
#for i in range(5) :
#  print '<li>', bmpUpdate[i][5]

#---urban
urbnUpdate = [0] * 5
for i in range(len(urbnUpdate)) :
  urbnUpdate[i] = [0.0] * 9

if ( 0.0 < urbnATA ) :
  upDist = [0.0] * len(urbnDist)
  for i in range(1,len(urbnDist)-1) :
    upDist[i] = float(urbnDist[0]) * float(urbnDist[i]) * float(urbnATA) / 100.0 / 100.0
    upDist[i] = '%.2f'%upDist[i]
  upDist.pop(0)
  upDist.pop(-1)

  #print '<li>', upDist

  for i in range(len(urbnUpdate[0])) :							# urbn area for BMP ("Effective BMP application area (ac)")
    urbnUpdate[0][i] = upDist[i]

  for i in range(1,len(urbnUpdate)) :
    for j in range(len(urbnUpdate[i])) :
      urbnUpdate[i][j] = '%.4f'%float(urbnConc[i-1])

#  for i in range(len(urbnUpdate)) :
#    print '<li>', urbnUpdate[i]

jsStr2 = [] 
for i in range(len(urbnUpdate)) :
  for j in range(len(urbnUpdate[i])) :
    tmpStr2 = 'opener.document.bmpMain.UrbanBMP_' + str(i+1) + '_01' + str(j+1) + '.value = "' + str(urbnUpdate[i][j]) + '" ; '
    jsStr2.append(tmpStr2)

#---------------------------------------E bmp set opener--------------------------------------------------------
#-------------S HTML--------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL BMP Optimization Module</title>'

print '<script language="JavaScript">'
print 'function UpdateVal() {'
for i in range(len(jsStr)) :
  print jsStr[i]

for i in range(len(jsStr2)) :
  print jsStr2[i]
print '}'
print '</script>'

print '</head>'
print '<body>'
print '<center><br><img src="./img/STEPL_WEB_title.jpg" width=400><hr><br>'
print '<form name=main>'
print '  <table border=1 width=800>'
print '    <tr>'
print '      <td align=center><font face="Times New Roman"><b>Landuse</b></font></td>'
print '      <td align=center><font face="Times New Roman"><b>BMP</b></font></td>'
print '      <td align=center><font face="Times New Roman"><b>Area to Apply (%)</b></font></td>'
print '      <td align=center><font face="Times New Roman"><b>Annual Cost ($)</b></font></td>'
print '    </tr>'
for i in range(upBdr+1) :
  print '    <tr>'
  print '      <td align=left><font face="Times New Roman">', rankArr[i][0], '</td>'
  print '      <td align=left><font face="Times New Roman">', rankArr[i][1], '</td>'
  print '      <td align=right><font face="Times New Roman">', rankArr_ATA[i], '</td>'
  print '      <td align=right><font face="Times New Roman">', locale.format('%d', int(rankArr_COST[i]+0.5), 1), '</td>'
  print '    </tr>'

print '    <tr><td colspan=4><hr></td></tr>'
print '    <tr>'
print '      <td align=right colspan=4><font face="Times New Roman">'
print '        <b>Total Annual Cost ($/year): <font color=tomato>', locale.format('%d', int(sum_COST+0.5), 1), '</b></font></font>'
print '      </td>'
print '    </tr>'
print '  </table>'
print '  <hr>'
print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Update" onClick="javascript:UpdateVal()">'




print '</form>'
print '</body>'
print '</html>'
#-------------E HTML--------------------------------------------------------------------------------------------































chmod777dir = 'chmod 777 ' + path 
chmod777file1 = 'chmod 777 ' + path + '*'
chmod777file2 = 'chmod 777 ' + path + '*.*'
os.system(chmod777dir)
os.system(chmod777file1)
os.system(chmod777file2)
