#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob, math, locale
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()


#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
bmpdata1 = str(form.getvalue('bmpdata4'))
dftLoad = str(form.getvalue('dftLoadStr'))
numBMP = int(form.getvalue('numBMP'))
sltWQname = str(form.getvalue('sltWQname'))
curLoad = str(form.getvalue('curLoad'))
tgtLoad = str(form.getvalue('tgtLoad'))
rqdLoad = str(form.getvalue('rqdLoad'))

mpaArr1 = []
for i in range(numBMP) :
  tmpStr1 = str(form.getvalue('mpa_' + str(i)))
  if ( tmpStr1 == 'None' or tmpStr1 == 'none' or tmpStr1 == '' ) :
    tmpStr1 = '0'
  tmpStr1.replace(',','')
  mpaArr1.append(float(tmpStr1))

bmpdata1 = bmpdata1.split('____')
bmpdata1.pop(-1)
#for i in range(len(bmpdata1)) :
#  bmpdata1[i] = bmpdata1[i].split('__')

curLoad = float(curLoad.replace(',',''))
tgtLoad = float(tgtLoad.replace(',',''))
rqdLoad = float(rqdLoad.replace(',',''))
dftLoad = dftLoad.split('____')
for i in range(len(dftLoad)) :
  dftLoad[i] = float(dftLoad[i])
  

#print '<li>', dftLoad, numBMP, sltWQname
#print '<li>', curLoad, tgtLoad, rqdLoad
#print '<li>', len(mpaArr1), len(bmpdata1)

#----E input----------------------------------------------------------------------------------------------------
#--------------------S declare array----------------------------------------------------------------------------
#---bmpdata2 = mpaArr1 + bmpdata1
bmpdata2 = []
for i in range(len(bmpdata1)) :
  #print '<li>', mpaArr1[i], bmpdata1[i]
  if ( 0.0 < mpaArr1[i] ) :
    tmpStr2 = str(mpaArr1[i]) + '__' + bmpdata1[i]
    bmpdata2.append(tmpStr2)

#print '<hr>'
for i in range(len(bmpdata2)) :
  #print '<li>', bmpdata2[i]
  # (mpa) - (mass rdc/ac) - (max mass rdc) - (unit cost) - (luse area) - (luse) - (bmp) - (mass rdc/ac : n, p, b, s)
  #   0		1		2		3		4	   5	    6		7, 8, 9 , 10
  bmpdata2[i] = bmpdata2[i].split('__')
  for j in range(len(bmpdata2[i])) :
    if ( j != 5 and j != 6 ) :
      bmpdata2[i][j] = float(bmpdata2[i][j])
    else :
      bmpdata2[i][j] = str(bmpdata2[i][j])
  #print '<li>', bmpdata2[i]

#--------------------E declare array----------------------------------------------------------------------------
#------------------------------------------S def looping--------------------------------------------------------
def myLoop(myArr,rqdLoadCur) :
  intv = int(myArr[0]/100) 
  optArea = -1
  rdcVal1 = myArr[1]
#  print '<li>', rdcVal1
  for i in range(1,100) :
    rdcVal2 = intv * (i+1) * myArr[1]
    if ( rdcVal1 < rqdLoadCur and rqdLoadCur <= rdcVal2 ) :
      optArea = intv * (i+1)
    rdcVal1 = rdcVal2
#    print '<li>', (intv * (i+1)), rdcVal1, optArea
#  print '<hr>'

  if ( optArea < 0.0 ) :					# if not meet, try max area
    rdcVal1 = myArr[0] * myArr[1]
    optArea = myArr[0] 

  rqdLoadCur = rqdLoadCur - rdcVal1

  return optArea, rqdLoadCur
#------------------------------------------E def looping--------------------------------------------------------
#---S loop------------------------------------------------------------------------------------------------------
ataArr1 = [0.0] * len(bmpdata2)					# area to apply array
rqdLoadCur = rqdLoad
#print '<li>', bmpdata2[0]

