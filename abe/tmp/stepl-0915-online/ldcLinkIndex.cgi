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
ystimeldc = str(form.getvalue('ystimeldc'))
allPct = str(form.getvalue('allPct'))

#print '<li>', ystimeldc, allPct

#----E input----------------------------------------------------------------------------------------------------
#----------------S HTML-----------------------------------------------------------------------------------------
indexFile = open('./index.html','r')
indexCnt = indexFile.readlines()
indexFile.close()

for i in range(len(indexCnt)) :
  tmpStr = indexCnt[i].split('ystimeldc')
  if ( 1 < len(tmpStr) ) :
    tmpStr2 = '    <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
    tmpStr2 += '<input type=hidden name=allPct value="' + allPct + '">'
    print tmpStr2
  else :
    print indexCnt[i]
#----------------E HTML-----------------------------------------------------------------------------------------
























