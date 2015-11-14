#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------

import cgi, cgitb, os
form = cgi.FieldStorage()
cgitb.enable()

pw = form.getvalue('password')

print '<br><br><br><br><center>'

if pw == '12250211' :
  os.system('rm -rf ./tmp/*')
  print 'Deleted all files in "tmp"'
else :
  print 'You are not permitted to do this. '

print '<li> Last Line '
