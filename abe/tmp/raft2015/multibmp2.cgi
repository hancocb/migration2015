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
intRate = float(form.getvalue('interest')) / 100.0
sltWQname = str(form.getvalue('LoadType'))
allPct = float(form.getvalue('allPct'))

if ( sltWQname == 'N' ) :
  wqClm = 2
elif ( sltWQname == 'P' ) :
  wqClm = 3
elif ( sltWQname == 'B' ) :
  wqClm = 4
elif ( sltWQname == 'S' ) :
  wqClm = 5
#print '<li>', ystime, intRate, sltWQname, wqClm, '<hr>'

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


bmpdata1 = [' '] * 55
for i in range(len(bmpdata1)) :
  bmpdata1[i] = [' '] * 10
  for j in range(len(bmpdata1[i])) :
    bmpdata1[i][j] = str(form.getvalue('bmpdata_' + str(i) + '_' + str(j)))
    if ( 2 <= j ) :
      bmpdata1[i][j] = bmpdata1[i][j].replace(' ','')
    if ( bmpdata1[i][j] == 'None' or bmpdata1[i][j] == 'none' or bmpdata1[i][j] == '' ) :
      bmpdata1[i][j] = 'noVal'
bmpdata1.pop(0)

#for i in range(len(bmpdata1)) :
#  print '<li>', bmpdata1[i]
#print '<hr>'


delPrvOpt = glob.glob('./tmp/' + ystime + '/*')
PrvOptDir = ''
for i in range(len(delPrvOpt)) :
  if ( delPrvOpt[i][-3:] == 'mlt' ) :
    DelStr = 'rm -rf ' + delPrvOpt[i]
    #print '<li>', DelStr
    os.system(DelStr)
    print 'Previous BMP optimization deleted..<br>'
    PrvOptDir = delPrvOpt[i]

mkdirPath = 'mkdir ./tmp/' + ystime + '/mlt'
chmodPath = 'chmod 777 ./tmp/' + ystime + '/mlt'
cpExePath = 'cp stepl_amc ./tmp/' + ystime + '/mlt/.'
cpInpPath = 'cp ./tmp/' + ystime + '/inp/*.* ./tmp/' + ystime + '/mlt/.'
cpPcpPath = 'cp ./tmp/' + ystime + '/cligen/pcp.txt ./tmp/' + ystime + '/mlt/.'
cpParPath = 'cp ./tmp/' + ystime + '/myOptPar.pys ./tmp/' + ystime + '/mlt/.'
cpExePath2 = 'cp stepl_amc ./tmp/' + ystime + '/stepl'

path = './tmp/' + ystime + '/mlt/'

os.system(mkdirPath)
os.system(chmodPath)
os.system(cpExePath)
os.system(cpInpPath)
os.system(cpPcpPath)
os.system(cpParPath)
os.system(cpExePath2)

#----E input----------------------------------------------------------------------------------------------------
#-------------------------------------------S def CalCost-------------------------------------------------------
def CalCost(estb,main,life,itrs) :                                                      # establishment, maintenance, design life, interest rate
  estb = float(estb)
  main = float(main) / 100.0                                                            # percentage to ratio
  life = float(life)
  itrs = float(itrs)
  if ( life < 1 ) :
    life = 1
  myVal_1 = 0.0
  myVal_2 = 0.0
  for i in range(1,life+1) :
    myVal_1 += (1+itrs) ** (life-1)
  myVal_2 = estb * ((1+itrs) ** life) + estb * main * myVal_1
  myVal_3 = myVal_2 / life

  return myVal_3

