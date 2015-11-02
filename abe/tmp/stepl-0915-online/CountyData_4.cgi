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

numWSD = int(form.getvalue('numWSD'))

#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>  </title>'
print '</head>'
print '<body>'
print '<input type=hidden name="Caller" value="None"> '
print '<form name=CountyData_3>'
print '<center>'
print '  <table border=1 width=400>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>R</td>'
print '      <td align=center bgcolor=#BDBDBD><b>K</td>'
print '      <td align=center bgcolor=#BDBDBD><b>LS</td>'
print '      <td align=center bgcolor=#BDBDBD><b>C</td>'
print '      <td align=center bgcolor=#BDBDBD><b>P</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>'
print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=usleR>'
print '      </td>'
print '      <td align=center>'
print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=usleK>'
print '      </td>'
print '      <td align=center>'
print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=usleLS>'
print '      </td>'
print '      <td align=center>'
print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=usleC>'
print '      </td>'
print '      <td align=center>'
print '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=4 name=usleP>'
print '      </td>'
print '    </tr>'
print '  </table><br>'
print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Select" onClick="javascript:sendPcpInfo()">'
print '</form>'
print '</body>'
print '<script language="JavaScript">'
print 'function sendPcpInfo() {'
#----send USLE
print '  alert( document.getElementsByName("Caller")[0].value );'
print '  var tmpVal = document.CountyData_3.usleC.value ;'
print '  tmpVal = Math.round(tmpVal*100) / 100 ;'
print '  if ( tmpVal < 0.2 ) {'
print '    tmpVal = 0.2 ;'
print '  }                             // STEPL uses 0.2 for minimum USLE C of Cropland.'
print ''
for i in range(1,numWSD+1) :
    tmpStr = ' top.document.inputMain.usleCropland_1' + str('%02i'%i) + '.value = document.CountyData_3.usleR.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleCropland_2' + str('%02i'%i) + '.value = document.CountyData_3.usleK.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleCropland_3' + str('%02i'%i) + '.value = document.CountyData_3.usleLS.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleCropland_4' + str('%02i'%i) + '.value = tmpVal ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleCropland_5' + str('%02i'%i) + '.value = document.CountyData_3.usleP.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.uslePasture_1' + str('%02i'%i) + '.value = document.CountyData_3.usleR.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.uslePasture_2' + str('%02i'%i) + '.value = document.CountyData_3.usleK.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.uslePasture_3' + str('%02i'%i) + '.value = document.CountyData_3.usleLS.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.uslePasture_4' + str('%02i'%i) + '.value = "0.04" ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.uslePasture_5' + str('%02i'%i) + '.value = document.CountyData_3.usleP.value ;'
    print tmpStr

    tmpStr = ' top.document.inputMain.usleForest_1' + str('%02i'%i) + '.value = document.CountyData_3.usleR.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleForest_2' + str('%02i'%i) + '.value = document.CountyData_3.usleK.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleForest_3' + str('%02i'%i) + '.value = document.CountyData_3.usleLS.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleForest_4' + str('%02i'%i) + '.value = "0.003" ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleForest_5' + str('%02i'%i) + '.value = document.CountyData_3.usleP.value ;'
    print tmpStr

    tmpStr = ' top.document.inputMain.usleUser_1' + str('%02i'%i) + '.value = document.CountyData_3.usleR.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleUser_2' + str('%02i'%i) + '.value = document.CountyData_3.usleK.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleUser_3' + str('%02i'%i) + '.value = document.CountyData_3.usleLS.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleUser_4' + str('%02i'%i) + '.value = document.CountyData_3.usleC.value ;'
    print tmpStr
    tmpStr = ' top.document.inputMain.usleUser_5' + str('%02i'%i) + '.value = document.CountyData_3.usleC.value ;'
    print tmpStr
#print '  alert("Updated");'
print '}'
print '</script>'
print '</html>'
#----E HTML-----------------------------------------------------------------------------------------------------




