for i in range(len(bmpdata2)) :
  if ( 0.0 < rqdLoadCur ) :
    ataArr1[i], rqdLoadCur = myLoop(bmpdata2[i],rqdLoadCur)
    #print '<li>aa', ataArr1[i], rqdLoadCur

#print '<hr>'
#for i in range(len(ataArr1)) :
#  if ( 0.0 < ataArr1[i] ) :
#    print '<li>', ataArr1[i], bmpdata2[i]
#---E loop------------------------------------------------------------------------------------------------------
#--------------S compute loads with BMPs------------------------------------------------------------------------
# (mpa) - (mass rdc/ac) - (max mass rdc) - (unit cost) - (luse area) - (luse) - (bmp) - (mass rdc/ac : n, p, b, s)
#   0         1               2               3               4          5        6           7, 8, 9 , 10
rdcLoad1 = [0.0] * len(ataArr1)						# mass reductions by each BMP
rdcLoad2 = [0.0, 0.0, 0.0, 0.0]						# mass reductions by BMPs
for i in range(len(ataArr1)) :
  if ( 0.0 < ataArr1[i] ) :
    rdcLoad1[i] = [0.0, 0.0, 0.0, 0.0]
    rdcLoad1[i][0] = ataArr1[i] * bmpdata2[i][7]
    rdcLoad1[i][1] = ataArr1[i] * bmpdata2[i][8]
    rdcLoad1[i][2] = ataArr1[i] * bmpdata2[i][9]
    rdcLoad1[i][3] = ataArr1[i] * bmpdata2[i][10]
    rdcLoad2[0] += rdcLoad1[i][0]
    rdcLoad2[1] += rdcLoad1[i][1]
    rdcLoad2[2] += rdcLoad1[i][2]
    rdcLoad2[3] += rdcLoad1[i][3]
    
  

#print '<li> tgtLoad: ', tgtLoad
#print '<li> curLoad: ', curLoad
#print '<li> rqdLoad: ', rqdLoad
#print '<li> dftLoad: ', dftLoad
#print '<li> rdcLoad2: ', rdcLoad2

#for i in range(len(ataArr1)) :
#  if ( 0.0 < ataArr1[i] ) :
#    print '<li>', rdcLoad1[i]
#--------------E compute loads with BMPs------------------------------------------------------------------------
#---------------------------------------------S general output--------------------------------------------------
outArr1 = [0.0] * 12
# 0,1,2,3 : w/o BMP
# 4,5,6,7 : w/  BMP
# 8,9,10,11 : %

for i in range(4) :
  outArr1[i] = dftLoad[i]
for i in range(4,8) :
  outArr1[i] = dftLoad[i-4] - rdcLoad2[i-4]
for i in range(8,12) :
  outArr1[i] = rdcLoad2[i-8] / dftLoad[i-8] * 100

#print '<li>', outArr1
#---------------------------------------------E general output--------------------------------------------------
#---S check if meet goal----------------------------------------------------------------------------------------
FinSimLoad = 0.0
if ( sltWQname[0] == 'N' ) :
  FinSimLoad = float(outArr1[4])
elif ( sltWQname[0] == 'P' ) :
  FinSimLoad = float(outArr1[5])
elif ( sltWQname[0] == 'B' ) :
  FinSimLoad = float(outArr1[6])
elif ( sltWQname[0] == 'S' ) :
  FinSimLoad = float(outArr1[7])

chkMeetGoal = ''
if ( float(tgtLoad) < FinSimLoad ) :
  chkMeetGoal = '<font face="Times New Roman" size=7 color=red>Increase BMP area !!</font><br>'

#---E check if meet goal----------------------------------------------------------------------------------------
#-----------------------------------------------------------------S for HTML------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US')