#-------------------------------------------E def CalCost-------------------------------------------------------
#-----------------S declare bmpdata2----------------------------------------------------------------------------
bmpdata2 = []
for i in range(len(bmpdata1)) :
  if ( bmpdata1[i][wqClm] != 'noVal' and bmpdata1[i][7] != 'noVal' and bmpdata1[i][8] != 'noVal' and bmpdata1[i][9] != 'noVal' ) :
    if ( 0.0 < float(bmpdata1[i][wqClm]) ) :
      myCost = 0.0
      myCost = CalCost(bmpdata1[i][7],bmpdata1[i][8],bmpdata1[i][9],intRate)
      myCost = int(myCost + 0.5)
      ##tmpStr1 = bmpdata1[i][0] + '__' + bmpdata1[i][1] + '__' + bmpdata1[i][wqClm] + '__'
      ##tmpStr1 += bmpdata1[i][7] + '__' + bmpdata1[i][8] + '__' + bmpdata1[i][9] + '__' + str(myCost)
      #tmpStr1 = bmpdata1[i][0] + '__' + bmpdata1[i][1] + '__' + bmpdata1[i][wqClm] + '__' + str(myCost)
      tmpStr1 = bmpdata1[i][0] + '__' + bmpdata1[i][1] + '__'
      tmpStr1 += bmpdata1[i][2] + '__' + bmpdata1[i][3] + '__' + bmpdata1[i][4] + '__' + bmpdata1[i][5] + '__'
      tmpStr1 += str(myCost)
      bmpdata2.append(tmpStr1)

for i in range(len(bmpdata2)) :
  bmpdata2[i] = bmpdata2[i].split('__')
  bmpdata2[i][0] = bmpdata2[i][0].replace(' ','')
#  print '<br>a01', bmpdata2[i]
#print '<hr>'

#-----------------E declare bmpdata2----------------------------------------------------------------------------
#---------------------------------------S def. stepl run--------------------------------------------------------
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

areaWSD = tmpArr1[2].split()
#print '<li>a02', areaWSD


#---urban concentration values, fixed
urbnConcArr = [''] * 4
for i in range(1,len(BMPset_2)) :
  urbnConcStr = ''
  for j in range(1,len(BMPset_2[i])-1) :
    urbnConcStr += str(BMPset_2[i][j]) + '\t'
  urbnConcStr += str(BMPset_2[i][-1])
  urbnConcArr[i-1] = urbnConcStr + '\n'

#for i in range(len(urbnConcArr)) :
#  print '<li>', urbnConcArr[i]


#---def urban area
def urbnArea(urbnDist,ATA) :
  urbnStr = ''
  for j in range(1,len(urbnDist)-2) :
    tmpVal1 = float(urbnDist[j]) * float(urbnDist[0]) / 100.0 * ATA / 100.0
    tmpVal1 = '%.4f'%tmpVal1
    urbnStr += str(tmpVal1) + '\t'
  tmpVal1 = float(urbnDist[-2]) * float(urbnDist[0]) / 100.0 * ATA / 100.0
  tmpVal1 = '%.4f'%tmpVal1
  urbnStr += str(tmpVal1)

  return urbnStr


#---default myBMPset
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
noBMPset = [''] * len(myBMPset)
for i in range(len(myBMPset)) :
  noBMPset[i] = myBMPset[i]                                             # no BMP
#  print '<li>', myBMPset[i]


#---update myBMPset
def updateBMPset(myBMPset,rankArr,urbnConcStr,urbnDist,ATA) :
  rankArr[0] = rankArr[0].replace(' ','')
  if ( rankArr[0] == 'Urban' ) :
    urbnStr = urbnArea(urbnDist,ATA)
    myBMPset[20] = urbnStr + '\n'
    nVal = ''
    pVal = ''
    bVal = ''
    sVal = ''
    for i in range(8) :
      nVal += '%.4f'%float(rankArr[2]) + '\t'
      pVal += '%.4f'%float(rankArr[3]) + '\t'
      bVal += '%.4f'%float(rankArr[4]) + '\t'
      sVal += '%.4f'%float(rankArr[5]) + '\t'
    nVal += '%.4f'%float(rankArr[2]) + '\n'
    pVal += '%.4f'%float(rankArr[3]) + '\n'
    bVal += '%.4f'%float(rankArr[4]) + '\n'
    sVal += '%.4f'%float(rankArr[5]) + '\n'

    myBMPset[22] = nVal
    myBMPset[24] = pVal
    myBMPset[26] = bVal
    myBMPset[28] = sVal

  #---update bmp eff. Cropland
  else :
    nVal = float(rankArr[2]) * float(ATA) / 100.0
    pVal = float(rankArr[3]) * float(ATA) / 100.0
    bVal = float(rankArr[4]) * float(ATA) / 100.0
    sVal = float(rankArr[5]) * float(ATA) / 100.0
    nonBMPeffStr = str('%.4f'%nVal) + '\t' + str('%.4f'%pVal) + '\t'
    nonBMPeffStr += str('%.4f'%bVal) + '\t' + str('%.4f'%sVal) + '\t' + str(int(ATA+0.5)) + '\n'

    if ( rankArr[0] == 'Cropland' ) :
      myBMPset[1] = nonBMPeffStr
    if ( rankArr[0] == 'Forest' ) :
      myBMPset[7] = nonBMPeffStr
    elif ( rankArr[0] == 'Feedlots' ) :
      myBMPset[13] = nonBMPeffStr

  return myBMPset


