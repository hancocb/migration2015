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
runoff = str(form.getvalue('runoff'))
baseflow = str(form.getvalue('baseflow'))
myWQ = [0.0,0.0,0.0,0.0]
myWQ[0] = float(form.getvalue('myN'))
myWQ[1] = float(form.getvalue('myP'))
myWQ[2] = float(form.getvalue('myB'))
myWQ[3] = float(form.getvalue('myS'))
ystime = str(form.getvalue('ystime'))
path = './tmp/' + ystime + '/cal/'

#print '<li>', ystime, runoff, baseflow
#print '<li>', myWQ
#----E input----------------------------------------------------------------------------------------------------
#-----------------------------S stepl_obs.pys-------------------------------------------------------------------
obs = open(path + 'stepl_obs.pys','w')
obs.write(runoff + '\n')
obs.write(baseflow + '\n')
for i in range(len(myWQ)) :
  if ( 0.0 < myWQ[i] ) :
    obs.write(str(myWQ[i]) + '\n')
  else :
    obs.write('99999999.99\n')
obs.close()
#-----------------------------E stepl_obs.pys-------------------------------------------------------------------
#----S numWSD---------------------------------------------------------------------------------------------------
mainInpFile = open('./tmp/' + ystime + '/inp/mainINP.txt','r')
mainInp = mainInpFile.readlines()
mainInpFile.close()

numWSD = 1
mainInp[0] = mainInp[0].split('\t')
numWSD = int(mainInp[0][0])
#print '<li>', numWSD
#----E numWSD---------------------------------------------------------------------------------------------------
#---------------------------------------------S temporary BMP files---------------------------------------------
rptStr_1 = '        N       P       BOD     Sediment        AppliedArea\n'
rptStr_2 = '0.0000  0.0000  0.0000  0.0000  100.0000\n'
rptStr_3 = '0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000  0.0000\n'


bmp = open(path + 'BMPs.txt','w')
for i in range(5) :
  bmp.write(rptStr_1)
  for j in range(numWSD) :
    bmp.write(rptStr_2)
  bmp.write('\n')

bmp.write('2.0000  2.5000  1.8000  3.0000  2.2000  2.2000  1.9000  1.5000  1.5000\n')
bmp.write('0.2000  0.4000  0.3000  0.5000  0.4000  0.4000  0.3000  0.2000  0.2000\n')
bmp.write('9.3000  9.0000  7.8000  9.3000  10.0000 10.0000 4.0000  4.0000  4.0000\n')
bmp.write('75.0000 120.0000        67.0000 150.0000        100.0000        100.0000        150.0000        70.0000 70.0000\n\n')

for i in range(5) :
  for j in range(numWSD) :
    bmp.write(rptStr_3)
  bmp.write('\n')
bmp.close()
#---------------------------------------------E temporary BMP files---------------------------------------------
#-------------------------------------------------------------------------S set files---------------------------
cpAMCPath = 'cp ./runAMC_1.* ' + path + '.'
os.system(cpAMCPath)

cpCmd = 'cp stepl_amc ./tmp/' + ystime + '/stepl'
os.system(cpCmd)
#-------------------------------------------------------------------------E set files---------------------------
#-----------------S HTML----------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STPL WEB Auto-Calibration Module</title>'
rfsStr =  '<meta http-equiv="refresh" content="10;url=./cal_amc_3.cgi?ystime=' + ystime + '">'
print rfsStr
print '</head>'
print '<body>'
print '<form name=OptMain>'

#ifrStr2 = '<iframe name=runGAFrame src="' + path + 'sendMail.html" frameborder=0 width=240 height=60 scrolling="no"></iframe>'
#print ifrStr2
ifrStr = '<iframe name=runGAFrame src="' + path + 'runAMC_1.html" frameborder=0 width=240 height=60 scrolling="no"></iframe>'
print ifrStr

print '  <center><br><br><br><br>'
print '  <img src="./img/loading.gif" width=200><br>'
print 'Auto-Calibration Initiating....'
print '<hr>'


print '</form>'
print '</body>'
print '</html>'

#-----------------E HTML----------------------------------------------------------------------------------------























chmod777 = 'chmod 777 ' + path + '/*.*'
os.system(chmod777)



