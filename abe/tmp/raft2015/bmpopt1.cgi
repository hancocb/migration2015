#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob, math
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()


#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
ystimeldc = str(form.getvalue('ystimeldc'))
allPct = str(form.getvalue('allPct'))

#print '<li>', ystime
#print '<li>', ystimeldc
#print '<li>', allPct
#----E input----------------------------------------------------------------------------------------------------
#-------------------S read files from ldc-----------------------------------------------------------------------
if ( ystimeldc[0] == '2' ) :
  ldcPath = '../pldc/tmp/' + ystimeldc + '/'

  sltWQnameFile = open(ldcPath + 'sltWQname.pys','r')
  sltWQnameTmp = sltWQnameFile.readlines()
  sltWQnameFile.close()
  sltWQname = str(sltWQnameTmp[0][0])

  bmpFile = open(ldcPath + 'BMPtable.csv','r')
  bmpHeader = bmpFile.readline()
  bmpSet = bmpFile.readlines()
  bmpFile.close()

#  print '<li>', sltWQname
#  print '<li>', bmpSet
bmpEffClm = 0
if ( sltWQname == 'N' ) :
  bmpEffClm =0 
elif ( sltWQname == 'P' ) :
  bmpEffClm =1 
elif ( sltWQname == 'B' ) :
  bmpEffClm =2 
elif ( sltWQname == 'S' ) :
  bmpEffClm =3 


#--del if exist
delPrvOpt = glob.glob('./tmp/' + ystime + '/*')
PrvOptDir = ''
for i in range(len(delPrvOpt)) :
  if ( delPrvOpt[i][-3:] == 'opt' ) :
    DelStr = 'rm -rf ' + delPrvOpt[i]
#    print '<li>', DelStr
    os.system(DelStr)
    print 'Previous BMP optimization deleted..<br>'
    PrvOptDir = delPrvOpt[i]

mkdirPath = 'mkdir ./tmp/' + ystime + '/opt'
chmodPath = 'chmod 777 ./tmp/' + ystime + '/opt'
cpExePath = 'cp stepl_amc ./tmp/' + ystime + '/opt/.'
cpInpPath = 'cp ./tmp/' + ystime + '/inp/*.* ./tmp/' + ystime + '/opt/.'
cpPcpPath = 'cp ./tmp/' + ystime + '/cligen/pcp.txt ./tmp/' + ystime + '/opt/.'
cpParPath = 'cp ./tmp/' + ystime + '/myOptPar.pys ./tmp/' + ystime + '/opt/.'
cpExePath2 = 'cp stepl_amc ./tmp/' + ystime + '/stepl'

path = './tmp/' + ystime + '/opt/'

os.system(mkdirPath)
os.system(chmodPath)
os.system(cpExePath)
os.system(cpInpPath)
os.system(cpPcpPath)
os.system(cpParPath)
os.system(cpExePath2)
#-------------------E read files from ldc-----------------------------------------------------------------------
#--------------------------------------------------------S make BMP order---------------------------------------
bmpInfoFile = open('../pldc/BMPlistM.txt','r')
bmpInfo = bmpInfoFile.readlines()
bmpInfoFile.close()

for i in range(len(bmpInfo)) :							# BMP eff. database file
  bmpInfo[i] = bmpInfo[i].replace('\r','')
  bmpInfo[i] = bmpInfo[i].replace('\n','')
  bmpInfo[i] = bmpInfo[i].split('\t')

bmpEff = ['N_P_B_S'] * len(bmpSet)
for i in range(len(bmpSet)) :
  bmpSet[i] = bmpSet[i].replace('\r','')
  bmpSet[i] = bmpSet[i].replace('\n','')
  bmpSet[i] = bmpSet[i].split(',')
  for j in range(len(bmpInfo)) :
    if ( str(bmpInfo[j][0]) == str(bmpSet[i][0]) and str(bmpInfo[j][1]) == str(bmpSet[i][1]) ) : 
      bmpEff[i] = str(bmpInfo[j][2]) + '__' + str(bmpInfo[j][3]) + '__' + str(bmpInfo[j][4]) + '__' + str(bmpInfo[j][5])

for i in range(len(bmpSet)) :
  bmpEff[i] = bmpEff[i].split('__')
#  print '<li>', bmpSet[i], ':::::::::::::', bmpEff[i]

#----area info
luseArea = []
mainINPfile = open(path + 'mainINP.txt','r')
tmpStr1 = mainINPfile.readline()
tmpStr1 = tmpStr1.replace('\r','')
tmpStr1 = tmpStr1.replace('\n','')
tmpStr1 = tmpStr1.split('\t')
numWSD = int(tmpStr1[0])
tmpStr2 = mainINPfile.readline() 						# this line is '----------...'
for i in range(numWSD) : 
  tmpStr3 = mainINPfile.readline()
  luseArea.append(tmpStr3)
mainINPfile.close()

