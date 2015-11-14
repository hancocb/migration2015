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

numWSD = str(form.getvalue('numWSD'))

#----S HTML-----------------------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>County Data</title>'
print '</head>'
print '<body>'
print '  <br><center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD>State</td>'
print '      <td align=center bgcolor=#BDBDBD>County</td>'
print '    </tr>'
print '    <tr align=middle>'
print '      <td align=center width=160>'
print '        <iframe name=StateFrame src="./CountyData_0.html" frameborder=0 width=160 height=60 scrolling="no"></iframe>'
print '      </td>'
print '      <td align=center width=240>'
print '        <iframe name=CountyFrame src="./CountyData_1.cgi" frameborder=0 width=240 height=60 scrolling="no"></iframe>'
print '      </td>'
print '    </tr>'
print '  </table>'
tmpStr = '<iframe name=CountyData_3_Frame src="./CountyData_3.cgi?numWSD=' + str(numWSD) + '" frameborder=0 width=500 height=260 scrolling="no"></iframe>'
print tmpStr
print '</body>'
print '<script language="JavaScript">'
print 'function StateSelected() {'
print '  document.CountyFrame.CountyForm.State.value = document.StateForm.State.value ;'
print '  document.CountyFrame.CountyForm.submit() ;'
print '}'
print '</script>'
print '</html>'
#----E HTML-----------------------------------------------------------------------------------------------------

