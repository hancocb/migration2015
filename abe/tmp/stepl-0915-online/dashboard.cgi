#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>"
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, find 'Table1', 'Table2',...
# to jump, find 'BMPinputs', 'ubForm', 'JavaScript'

def isFloat(string):
  try:
    ret = float(string)
  except:
    ret = 0
  return ret

def isInt(string):
  try:
    ret = int(string)
  except:
    ret = 0
  return ret

def isStr(string):
  try:
    ret = str(string);
  except:
    ret = 0
  return ret

#----S input----------------------------------------------------------------------------------------------------
ystimeldc = str(form.getvalue('ystimeldc'))     # if from LDC
allPct = str(form.getvalue('allPct'))

rerun = 0
numWSD = 0
numGLY = 0
numSTR = 0
histLog = None

try:
  histLog = str(form.getvalue('logNum'))
except:
  histLog = None

try: 
  numWSD = int(form.getvalue('numWSD'))
  numGLY = int(form.getvalue('numGLY'))
  numGLY = int(form.getvalue('numSTR'))
  rerun = int(form.getvalue('rerun'))
except:
  numWSD = 0
  numGLY = 0
  numSTR = 0
  rerun = 0

ystime = 0

if histLog != None:
  ystime = histLog
else:
  ystime = str(form.getvalue('ystime'))

path = './tmp/' + ystime + '/'
simDir = glob.glob(path + 'sim_*')
status = isInt(len(simDir))

#----S HTML-----------------------------------------------------------------------------------------------
print '<html>'
print '<head><title>Web-based STEPL</title><meta charset="UTF-8"></head>'
print '<body"><br>'

print '<div style="text-align:center"><img src="./img/STEPL_WEB_title.jpg" style="width:400px" alt=""></div><br><hr><br>'

print '<div style="text-align:center; ">Dashboard</div><br><hr><br>'

print '  <table style="margin: 0px auto; width: 900px" border=0>'
print '   <tr><td style="width:300px;text-align:center">Input Form</td><td style="width:300px;text-align:center">BMPs</td><td style="width:300px;text-align:center">Results</td></tr>'
print '   <tr><td style="padding: 5px;text-align:center;vertical-align:top" rowspan=', str(status+1) ,'><input style="WIDTH:200px;height:30px;CURSOR:hand;" type=button onClick="complete()" value="Main Input"></td></tr>'
for i in range(1,status+1):
  print '   <tr>'
  print '   <td style="padding: 3px;text-align:center"><input style="WIDTH:200px;height:25px;CURSOR:hand;" type=button onClick="complete' + str(i) + '()" value="sim_'+ str(i) +'"></td>'
  print '   <td style="padding: 3px;text-align:center"><input style="WIDTH:200px;height:25px;CURSOR:hand;" type=button onClick="complete()" value="sim_'+ str(i) +'"></td>'
  print '   </tr>'
print ''
print ''
print ''
print '  </table><br><hr>'

print '<form name=main method="POST" action="./inputMain.cgi" target="new">'
print ' <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
print ' <input type=hidden name=logNum value="' + histLog + '">'
print ' <input type=hidden name=numWSD value="' + str(numWSD) + '">'
print ' <input type=hidden name=numGLY value="' + str(numGLY) + '">'
print ' <input type=hidden name=numSTR value="' + str(numSTR) + '">'
print ' <input type=hidden name=rerun value="' + str(rerun) + '">'
print ' <input type=hidden name=ystime value="' + ystime + '">'
print ' <input type=hidden name=allPct value="' + allPct + '">'
print ' <input type=hidden name=simLog value="0">'
print ' </form>'

#print '<input style="WIDTH:200px;height:30px;CURSOR:hand;" type=button onClick="complete()" value="Next"></div><br><br>'
#----S JavaScript-----------------------------------------------------------------------------------------------
print '<script language="JavaScript">'
print 'function complete() {  '
print ' document.main.rerun.value = 1;'
print ' document.main.submit();'
print '}'

for i in range(1,status+1):
  print 'function complete' + str(i) + '() {  '
  print ' document.main.rerun.value = 3;'
  print ' document.main.simLog.value = ' + str(i) +';'
  print ''
  print ''
  print ' document.main.submit();'
  print '}'

print '</script>'
#----E JavaScript-----------------------------------------------------------------------------------------------



print '</body>'
print '</html>'


