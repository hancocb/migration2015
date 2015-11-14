#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
path = './tmp/' + ystime + '/cal/'


#----E input----------------------------------------------------------------------------------------------------
#---------------------------------------------------S HTML------------------------------------------------------
print '<html>'
print '<head><title>STEPL WEB</title></head>'
print '<body>'

print '<center><br><br><br><br>'
print 'Do <b><font color=red>NOT</font></b> turn off the web browsers for <b>watershed inputs </b>and <b>BMPs</b>.<br><br>'
print 'The model will send you an e-mail when auto-calibration is finished.<br><br>'
print 'It will take 10-30 minutes, approximately.<br>'
print '<hr>'
print 'Your scenario name is <b>', ystime, '</b><br>'

print '</body>'
print '</html>'


#---------------------------------------------------E HTML------------------------------------------------------


