outArrStr = ['ys'] * len(outArr1)
outArrStr[0] = outArr1[0]
outArrStr[1] = outArr1[4]
outArrStr[2] = outArr1[8]
outArrStr[3] = outArr1[1]
outArrStr[4] = outArr1[5]
outArrStr[5] = outArr1[9]
outArrStr[6] = outArr1[2]
outArrStr[7] = outArr1[6]
outArrStr[8] = outArr1[10]
outArrStr[9] = outArr1[3]
outArrStr[10] = outArr1[7]
outArrStr[11] = outArr1[11]

for i in range(len(outArr1)) :
  if ( i < 8 ) : 
    outArrStr[i] = locale.format('%d',int(outArrStr[i]+0.5),1) 
  else :
    outArrStr[i] = locale.format('%.1f',outArrStr[i],1)


empTxt = [' '] * len(outArrStr)
if ( sltWQname[0] == 'N' ) :
  empTxt[0] = '<font color=red><b> '
  empTxt[1] = '<font color=red><b> '
  empTxt[2] = '<font color=red><b> '
elif ( sltWQname[0] == 'P' ) :
  empTxt[3] = '<font color=red><b> '
  empTxt[4] = '<font color=red><b> '
  empTxt[5] = '<font color=red><b> '
elif ( sltWQname[0] == 'B' ) :
  empTxt[6] = '<font color=red><b> '
  empTxt[7] = '<font color=red><b> '
  empTxt[8] = '<font color=red><b> '
elif ( sltWQname[0] == 'S' ) :
  empTxt[9] = '<font color=red><b> '
  empTxt[10] = '<font color=red><b> '
  empTxt[11] = '<font color=red><b> '


if ( sltWQname[0] == 'N' ) :
  LoadUnit = ' lbs/year'
elif ( sltWQname[0] == 'P' ) :
  LoadUnit = ' lbs/year'
elif ( sltWQname[0] == 'B' ) :
  LoadUnit = ' lbs/year'
elif ( sltWQname[0] == 'S' ) :
  LoadUnit = ' tons/year'
else :
  print '<li> ERROR 02'


tgtLoad = str(locale.format('%d',int(tgtLoad+0.5),1))
curLoad = str(locale.format('%d',int(curLoad+0.5),1))
rqdLoad = str(locale.format('%d',int(rqdLoad+0.5),1))


optDscArr = []
for i in range(len(ataArr1)) :
  if ( 0.0 < ataArr1[i] ) :
    optStr1 = bmpdata2[i][5]
    optStr2 = bmpdata2[i][6]
    optVal1 = float(ataArr1[i])
    optVal2 = float(bmpdata2[i][4])
    optVal3 = '%.1f'%(optVal1 / optVal2 * 100.0) 					# applied percentage 
    optVal4 = optVal1 * bmpdata2[i][3]							# cost
    optVal5 = bmpdata2[i][1] * ataArr1[i]
    optDscArr.append(optStr1 + '__' + optStr2 + '__' + str('%.1f'%optVal1) + '__' + str(optVal3) + '__' + str(optVal4) + '__' + str(optVal5)) 

totCost = 0.0

for i in range(len(optDscArr)) :
  optDscArr[i] = optDscArr[i].split('__')
  totCost += float(optDscArr[i][4])
  optDscArr[i][2] = str(locale.format('%d',int(float(optDscArr[i][2])+0.5),1))
  optDscArr[i][3] = str(locale.format('%.1f',int(float(optDscArr[i][3])+0.5),1))
  optDscArr[i][4] = str(locale.format('%d',int(float(optDscArr[i][4])+0.5),1))
  optDscArr[i][5] = str(locale.format('%d',int(float(optDscArr[i][5])+0.5),1))
  #optDscArr[i][5] = str(optDscArr[i][5])
#  print '<li>', optDscArr[i]
totCost = str(locale.format('%d',int(totCost+0.5),1))

