#!/usr/local/bin/python
#-------------------w3c Validated-----------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

numWSD = str(form.getvalue('numWSD'))

#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '  <title>County Data</title>'
print '<script>'
print 'function StateSelected() {'
print '  document.CountyFrame.CountyForm.State.value = document.StateForm.State.value; '
print '  document.CountyFrame.CountyForm.submit() ;'
print '}'
print 'function updateState() { '
print '	document.StateFrame.StateForm.State.value = opener.document.inputMain.State.value; '
print '	document.StateFrame.StateSelected(); '
#print '	document.CountyFrame.CountyForm.County.value =  opener.document.inputMain.CountyName.value;'
#print ' alert( document.CountyFrame.CountyForm.State.value + " " + document.CountyFrame.CountyForm.County.value ) ;'
print '}'
print '</script>'
print '</head>'

print '<body onload="updateState()">'
print '  <br><div style = "text-align:center">'
print '  <table style="margin: 0 auto;" border=1 >'
print '    <tr>'
print '      <td style="text-align:center; background-color:#BDBDBD;">State</td>'
print '      <td style="text-align:center; background-color:#BDBDBD;">County</td>'
print '    </tr>'
print '    <tr style = "text-align:center">'
print '      <td style="width:160; text-align:center">'
print '        <iframe name=StateFrame src="./CountyData_0.html" style="border: 0px; overflow:hidden;" width=160 height=60 ></iframe>'
print '      </td>'
print '      <td style="width:240; text-align:center">'
print '        <iframe name=CountyFrame src="./CountyData_1.cgi" style="border: 0px; overflow:hidden;" width=240 height=60 ></iframe>'
print '      </td>'
print '    </tr>'
print '  </table>'
tmpStr = '<iframe name=CountyData_3_Frame src="./CountyData_3.cgi?numWSD=' + str(numWSD) + '" style="border: 0px; overflow:hidden;" width=500 height=260 ></iframe>'
print tmpStr
print '</div>'
print '</body>'

print '</html>'
#----E HTML-----------------------------------------------------------------------------------------------------

