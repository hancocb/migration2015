#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
NumGully = int(form.getvalue('numGLY'))
NumStreambank = int(form.getvalue('numSTR'))
numWSD = int(form.getvalue('numWSD'))

#----E input----------------------------------------------------------------------------------------------------
#----------------S HTML-----------------------------------------------------------------------------------------
print '<html>'
print '<head> <title>Gully & Streambank Erosion</title> </head>'
print '<body onLoad="init();"> <center><br>'
print '<form name=GS>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=9>'
print '        <font color=blue><b>Gully dimensions in the different watersheds'
print '      </td>'
print '    </tr>'
print '    <tr>' 
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Gully</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Top Width (ft)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Bottom Width (ft)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Depth (ft)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Length (ft)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Years to Form</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMP Efficiency (0-1)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Soil Texture Class</td>'
print '    </tr>'

for j in range(1,NumGully+1) :
  print '    <tr>'
  print '      <td align=center>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '1'
  print '        <select name=', tmpName, '>'
  for i in range(1,numWSD+1) :
    tmpStr = 'W' + str(i)
    print '<option value=', i, '>', tmpStr
  print '        </select>'
  print '      </td>' 
  tmpName = 'GS1_' + str('%02i' % int(j)) + '2'
  tmpStr = 'Gully' + str('%02i' % int(j))
  print '      <td align=center>', tmpStr, '<input type=hidden style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', j, '></td>' 
  tmpName = 'GS1_' + str('%02i' % int(j)) + '3'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '4'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '5'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '6'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '7'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '8'
  print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.95></td>'
  tmpName = 'GS1_' + str('%02i' % int(j)) + '9'
  print '      <td align=center><select name=', tmpName, '>'
  print '                         <option value=1>Clay'
  print '                         <option value=2>Clay loam'
  print '                         <option value=3>Fine Sandy loam'
  print '                         <option value=4>Loams sandy clay loams'
  print '                         <option value=5>Organic'
  print '                         <option value=6>Sands Loamy sands'
  print '                         <option value=7>Sandy clay'
  print '                         <option value=8>Sandy loam'
  print '                         <option value=9>Silt Loam'
  print '                         <option value=10>Silty clay loam silty clay'
  print '                       </select>'
  print '      </td>'
  print '    </tr>'
print '  </table><br><hr><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Watershed</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Stream Bank</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Length (ft)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Height (ft) </td>'
print '      <td align=center bgcolor=#BDBDBD><b>Lateral Recession</td>'
print '      <td align=center bgcolor=#BDBDBD><b>BMP Efficiency (0-1)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Soil Texture Class</td>'
print '    </tr>'

for j in range(1, NumStreambank+1) :
  print '    <tr>'
  print '      <td align=center>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '1'
  print '        <select name=', tmpName, '>'
  for i in range(1,numWSD+1) :
    tmpStr = 'W' + str(i)
    print '<option value=', i, '>', tmpStr
  print '        </select>'
  print '      </td>'
  tmpStr = 'Bank' + str(j)
  tmpName = 'GS2_' + str('%02i' % int(j)) + '2'
  print '      <td align=center>', tmpStr
  print '        <input type=hidden style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=', j, '></td>'
  print '      </td>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '3'
  print '      <td align=center>'
  print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  print '      </td>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '4'
  print '      <td align=center>'
  print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.0></td>'
  print '      </td>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '5'
  print '      <td align=center>'
  print '        <select name=', tmpName, '>'
  print '          <option value=1>Slight'
  print '          <option value=2>Moderate'
  print '          <option value=3>Severe'
  print '          <option value=4>Very Severe'
  print '        </select>'
  print '      </td>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '6'
  print '      <td align=center>'
  print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=', tmpName, ' value=0.95></td>'
  print '      </td>'
  tmpName = 'GS2_' + str('%02i' % int(j)) + '7'
  print '      <td align=center>'
  print '        <select name=', tmpName, '>'
  print '                         <option value=1>Clay'
  print '                         <option value=2>Clay loam'
  print '                         <option value=3>Fine Sandy loam'
  print '                         <option value=4>Loams, sandy clay loams'
  print '                         <option value=5>Organic'
  print '                         <option value=6>Sands, Loamy sands'
  print '                         <option value=7>Sandy clay'
  print '                         <option value=8>Sandy loam'
  print '                         <option value=9>Silt Loam'
  print '                         <option value=10>Silty clay loam, silty clay'
  print '        </select>'
  print '      </td>'
  print '</tr>'
print '  </table><br>'
print '  <input type=hidden name=NumGully value=', NumGully, '>'
print '  <input type=hidden name=NumStreambank value=', NumStreambank, '>'

print '<input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Update" onClick="javascript:returnVal()">'
#print '<input style="WIDTH:200;height:30;CURSOR:hand" type=submit value="Update">'

print '</form>'
print '</body>'

print '<script language="JavaScript">'
print 'function init() {'
for i in range(1,NumGully+1) :
  for j in range(1,10) :
    if ( j != 2 ) :
      tmpStr = '  document.GS.GS1_' + str('%02i'%i) + str(j) + '.value = opener.document.inputMain.GS1_' + str('%02i'%i) + str(j) + '.value ;'
      print tmpStr
for i in range(1,NumStreambank+1) :
  for j in range(1,8) :
    if ( j != 2 ) :
      tmpStr = '  document.GS.GS2_' + str('%02i'%i) + str(j) + '.value = opener.document.inputMain.GS2_' + str('%02i'%i) + str(j) + '.value ;'
      print tmpStr
print '}'

print 'function returnVal() {'
for i in range(1,NumGully+1) :
  for j in range(1,10) :
    tmpStr = '  opener.document.inputMain.GS1_' + str('%02i'%i) + str(j) + '.value = document.GS.GS1_' + str('%02i'%i) + str(j) + '.value ;'
    print tmpStr
for i in range(1,NumStreambank+1) :
  for j in range(1,8) :
    tmpStr = '  opener.document.inputMain.GS2_' + str('%02i'%i) + str(j) + '.value = document.GS.GS2_' + str('%02i'%i) + str(j) + '.value ;'
    print tmpStr

print '  alert("Updated") ;'
print '  self.close();'
print '}'
print '</script>'

print '</html>'

#----------------E HTML-----------------------------------------------------------------------------------------






















