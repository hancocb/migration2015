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

if ( allPct == 'none' or allPct == 'None' ) :
  allPct = 0.0
else :
  allPct = float(allPct) * 100

#print '<li>', ystime
#print '<li>', ystimeldc
#print '<li>', allPct
#----E input----------------------------------------------------------------------------------------------------
#------------------S read BMPlistM.txt from pldc----------------------------------------------------------------
if ( ystimeldc[0] == '2' ) :
  bmpDataFile = open('../pldc/tmp/' + str(ystimeldc) + '/STEPL_BMP_LIST.txt','r')
  bmpData1 = bmpDataFile.readlines()
  bmpDataFile.close()
else :
  bmpDataFile = open('../pldc/BMPlistM.txt','r')
  bmpData1 = bmpDataFile.readlines()
  bmpDataFile.close()

for i in range(len(bmpData1)) :
  bmpData1[i] = bmpData1[i].replace('\r','')
  bmpData1[i] = bmpData1[i].replace('\n','')
  bmpData1[i] = bmpData1[i].split('\t')
#  print '<li>', bmpData1[i]


#------------------E read BMPlistM.txt from pldc----------------------------------------------------------------





#----------------------------------------------------------S HTML-----------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL WEB</title>'
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
print '<form name=main method="POST" action="./multibmp2.cgi">'
print '<center><br>'

print '<font color=tomato face="Times New Roman"><b>Define Load type, Interest rate, and Required Pollutant Reduction</b></font><br>'
print '<table border=0 width=900>'
print '  <tr>'
print '    <td align=left><font face="Times New Roman">Define Load Type:</font>'
print '      <select name=LoadType>'
print '        <option value="X">---'
print '        <option value="N">Nitrogen'
print '        <option value="P">Phosphorus'
print '        <option value="B">BOD'
print '        <option value="S">Sediment'
print '      <select>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">Interest Rate: <input type=text name=interest size=2 style="text-align:right" value="4">%</font>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=left>'
allPct = str('%.2f'%allPct)
print '      <font face="Times New Roman">Required Pollutant Reduction: <input type=text name=allPct size=2 style="text-align:right" value="' + allPct + '">%</font>'
print '    </td>'
print '  </tr>'
print '</table>'

print '<hr>'
print '<font color=tomato face="Times New Roman"><b>Set Costs</b></font><br>'

print '<table border=0 width=900>'
print '  <tr>'
print '    <td><font size=2 face="Times New Roman">'
print '      <font color=tomato><sup><b>1</b></sup></font>E. Cost: Establishment Cost ($ per ac)<br>'
print '      <font color=tomato><sup><b>2</b></sup></font>M. Cost: Annual Maintenance Cost (% of establishment cost)<br>'
print '      <font color=tomato><sup><b>3</b></sup></font>Life: BMP Design Life (year)'
print '    </font></td>'
print '  </tr>'
print '</table>'

print '<table border=1 width=900>'
print '  <tr>'
print '    <td rowspan=2 align=center><font size=2 face="Times New Roman">Landuse</font></td>'
print '    <td rowspan=2 align=center width=250><font size=2 face="Times New Roman">BMP Name</font></td>'
print '    <td colspan=4 align=center><font size=2 face="Times New Roman">BMP Efficiency (fraction)</td>'
print '    <td rowspan=2 align=center><font face="Times New Roman"><font size=2>E. Cost</font><font color=tomato><sup><b>1</b></sup></font></td>'
print '    <td rowspan=2 align=center><font face="Times New Roman"><font size=2>M. Cost</font><font color=tomato><sup><b>2</b></sup></font></td>'
print '    <td rowspan=2 align=center><font face="Times New Roman"><font size=2>Life</font><font color=tomato><sup><b>3</b></sup></font></td>'
print '  </tr>'
print '  <tr>'
print '    <td align=center><font size=2 face="Times New Roman">N</font></td>'
print '    <td align=center><font size=2 face="Times New Roman">P</font></td>'
print '    <td align=center><font size=2 face="Times New Roman">BOD</font></td>'
print '    <td align=center><font size=2 face="Times New Roman">S</font></td>'
print '  </tr>'
for i in range(1,len(bmpData1)) :
  print '  <tr>'
  for j in range(len(bmpData1[i])) :
    if ( j != 6 ) :							# type
      if ( 1 < j ) :
	boxSize = 2
      elif ( j == 0 ) :
	boxSize = 10
      else :
	boxSize = 50 
      if ( j < 2 ) :
        readOnly = 'readonly'
      else :
        readOnly = ''
      print '    <td align=center>'
      print '      <input type=text name="bmpdata_' + str(i) + '_' + str(j) + '" value="' + str(bmpData1[i][j])
      if ( 2 <= j ) :
        print ' " size="' + str(boxSize) + '" ' + readOnly + ' style="text-align:right" >'
      else :
	print ' " size="' + str(boxSize) + '" ' + readOnly + '>'
      print '    </td>'
  print '  </tr>'
print '</table>'

print '<input type=hidden name=ystime value="' + str(ystime) + '">'
for i in range(1,5) :
  for j in range(1,10) :
    UrbnConcStr = '<input type=hidden name="UrbnConc_' + str(i) + str(j) + '" size=3>'
    print UrbnConcStr
print '<hr>'

print '<input type=submit style="width:150;heigh:30;cursor:hand" value="Next">'

print '</form>'
print '</body>'
print '</html>'
#----------------------------------------------------------E HTML-----------------------------------------------



