totArea = [0.0,0.0,0.0,0.0,0.0,0.0]						# total area of landuses: urbn, crop, past, frst, user, feed
wsdArea = 0.0
for i in range(len(luseArea)) :
  luseArea[i] = luseArea[i].replace('\r','')
  luseArea[i] = luseArea[i].replace('\n','')
  luseArea[i] = luseArea[i].split('\t')
  for j in range(len(totArea)) :
    totArea[j] += float(luseArea[i][j])
wsdArea = math.fsum(totArea)
#print '<li>', totArea
#print '<li>', wsdArea

unitCost = ['0.0__luse__bmp__0.0__0.0__0.0__0.0'] * 6						# unit cost per 1% area to apply, luse, bmp, eff.
for i in range(len(bmpSet)) :
  if ( bmpSet[i][0] == 'Cropland' ) :
    unitCost[1] = str(bmpSet[i][3]) + '__' + str(bmpSet[i][0]) + '__' + str(bmpSet[i][1])
    unitCost[1] += '__' + str(float(bmpEff[i][0]) * 100.0) + '__' + str(float(bmpEff[i][1]) * 100.0)
    unitCost[1] += '__' + str(float(bmpEff[i][2]) * 100.0) + '__' + str(float(bmpEff[i][3]) * 100.0)
  elif ( bmpSet[i][0] == 'Forest' ) :
    unitCost[3] = str(bmpSet[i][3]) + '__' + str(bmpSet[i][0]) + '__' + str(bmpSet[i][1])
    unitCost[3] += '__' + str(float(bmpEff[i][0]) * 100.0) + '__' + str(float(bmpEff[i][1]) * 100.0)
    unitCost[3] += '__' + str(float(bmpEff[i][2]) * 100.0) + '__' + str(float(bmpEff[i][3]) * 100.0)
  elif ( bmpSet[i][0] == 'Feedlots' ) :
    unitCost[5] = str(bmpSet[i][3]) + '__' + str(bmpSet[i][0]) + '__' + str(bmpSet[i][1])
    unitCost[5] += '__' + str(float(bmpEff[i][0]) * 100.0) + '__' + str(float(bmpEff[i][1]) * 100.0)
    unitCost[5] += '__' + str(float(bmpEff[i][2]) * 100.0) + '__' + str(float(bmpEff[i][3]) * 100.0)
  elif ( bmpSet[i][0] == 'Urban' ) :
    unitCost[0] = str(bmpSet[i][3]) + '__' + str(bmpSet[i][0]) + '__' + str(bmpSet[i][1])
    unitCost[0] += '__' + str(float(bmpEff[i][0]) * 100.0) + '__' + str(float(bmpEff[i][1]) * 100.0)
    unitCost[0] += '__' + str(float(bmpEff[i][2]) * 100.0) + '__' + str(float(bmpEff[i][3]) * 100.0)

for i in range(len(unitCost)) :
  unitCost[i] = unitCost[i].split('__')
  #print '<li>', unitCost[i]
  unitCost[i].append(unitCost[i][0])
  #print '<li>', unitCost[i]
  unitCost[i][0] = float(unitCost[i][0])
  unitCost[i][3+bmpEffClm] = float(unitCost[i][3+bmpEffClm])
  if ( 0.0 < unitCost[i][3+bmpEffClm] and 0.0 < totArea[i] ) :
    unitCost[i][0] = unitCost[i][0] / ( unitCost[i][3+bmpEffClm] * 100.0 * totArea[i] / wsdArea )
    #			($/ac)		(BMP eff. for landuse) (frac.>>%)   (luse area)   (watershed area) : $/ac/ (1% reduction at watershed level)
  else :
    unitCost[i][0] = 0.0
#  if ( totArea[i] <= 0.0 or unitCost[i][3+bmpEffClm] <= 0.0 ) :
#    unitCost[i][0] = 0.0
unitCost.sort()

#for i in range(len(unitCost)) :
#  print '<li>aa', unitCost[i]

rankArr1 = []
for i in range(len(unitCost)) :
  if ( 0.0 < unitCost[i][0] ) :
#    print '<li>', unitCost[i]
    rnkStr1 = str(unitCost[i][1]) + '__' + str(unitCost[i][2]) + '__' + str('%.5f'%float(unitCost[i][0])) + '__' + str(unitCost[i][3])
    rnkStr1 += '__' + str(unitCost[i][4]) + '__' + str(unitCost[i][5]) + '__' + str(unitCost[i][6]) + '__' + str(unitCost[i][7])
    rankArr1.append(rnkStr1)

rankArrAll = ''
for i in range(len(rankArr1)) :
  rankArrAll += rankArr1[i] + '____' 
#  print '<li>', rankArr1[i]
#--------------------------------------------------------E make BMP order---------------------------------------
#---S sltWQname-------------------------------------------------------------------------------------------------
if ( sltWQname == 'N' ) :
  sltWQnameStr = 'Nitrogen'
elif ( sltWQname == 'P' ) :
  sltWQnameStr = 'Phosphorus'
