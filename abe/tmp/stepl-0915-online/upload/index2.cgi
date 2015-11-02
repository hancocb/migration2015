#!/usr/local/bin/python
#------------------------------------------------------


import cgi, cgitb, os, random 
import cgitb; cgitb.enable()
# programmed by Youn Shik Park, park397@purdue.edu, caronys@nate.com

#------------------------------------------S do not change-------------------------------------------
import socket
ip = cgi.escape(os.environ["REMOTE_ADDR"])
form = cgi.FieldStorage()
ip = form.getvalue('rtcInput') 
rdmNum =  int('%04i' % int(random.randint(0,9999)))
tmpIP = str(rdmNum * 10000000000 + int(ip[4:]))
ip = tmpIP
fileitem = form['filename']
#------------------------------------------E do not change-------------------------------------------
#----S set Dir.--------------------------------------------------------------------------------------
ystime = ip 
path = './tmp/' 
#----E set Dir.--------------------------------------------------------------------------------------
#------------------------------------------S do not change-------------------------------------------
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open(path + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
chmod_path = 'chmod 777 ./tmp/' 
os.system(chmod_path)
chmod_path = 'chmod 777 ./tmp/*.*'
os.system(chmod_path)

print """\
Content-Type: text/html\n
"""