# (mpa) - (mass rdc/ac) - (max mass rdc) - (unit cost) - (luse area) - (luse) - (bmp) - (mass rdc/ac : n, p, b, s)
#   0         1               2               3               4          5        6           7, 8, 9 , 10

#-----------------------------------------------------------------E for HTML------------------------------------
#------------S graphs-------------------------------------------------------------------------------------------
pathSim = './tmp/' + ystime + '/mlt/'

#----dat files
def datFile(pathSim,GnuArr,myName) :
  if ( myName == 'B' ) :
    headerName = 'BOD'
  else :
    headerName = myName
 
  myDat = open(pathSim + myName + 'gnu.dat','w')
  myDat.write('Watershed\t' + headerName + '_Load_(no_BMP)\t' + headerName + '_Load_(with_BMP)\n')
  myDat.write(GnuArr + '\n')
  myDat.close()

Narr = 'Total\\n(' + str('%.1f'%float(outArr1[8])) + ')' + '\t' + str('%.2f'%float(outArr1[0])) + '\t' + str('%.2f'%float(outArr1[4]))
Parr = 'Total\\n(' + str('%.1f'%float(outArr1[9])) + ')' + '\t' + str('%.2f'%float(outArr1[1])) + '\t' + str('%.2f'%float(outArr1[5]))
Barr = 'Total\\n(' + str('%.1f'%float(outArr1[10])) + ')' + '\t' + str('%.2f'%float(outArr1[2])) + '\t' + str('%.2f'%float(outArr1[6]))
Sarr = 'Total\\n(' + str('%.1f'%float(outArr1[11])) + ')' + '\t' + str('%.2f'%float(outArr1[3])) + '\t' + str('%.2f'%float(outArr1[7]))

datFile(pathSim,Narr,'N')
datFile(pathSim,Parr,'P')
datFile(pathSim,Barr,'B')
datFile(pathSim,Sarr,'S')


#----script files
def sctFile(pathSim,myName) :
  #----define min & max
  maxVal = 0.0
  myDatFile = open(pathSim + myName + 'gnu.dat','r')
  myDat = myDatFile.readlines()
  myDatFile.close()
  for i in range(1,len(myDat)) :                                # first line is header
    if ( 2 < len(myDat[i]) ) :
      tmpDat = myDat[i].replace('\r','')
      tmpDat = tmpDat.replace('\n','')
      tmpDat = tmpDat.split('\t')
      tmpDat[1] = float(tmpDat[1])
      tmpDat[2] = float(tmpDat[2])
      if ( maxVal <= tmpDat[1] ) :
        maxVal = tmpDat[1]
      if ( maxVal <= tmpDat[2] ) :
        maxVal = tmpDat[2]
  maxVal = maxVal * 1.2
  maxVal = '%.2f'%maxVal
  sctArr = [''] * 40
  sctArr[1] = 'set key top left\n'
  sctArr[2] = 'set terminal jpeg font "Helvetica,10"\n'
  sctArr[4] = 'set xtics border in scale 1,0.5 nomirror rotate by 0  offset character 0, 0.5, -2\n'
  sctArr[6] = 'set yrange[0.00:' + str(maxVal) + ']\n'
  #sctArr[6] = 'set autoscale y\n'
  sctArr[8] = 'set autoscale y2\n'
  sctArr[10] = 'set output "' + pathSim + myName + '_bar.jpg"\n'
  sctArr[12] = 'set xlabel "Watershed (Reduction, %)"\n'
  if ( myName == 'S' ) :
    sctArr[14] = 'set ylabel "Annual Loads (tons)"\n'
  else :
    sctArr[14] = 'set ylabel "Annual Loads (lbs)"\n'
  #sctArr[16] = 'set y2label "Total Annual Loads (lbs)"\n'
  sctArr[18] = 'set style data histogram\n'
  sctArr[20] = 'set style histogram cluster gap 1\n'
  sctArr[22] = 'set style fill solid border -1\n'
  sctArr[24] = 'set boxwidth 0.9\n'
  sctArr[26] = 'plot "' + pathSim + myName + 'gnu.dat' + '" using 2:xtic(1) ti col lt 1, "" u 3 ti col lt 2 \n'

  mySct = open(pathSim + myName + 'gnu.script','w')
  for i in range(len(sctArr)) :
    if ( 2 < len(sctArr[i]) ) :
      mySct.write(sctArr[i])
  mySct.close()
  gnuplotExe = 'gnuplot ' + pathSim + myName + 'gnu.script'
  os.system(gnuplotExe)

