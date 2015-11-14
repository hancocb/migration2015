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


#print '<li>', path
#----E input----------------------------------------------------------------------------------------------------
#---------------------------------------------------S HTML------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>Auto-Calibration Results</title>'
print '</head>'
print '<body>'
#cpOptFile = 'cp ' + path + 'myOptPar.pys ./tmp/' + ystime + '/.'
#os.system(cpOptFile)
print '<center><br><br>'
print '<font color=tomato>Auto-Calibration Summary</font>'
print '<hr>'
simFile = open(path + 'stepl_rst.pys','r')
simVal = simFile.readlines()
simFile.close()
obsFile = open(path + 'stepl_obs.pys','r')
obsVal = obsFile.readlines()
obsFile.close()
wqName = ['Nitrogen','Phosphorus','BOD','Sediment']
SltWQ = int(obsVal[-1])
print '<table border=1 width=500>'
print '  <tr>'
print '    <td align=center width=200> </td>'
print '    <td align=center>Observed</td>'
print '    <td align=center>Estimated</td>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>Runoff (ac-ft)</td>'
print '    <td align=right>', '%.2f'%float(obsVal[0]), '</td>'
print '    <td align=right>', '%.2f'%float(simVal[0]), '</td>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>Baseflow (ac-ft)</td>'
print '    <td align=right>', '%.2f'%float(obsVal[1]), '</td>'
print '    <td align=right>', '%.2f'%float(simVal[1]), '</td>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>', wqName[SltWQ-3], '(<sup>*</sup>unit)</td>'
print '    <td align=right>', '%.2f'%float(obsVal[SltWQ-1]), '</td>'
print '    <td align=right>', '%.2f'%float(simVal[SltWQ-1]), '</td>'
print '  </tr>'
print '</table>'
print '<table border=0 width=500>'
print '  <tr>'
print '    <td align=right><sup>*</sup>Unit is "ton/year" for sediment and is "lb/year" for others.'
print '  </tr>'
print '</table>'
print '<hr>'

#----parameters
parFile = open(path + 'myOptParFinal.pys','r')
myPar = parFile.readlines()
parFile.close()
for i in range(len(myPar)) :
  myPar[i] = myPar[i].replace('\r','')
  myPar[i] = myPar[i].replace('\n','')
  myPar[i] = '%.4f'%float(myPar[i])
  
print '<table border=1 width=800>'
print '  <tr align=middel>'
print '    <td align=center colspan=3>Calibrated Parameter Description</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center width=200>Parameter Name</td>'
print '    <td align=center width=200>Calibrated Parameter</td>'
print '    <td align=center>Description</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>CN ratio</td>'
print '    <td align=rignt>', myPar[0], '</td>'
print '    <td align=left>CNs will be multiplied by the value.</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>GW ratio</td>'
print '    <td align=rignt>', myPar[1], '</td>'
print '    <td align=left>Groundwater infiltration rates will be multiplied by the value.</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>NT Runoff ratio</td>'
print '    <td align=rignt>', myPar[2], '</td>'
print '    <td align=left>Nutrient concentration in runoff (mg/l) will be multiplied by the value.</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>NT Groundwater ratio</td>'
print '    <td align=rignt>', myPar[3], '</td>'
print '    <td align=left>Nutrient concentration in shallow groundwater (mg/l) will be multiplied by the value.</td>'
print '  </tr>'
print '  <tr align=middle>'
print '    <td align=center>Sediment Delivery Ratio</td>'
sdr = [0.0] * 3 										# sdr coefficients
sdr[0] = 0.417662 * float(myPar[4])
sdr[1] = -0.127097 * float(myPar[4])
sdr[2] = 0.42 * float(myPar[5])
for j in range(len(sdr)) :
  sdr[j] = '%.4f'%sdr[j]
drStr = str(sdr[0]) + ' x Area<sup>-0.134958</sup> ' + str(sdr[1])
drStr += '<br>' + str(sdr[2]) + ' x Area<sup>-0.125</sup>'
print '    <td align=rignt><font size=2>', drStr, '</font></td>'
print '    <td align=left>This sediment delivery ratio formula will be used.</td>'
print '  </tr>'
print '</table>'

print '</body>'
print '</html>'
#---------------------------------------------------E HTML------------------------------------------------------
#----S remove files---------------------------------------------------------------------------------------------
ch777 = 'chmod 777 ' + path + '*'
os.system(ch777)
ch777 = 'chmod 777 ' + path + '*.*'
os.system(ch777)

#rmStatus = 'rm -rf ' + path + 'status*.pys'
#os.system(rmStatus)
#----E remove files---------------------------------------------------------------------------------------------


