#---write BMPs.txt
def writeBMPs(myBMPset,path) :
  bmp = open(path + 'BMPs.txt','w')
  for i in range(len(myBMPset)) :
#    print '<li>', i, '::', myBMPset[i]
    bmp.write(myBMPset[i])
  bmp.close()


#---read STEPL result
def readRst(path,sltWQname) :
  rstFile = open(path + 'myRST.csv','r')
  rst = rstFile.readlines()
  rstFile.close()

  clm = 12
  if ( sltWQname[0] == 'N' ) :
    clm = 9
  elif ( sltWQname[0] == 'P' ) :
    clm = 10
  elif ( sltWQname[0] == 'B' ) :
    clm = 11

  myRdc1 = rst[-1].split()
  simLoad = float(myRdc1[clm])

  #---read all
  allLoad = [0.0, 0.0, 0.0, 0.0]
  allLoad[0] = float(myRdc1[9])
  allLoad[1] = float(myRdc1[10])
  allLoad[2] = float(myRdc1[11])
  allLoad[3] = float(myRdc1[12])

  #return simLoad
  return simLoad, allLoad
#---------------------------------------E def. stepl run--------------------------------------------------------
#---S run STEPL with no BMP-------------------------------------------------------------------------------------
# run STEPL with no BM
dftLoad = [0.0, 0.0, 0.0, 0.0]
writeBMPs(myBMPset,path)
os.chdir(path)
os.system('./stepl_amc')
os.chdir('../../../')
curLoad, dftLoad = readRst(path,sltWQname) 
#print '<li>a03, Current Load', curLoad
#---E run STEPL with no BMP-------------------------------------------------------------------------------------
#------------------------------S run STEPL with BMPs------------------------------------------------------------
bmpdata3 = [] 					# cost_mass - mass_area - rdcLoad - luseArea1 - luse - bmp 