sctFile(pathSim,'N')
sctFile(pathSim,'P')
sctFile(pathSim,'B')
sctFile(pathSim,'S')


#------------E graphs-------------------------------------------------------------------------------------------
#---S HTML------------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>Web-based STEPL</title>'
print '</head>'
print '<body>'
print '<br><center><img src="./img/STEPL_WEB_title.jpg" width=400><br></center>'
print '<form name=main>'
print '  <br><br><center>'

if ( 1 < len(chkMeetGoal) ) :
  print chkMeetGoal

print '  <table border=0 width=1080>'
print '  <tr>'
print '    <td align=left><font face="Times New Roman">Current Annual ' + sltWQname + ' Load: </td>'
print '    <td align=left><font face="Times New Roman">' + curLoad + LoadUnit + '</td>'
print '    <td width=600> </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left><font face="Times New Roman">Target Annual ' + sltWQname + ' Load: </td>'
print '    <td align=left><font face="Times New Roman">' + tgtLoad + LoadUnit + '</td>'
print '    <td> </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left><font face="Times New Roman">Required Annual ' + sltWQname + ' Reduction: </td>'
print '    <td align=left><font face="Times New Roman">' + rqdLoad + LoadUnit + '</td>'
print '    <td> </td>'
print '  </tr>'
print '</table><br><br>'

print '  <table border=1 width=1080>'
print '    <tr>'
print '      <td align=center colspan=6><font face="Times New Roman" color=tomato>'
print '        <b>Optimized BMP Summary</b>'
print '      </td>'
print '    </tr>'
print '    <tr bgcolor=#BDBDBD>'
print '      <td align=center><font face="Times New Roman">Landuse</td>'
print '      <td align=center><font face="Times New Roman">BMP</td>'
print '      <td align=center><font face="Times New Roman">Applied Area (ac)</td>'
print '      <td align=center><font face="Times New Roman">Applied Area (%)</td>'
print '      <td align=center><font face="Times New Roman">Reduction (' + LoadUnit + ')</td>'
print '      <td align=center><font face="Times New Roman">Cost ($)</td>'
print '    </tr>'
for i in range(len(optDscArr)) :
  print '    <tr>'
  print '      <td align=left><font face="Times New Roman">' + optDscArr[i][0] + '</td>'
  print '      <td align=left><font face="Times New Roman">' + optDscArr[i][1] + '</td>'
  print '      <td align=right><font face="Times New Roman">' + optDscArr[i][2] + '</td>'
  print '      <td align=right><font face="Times New Roman">' + optDscArr[i][3] + '</td>'
  print '      <td align=right><font face="Times New Roman">' + optDscArr[i][5] + '</td>'
  print '      <td align=right><font face="Times New Roman">' + optDscArr[i][4] + '</td>'
  print '    </tr>'

print '    <tr>'
print '      <td colspan=5 align=right><font face="Times New Roman"><b>Total Cost ($/year): </b></td>'
print '      <td align=right><font face="Times New Roman"><b>' + totCost + '</b></td>'
print '    </tr>'
print '  </table><br><br>'