elif ( sltWQname == 'B' ) :
  sltWQnameStr = 'BOD'
elif ( sltWQname == 'S' ) :
  sltWQnameStr = 'Sediment'
else :
  sltWQname = 'Unknown. Error will be occured.'
#---E sltWQname-------------------------------------------------------------------------------------------------
#-----------------------------------------------S HTML----------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL BMP Optimization Module</title>'

print '<script language="JavaScript">'
print 'function init() {'
for i in range(1,5) :
  for j in range(1,10) :
    tmpStr = '  document.main.UrbnConc_' + str(i) + str(j) + '.value = opener.document.bmpMain.UrbnConc_' + str(i) + str(j) + '.value ;'
    print tmpStr
print '}'
print '</script>'


print '</head>'
print '<body onLoad="init();">'
print '<center><br><img src="./img/STEPL_WEB_title.jpg" width=400><hr><br>'
print '<form name=main method="POST" action="./bmpopt2.cgi">'
print '  <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
print '  <input type=hidden name=ystime value="' + ystime + '">'
print '  <input type=hidden name=sltWQname value="' + sltWQnameStr + '">'
print '  <input type=hidden name=rankArrAll value="' + rankArrAll + '">'
print '  <input type=hidden name=numWSD value="' + str(numWSD) + '">'

#print '  <table border=0 width=800>'
#print '    <tr>'
#print '      <td align=left><font face="Times New Roman">'
#print '        The table shows BMP list to apply. The module will apply BMPs by the order in the table.<br>'
#print '        Changing the MATA, the module will run STEPL until the estimated pollutant load meets the target load.'
#print '      </td>'
#print '    </tr>'
#print '    <tr><td> </td></tr>'
#print '    <tr>'
#print '      <td align=left><font face="Times New Roman">'
#print '        Water quality parater is <b><font color=tomato>', sltWQnameStr, '</font></b>.<br>'
#myStr1 = '        Required Reduction Percentage is <input type=hidden name=allPct value="'
myStr1 = '<input type=hidden name=allPct value="' + str('%.2f'%float(allPct)) + '" style="text-align:right" size=4>'
print myStr1
#print '      </td>'
#print '    </tr>'
#print '  </table>'


#print '  <table border=1 width=800>'
#print '    <tr>'
#print '      <td align=center><font face="Times New Roman"><b>Landuse</font></td>'
#print '      <td align=center><font face="Times New Roman"><b>BMP</font></td>'
#print '      <td align=center><font face="Times New Roman"><b>BMP Efficiency (%)</td>'
#print '      <td align=center><font face="Times New Roman"><b>Cost<sup><font color=red>1</font></sup></td>'
#print '      <td align=center><font face="Times New Roman"><b>MATA<sup><font color=red>2</font></sup></td>'
#print '    </tr>'
#for i in range(len(rankArr1)) :
#  tblStr1 = rankArr1[i].split('__') 
#  tblStr2 = '    <tr>\n'
#  tblStr2 += '      <td align=left><font face="Times New Roman">' + tblStr1[0] + '</font></td>\n'
#  tblStr2 += '      <td align=left><font face="Times New Roman">' + tblStr1[1] + '</font></td>\n'
#  tblStr2 += '      <td align=right><font face="Times New Roman">' + str('%.2f'%float(tblStr1[3+bmpEffClm])) + '</font></td>\n'
#  tblStr2 += '      <td align=right><font face="Times New Roman">' + str('%.5f'%float(tblStr1[2])) + '</font></td>\n'
#  tblStr2 += '      <td align=center><input type=text name=maxAreaPct_' + str(i) + ' size=4 style="text-align:right" value=100></td>\n'
#  tblStr2 += '    </tr>\n'
#  print tblStr2
#print '  </table>'
#print '  <table width=800 border=0>'
#print '    <tr>'
#print '      <td width=300> </td>'
#print '      <td align=left><font face="Times New Roman">'
#print '        <b><sup><font color=red>1</font></sup></b>Cost: $ per area to apply per 1% of pollutant reduction at watershed level<br>'
#print '        <b><sup><font color=red>2</font></sup></b>MATA: Max. Area to Apply (%), setting required'
#print '      </td>'
#print '    </tr>'
#print '  </table><br><hr>'

#print '<input type=submit style=\'width:200;height:30;cursor:hand\' value=\'Proceed Optimization\'><br>'

print '<font face="Times New Roman">Making List..</font>'

for i in range(1,5) :
  for j in range(1,10) :
    UrbnConcStr = '<input type=hidden name="UrbnConc_' + str(i) + str(j) + '" size=3>'
    print UrbnConcStr
#  print '<br>'

print '</form>'

print '<script language="JavaScript">'
print '  function moveNext() {'
print '    document.main.submit() ;'
print '  }'
print '  setTimeout(\'moveNext()\',1000);'
print '</script>'

print '</body>'
print '</html>'
#-----------------------------------------------E HTML----------------------------------------------------------



