for i in range(len(bmpdata2)) : 

  #---set no BMPs to apply current BMP
  for j in range(len(noBMPset)) :
    myBMPset[j] = noBMPset[j]

  simLoad = 0.0
  luseArea1 = 0.0

  #---luse area
  if ( bmpdata2[i][0] == 'Urban' ) :
    luseArea1 = float(areaWSD[0])
  elif ( bmpdata2[i][0] == 'Cropland' ) :
    luseArea1 = float(areaWSD[1])
  elif ( bmpdata2[i][0] == 'Pastureland' ) :
    luseArea1 = float(areaWSD[2])
  elif ( bmpdata2[i][0] == 'Forest' ) :
    luseArea1 = float(areaWSD[3])
  elif ( bmpdata2[i][0] == 'Feedlots' ) :
    luseArea1 = float(areaWSD[5])

  if ( 0.0 < luseArea1 ) :
    myBMPset = updateBMPset(myBMPset,bmpdata2[i],urbnConcStr,urbnDist,100)
    #print '<hr><b>a04', bmpdata2[i], '</b>'
    #for j in range(len(myBMPset)) :
    #  print '<li>', myBMPset[j]
    writeBMPs(myBMPset,path)
    os.chdir(path)
    os.system('./stepl_amc')
    os.chdir('../../../')
    allLoad = [0.0, 0.0, 0.0, 0.0]
    simLoad, allLoad = readRst(path,sltWQname)
    simLoad = float(simLoad)
    curLoad = float(curLoad)
    rdcLoad = curLoad - simLoad
    unitCost = float(bmpdata2[i][-1])					# $/ac/yr
    if ( 0.0 < rdcLoad ) :
      cost_mass = (unitCost * luseArea1) / rdcLoad
    else :
      print '<li><b>Error 01'
    mass_area = (curLoad - simLoad) / luseArea1

    #---allLoad, dftLoad
    npsLoad = [0.0, 0.0, 0.0, 0.0]
    for j in range(4) :
      npsLoad[j] = (dftLoad[j] - allLoad[j]) / luseArea1		# mass_area for n, p, b, s

    #print '<li>', simLoad, '--', curLoad, '--', unitCost, '--', luseArea1, '--', bmpdata2[i][wqClm]
    #print '<li>------ ', bmpdata2[i][0], '--', bmpdata2[i][1], '--', int(cost_mass), '--', '%.4f'%mass_area
    tmpStr1 = '%.4f'%cost_mass + '__' + '%.4f'%mass_area + '__' + str(int(rdcLoad+0.5)) + '__' + str(int(unitCost+0.5))
    tmpStr1 += '__' + str(luseArea1) + '__' + str(bmpdata2[i][0]) + '__' + str(bmpdata2[i][1]) 
    tmpStr1 += '__' + str('%.4f'%npsLoad[0]) + '__' + str('%.4f'%npsLoad[1])
    tmpStr1 += '__' + str('%.4f'%npsLoad[2]) + '__' + str('%.4f'%npsLoad[3])
    bmpdata3.append(tmpStr1)


for i in range(len(bmpdata3)) :
  bmpdata3[i] = bmpdata3[i].split('__')
  bmpdata3[i][0] = float(bmpdata3[i][0])
bmpdata3.sort()


#print '<li>CurLoad: ', curLoad
#print '<li>TgtLoad: ', curLoad * (1-allPct/100)
#print '<li>RdcLoad: ', curLoad - (curLoad * (1-allPct/100))
#print '<hr>'


tmpStr2 = ''
bmpdata4 = ''
for i in range(len(bmpdata3)) : 
#  print '<li>', bmpdata3[i]
  tmpStr2 = ''
  for j in range(1,len(bmpdata3[i])-1) :
    tmpStr2 += str(bmpdata3[i][j]) + '__'
  tmpStr2 += str(bmpdata3[i][-1])
  bmpdata4 += tmpStr2 + '____'
#------------------------------E run STEPL with BMPs------------------------------------------------------------
#----------------------------------------------------------S for HTML-------------------------------------------
if ( sltWQname == 'N' ) :
  LoadTypeStr = 'Nitrogen'
  LoadUnit = 'lbs/year'
elif ( sltWQname == 'P' ) :
  LoadTypeStr = 'Phosphorus'
  LoadUnit = 'lbs/year'
elif ( sltWQname == 'B' ) :
  LoadTypeStr = 'BOD'
  LoadUnit = 'lbs/year'
elif ( sltWQname == 'S' ) :
  LoadTypeStr = 'Sediment'
  LoadUnit = 'tons/year'
else :
  print '<li> ERROR 02'


locale.setlocale(locale.LC_ALL, 'en_US')
curLoadStr = locale.format('%d', int(curLoad+0.5), 1)
tgtLoadStr = locale.format('%d', int(curLoad * (1-allPct/100)+0.5), 1)
rdqLoadStr = locale.format('%d', int(curLoad - (curLoad * (1-allPct/100))+0.5), 1)


# n, p, b, S load without bmps
dftLoadStr = str('%.1f'%dftLoad[0]) + '____' + str('%.1f'%dftLoad[1]) + '____' 
dftLoadStr += str('%.1f'%dftLoad[2]) + '____' + str('%.1f'%dftLoad[3])

#----------------------------------------------------------E for HTML-------------------------------------------
#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL WEB</title>'
print '</head>'

