#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL WEB</title>'
print '</head>'

print '<script language="JavaScript">'
print '  function init() {'
for i in range(5) :
  for j in range(4) :
    jsStr = '    document.gwMain.gwInft_' + str(i+1) + str(j+1) + '.value = '
    jsStr += 'opener.document.inputMain.gwInft_' + str(i+1) + str(j+1) + '.value ;'
    print jsStr

print '  }'

print '  function returnVal() {'
for i in range(5) :
  for j in range(4) :
    jsStr = '    opener.document.inputMain.gwInft_' + str(i+1) + str(j+1) + '.value = '
    jsStr += 'document.gwMain.gwInft_' + str(i+1) + str(j+1) + '.value ;'
    print jsStr
print '    alert("Updated");'
print '    self.close();'
print '  }'
print '</script>'


print '<body onLoad="init();">'
print '<form name=gwMain>'
print '  <br><center>'
print '  <table border=1 width=400>'
print '    <tr align=middle>'
print '      <td align=center colspan=5>'
print '        <b><font color=blue>Reference Soil Infiltration Fraction for Precipitation</font></b>'
print '      </td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD width=100>HSG</td>'
print '      <td align=center bgcolor=#BDBDBD width=75>A</td>'
print '      <td align=center bgcolor=#BDBDBD width=75>B</td>'
print '      <td align=center bgcolor=#BDBDBD width=75>C</td>'
print '      <td align=center bgcolor=#BDBDBD width=75>D</td>'
print '    </tr>'

luseArr = ['Urban','Cropland','Pastureland','Forest','User Defined']
for i in range(5) :
  print '  <tr>'
  print '    <td align=left>', luseArr[i], '</td>'
  for j in range(4) :
    print '    <td align=right>'
    txtBoxStr = '<input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 '
    txtBoxStr += 'name=gwInft_' + str(i+1) + str(j+1) + ' value="--">'
    print txtBoxStr
    print '    </td>'
  print '</tr>'

print '</table><br>'
print 'If you have changed any value in the table, click "Update" button.<br>'

print '<input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Update" onClick="javascript:returnVal()">'

print '</form>'
print '</body>'


print '</html>'



#----E HTML-----------------------------------------------------------------------------------------------------