print '  <table border=1 width=1080>'
print '  <tr align=middle>'
print '    <td align=center colspan=12><font face="Times New Roman" color=tomato>'
print '      <b>Annual Loads Summary</b>'
print '    </td>'
print '  </tr>'
###print '  <tr bgcolor=#BDBDBD>'
###print '    <td align=center width=90><font face="Times New Roman">N Load<br>(no BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">P Load<br>(no BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">BOD Load<br>(no BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">Sediment Load<br>(no BMP)<br>tons/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">N Load<br>(with BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">P Load<br>(with BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">BOD Load<br>(with BMP)<br>lbs/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">Sediment Load<br>(with BMP)<br>tons/year</td>'
###print '    <td align=center width=90><font face="Times New Roman">N<br>Reduction<br> %</td>'
###print '    <td align=center width=90><font face="Times New Roman">P<br>Reduction<br> %</td>'
###print '    <td align=center width=90><font face="Times New Roman">BOD<br>Reduction<br>%</td>'
###print '    <td align=center width=90><font face="Times New Roman">Sediment Reduction<br>%</td>'
###print '  </tr>'

print '  <tr>'
print '    <td align=center width=90><b><font face="Times New Roman">N Load<br>(no BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">N Load<br>(with BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">N<br>Reduction<br> %</td>'
print '    <td align=center width=90><b><font face="Times New Roman">P Load<br>(no BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">P Load<br>(with BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">P<br>Reduction<br> %</td>'
print '    <td align=center width=90><b><font face="Times New Roman">BOD Load<br>(no BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">BOD Load<br>(with BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">BOD<br>Reduction<br> %</td>'
print '    <td align=center width=90><b><font face="Times New Roman">S Load<br>(no BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">S Load<br>(with BMP)<br>lbs/year</td>'
print '    <td align=center width=90><b><font face="Times New Roman">S<br>Reduction<br> %</td>'
print '  </tr>'

print '  <tr>'
for i in range(len(outArr1)) :
  print '    <td align=right><font face="Times New Roman">' + empTxt[i] + outArrStr[i] + '</td>'
print '  </tr>'
print '</table><br><br>'

Nstr = '<img src="' + pathSim + 'N_bar.jpg" width=400>'
Pstr = '<img src="' + pathSim + 'P_bar.jpg" width=400>'
Bstr = '<img src="' + pathSim + 'B_bar.jpg" width=400>'
Sstr = '<img src="' + pathSim + 'S_bar.jpg" width=400>'

print '<table border=1>'
print '  <tr align=middle>'
print '    <td align=center colspan=2><font face="Times New Roman" color=tomato><b>Graphs</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>', Nstr, '</td>'
print '    <td align=center>', Pstr, '</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>', Bstr, '</td>'
print '    <td align=center>', Sstr, '</td>'
print '  </tr>'
print '</table><br>'

print '</form>'

print '<hr>'
print '<font color=6666CC size=2>'
print '  Developed by the Agricultural and Biological Engineering Department at Purdue University<br>'
print '</font>'
print '<font size=2>'
print '  <font color=gray>'
print '    Copyright &copy; 2015, Purdue University, all rights reserved. <br>'
print '    Purdue University is an equal access/equal opportunity university.<br>'
print '  </font>'
print '  Contact <a href=mailto:engelb@purdue.edu>Dr. Bernie Engel</a>'
print '  or <a href=mailto:theller@purdue.edu>Larry Theller</a> for more details if you need any help with STEPL WEB. '
print '  <br>'
print '  This implementation of the classic EPA model was designed by Dr. <a href=mailto:ysparkwithyou@gmail.com>Youn Shik Park</a>, Assistant Professor, Kongju National University, South-Korea.'
print '  <br>Programmatic support from US EPA, Illinois-Indiana Sea Grant,  and US Army Corp of Engineers.'
print '</font><br><br>'

print '</body>'
print '</html>'
#---E HTML------------------------------------------------------------------------------------------------------




chmod777 = 'chmod 777 ' + pathSim + '*'
os.system(chmod777)
chmod777 = 'chmod 777 ' + pathSim + '*.*'
os.system(chmod777)





