print '<body>'
print '<form name=main method="POST" action="./multibmp3.cgi"><center><br>'
print '<font color=tomato face="Times New Roman"><b>Define Maximum Possible Area to Apply BMPs</b></font>'

print '<input type=hidden name=bmpdata4 value="' + str(bmpdata4) + '">'
print '<input type=hidden name=dftLoadStr value="' + str(dftLoadStr) + '">'
print '<input type=hidden name=numBMP value="' + str(len(bmpdata3)) + '">'
print '<input type=hidden name=ystime value="' + str(ystime) + '">'


print '<table border=0 width=700>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">Load Type: '
print '    </td>'
print '    <td align=left>'
htStr1 = '      <input type=text name=sltWQname style="border-width:0px;text-align:right;" value="' + LoadTypeStr + '" readonly size=20> '
print htStr1
print '    </td>'
print '    <td width=200> </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">Current Annual ' + LoadTypeStr + ' Load: '
print '    </td>'
print '    <td align=left>'
htStr2 = '      <input type=text name=curLoad style="border-width:0px;text-align:right;" value="' + curLoadStr + '" readonly size=10> ' + LoadUnit 
print htStr2
print '    </td>'
print '    <td> </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">Target Annual ' + LoadTypeStr + ' Load: '
print '    </td>'
print '    <td align=left>'
htStr3 = '      <input type=text name=tgtLoad style="border-width:0px;text-align:right" value="' + tgtLoadStr + '" readonly size=10> ' + LoadUnit 
print htStr3
print '    </td>'
print '    <td> </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">Required Annual ' + LoadTypeStr + ' Reduction: '
print '    </td>'
print '    <td align=left>'
htStr4 = '      <input type=text name=rqdLoad style="border-width:0px;text-align:right" value="' + rdqLoadStr + '" readonly size=10> ' + LoadUnit 
print htStr4
print '    </td>'
print '    <td> </td>'
print '  </tr>'
print '</table>'

print '<table width=700 border=1>'
print '  <tr>'
print '    <td align=center><font face="Times New Roman">Landuse</td>'
print '    <td align=center width=350><font face="Times New Roman">BMP Name</td>'
print '    <td align=center><font face="Times New Roman">MPA (ac)</td>'
print '    <td align=center><font face="Times New Roman">Landuse (ac)</td>'
print '  </tr>'

for i in range(len(bmpdata3)) :
  print '<tr>'
  print '  <td><font face="Times New Roman">' + bmpdata3[i][5] + '</td>'
  print '  <td><font face="Times New Roman">' + bmpdata3[i][6] + '</td>'
  print '  <td align=center>'
  tbStr1 = '    <input type=text style="text-align:right" size=10 name=mpa_' + str(i) + ' value="0.0">'
  #tbStr1 = '    <input type=text style="text-align:right" size=10 name=mpa_' + str(i) + ' value="' + str(bmpdata3[i][4]) + '">'
  print tbStr1
  print '  </td>'
  print '  <td align=right><font face="Times New Roman">' + str(bmpdata3[i][4]) + '</td>'
  print '</tr>'
print '</table><br>'

print '<input type=submit style="width:150;heigh:30;cursor:hand" value="Optimize">'

print '</form>'

print '<hr>'
print '<font color=6666CC size=2>'
print '  Developed by the Agricultural and Biological Engineering Department at Purdue University<br>'
print '</font>'
print '<font size=2>'
print '  <font color=gray>'
print '	   Copyright &copy; 2014, Purdue University, all rights reserved. <br>'
print '    Purdue University is an equal access/equal opportunity university.<br>'
print '  </font>'
print '  Contact <a href=mailto:engelb@purdue.edu>Dr. Bernie Engel</a>'
print '  for more details if you need any help for STEPL WEB.'
print '  <br>'
print '  Programmed by <a href=mailto:parkyounshik@gmail.com>Youn Shik Park</a>, Purdue University Research Assistant'
print '</font><br><br>'

print '</body>'
print '</html>'
#----E HTML-----------------------------------------------------------------------------------------------------




















