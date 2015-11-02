#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '  <title>STEPL WEB</title>'
print '<script>'
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
print '</head>'


print '<body onLoad="init();">'
print '<form name=gwMain>'
print '  <br><div style = "text-align:center">'
print '  <table style="margin: 0 auto; width : 400px" border=1 >'
print '    <tr  style = "text-align:center">'
print '      <td  style = "text-align:center; color:blue; font-weight: bold;" colspan=5>'
print '       Reference Soil Infiltration Fraction for Precipitation'
print '      </td>'
print '    </tr>'
print '    <tr>'
print '      <td  style="text-align:center; background-color:#BDBDBD; width:100px">HSG</td>'
print '      <td  style="text-align:center; background-color:#BDBDBD; width:75px">A</td>'
print '      <td  style="text-align:center; background-color:#BDBDBD; width:75px">B</td>'
print '      <td  style="text-align:center; background-color:#BDBDBD; width:75px">C</td>'
print '      <td  style="text-align:center; background-color:#BDBDBD; width:75px">D</td>'
print '    </tr>'

luseArr = ['Urban','Cropland','Pastureland','Forest','User Defined']
for i in range(5) :
  print '  <tr>'
  print '    <td style = "text-align:left">', luseArr[i], '</td>'
  for j in range(4) :
    print '    <td style = "text-align:right">'
    txtBoxStr = '<input type=text style="text-align:right;border-width:0px;font-size:9pt" size=6 '
    txtBoxStr += 'name=gwInft_' + str(i+1) + str(j+1) + ' value="--">'
    print txtBoxStr
    print '    </td>'
  print '</tr>'

print '</table><br>'
print 'If you have changed any value in the table, click "Update" button.<br>'

print '<input style="WIDTH:200px;height:30px;CURSOR:hand" type=button value="Update" onClick="javascript:returnVal()">'
print '</div>'
print '</form>'
print '</body>'


print '</html>'



#----E HTML-----------------------------------------------------------------------------------------------------
