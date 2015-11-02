#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
# programmed by Youn Shik Park, parkyounshik@gmail.com, caronys@nate.com

import cgi, cgitb, os, string, random, datetime
import time, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

tmpStr = 'python ./sendMail.py'
os.system(tmpStr)



