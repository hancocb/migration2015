#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
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
numWSD = int(form.getvalue('numWSD'))

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
print '<meta charset="UTF-8">'
print '  <title>STEPL WEB</title>'
print '<script>'
print 'function init() {'
for i in range(1,5) :
  for j in range(1,10) :
    tmpStr = '  document.main.UrbnConc_' + str(i) + str(j) + '.value = opener.document.bmpMain.UrbnConc_' + str(i) + str(j) + '.value ;'
    print tmpStr
print '}'
print 'function complete(){'
print '  if ( ( document.main.allPct.value '
print '  == 0.0 ) || ( document.main.LoadType.value.localeCompare("X") == 0) )'
print '   alert( "Please fill in the Load Type and Pollutant Reduction field in order to proceed." );'
print '  else'
print '   document.main.submit();'
print '}'
print '</script>'
print '</head>'
print '<body onLoad="init();">'
print '<form name=main method="POST" action="./multibmp2.cgi">'
print '<div style="text-align:center;"><br>'

print '<span style="color:tomato; font-family:Times New Roman;"><b>Define Load type, Interest rate, and Required Pollutant Reduction</b></span><br>'
print '<table style="width:900px; border:0">'
print '  <tr>'
print '    <td style="text-align:left;"><span style="font-family:Times New Roman;">Select Watershed:</span>'
print '      <select name=Watershed>'
for i in range(1, numWSD):
  print '        <option value=' + str(i) + '>W' + str(i);
print '      </select>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td style="text-align:left;"><span style="font-family:Times New Roman;">Define Load Type:</span>'
print '      <select name=LoadType>'
print '        <option value="X">---'
print '        <option value="N">Nitrogen'
print '        <option value="P">Phosphorus'
print '        <option value="B">BOD'
print '        <option value="S">Sediment'
print '      </select>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td style="text-align:left;">'
print '      <span style="font-family:Times New Roman;">Interest Rate: <input type=text name=interest size=2 style="text-align:right" value="4">%</span>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td style="text-align:left;">'
allPct = str('%.2f'%allPct)
print '      <span style="font-family:Times New Roman;">Required Pollutant Reduction: <input type=text name=allPct size=2 style="text-align:right" value="' + allPct + '">%</span>'
print '    </td>'
print '  </tr>'
print '   <tr>'
print '    <td style="text-align:left;">'
print '<input type=button style="width:150;height:30;cursor:hand;text-align:left;" type=button onClick="complete()" value="Next">'
print '    </td>'
print '  </tr>'
print '</table>'



print '<hr>'
print '<span style="color:tomato; font-family:Times New Roman;"><b>Set Costs</b></span><br>'

print '<table style="width:900px; border:0">'
print '  <tr>'
print '    <td><div style="size:2; font-family:Times New Roman; text-align:left">'
print '      <span style="color:tomato;"><sup><b>1</b></sup></span>E. Cost: Establishment Cost ($ per ac)<br>'
print '      <span style="color:tomato;"><sup><b>2</b></sup></span>M. Cost: Annual Maintenance Cost (% of establishment cost)<br>'
print '      <span style="color:tomato;"><sup><b>3</b></sup></span>Life: BMP Design Life (year)'
print '    </div></td>'
print '  </tr>'
print '</table>'

print '<table style="width:900px;" border=1>'
print '  <tr>'

print '    <td style="text-align:center" rowspan=2><span style="size:2; font-family:Times New Roman;">Landuse</span></td>'

print '    <td style="text-align:center; width:250;" rowspan=2><span style="size:2; font-family=Times New Roman;">BMP Name</span></td>'

print '    <td style="text-align:center" colspan=4><span style="size:2; font-family:Times New Roman;">BMP Efficiency (fraction)</span></td>'
print '    <td style="text-align:center" rowspan=2><span style="size:2; font-family:Times New Roman;">E. Cost</span><span style="color:tomato;"><sup><b>1</b></sup></span> ($)</td>'
print '    <td style="text-align:center" rowspan=2><span style="size:2; font-family:Times New Roman;">M. Cost</span><span style="color:tomato;"><sup><b>2</b></sup></span> (%)</td>'
print '    <td style="text-align:center" rowspan=2><span style="size:2; font-family:Times New Roman;">Life</span><span style="color:tomato;"><sup><b>3</b></sup></span> (years)</td>'
print '  </tr>'

print '  <tr>'
print '    <td style="text-align:center"><span style="size:2; font-family:Times New Roman;">N</span></td>'
print '    <td style="text-align:center"><span style="size:2; font-family:Times New Roman;">P</span></td>'
print '    <td style="text-align:center"><span style="size:2; font-family:Times New Roman;">BOD</span></td>'
print '    <td style="text-align:center"><span style="size:2; font-family:Times New Roman;">S</span></td>'
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
      print '    <td style="text-align:center">'
      print '      <input type=text name="bmpdata_' + str(i) + '_' + str(j) + '" value="' + str(bmpData1[i][j]) + '"'
      if ( 2 <= j ) :
        print 'style="text-align:right; width:' + str(boxSize) + '" ' + readOnly + ' >'
      else :
        print 'style="width:' + str(boxSize) + '" ' + readOnly + '>'
      print '    </td>'
  print '  </tr>'
print '</table>'

print '<input type=hidden name=ystime value="' + str(ystime) + '">'
for i in range(1,5) :
  for j in range(1,10) :
    UrbnConcStr = '<input type=hidden name="UrbnConc_' + str(i) + str(j) + '" style="width:3">'
    print UrbnConcStr



print '</div>'
print '</form>'
print '</body>'
print '</html>'
#----------------------------------------------------------E HTML-----------------------------------------------



























