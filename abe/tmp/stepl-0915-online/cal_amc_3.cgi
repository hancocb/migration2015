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
print '<html>'
print '<head>'
print '  <title>STEPL WEB</title>'
#--------------S Check Status-----------------------------------------------------------------------------------
staList_1 = glob.glob(path + 'amc_status*')
staList_2 = []

for i in range(len(staList_1)) :
  staList_1[i] = staList_1[i].split('amc_status_')
  staList_1[i][1] = staList_1[i][1].replace('.pys','')
  staList_2.append(str(staList_1[i][1]))

finChk = 'no'
staList_3 = []
for i in range(len(staList_2)) :
  if ( staList_2[i] == 'w' ) :
    staList_3.append('1_Annual runoff and baseflow were calibrated.')
  elif ( staList_2[i] == 's' ) :
    staList_3.append('2_Sediment load was calibrated.')
  elif ( staList_2[i] == 'n' ) :
    staList_3.append('3_Nitrogen load was calibrated.')
  elif ( staList_2[i] == 'p' ) :
    staList_3.append('4_Phosphorus load was calibrated.')
  elif ( staList_2[i] == 'b' ) :
    staList_3.append('5_BOD load was calibrated.')
  elif ( staList_2[i] == 'd' ) :
    finChk = 'yes'

staList_3.sort()
#print '<li>', staList_3
#--------------E Check Status-----------------------------------------------------------------------------------
#-----------------------------S Refresh or Print----------------------------------------------------------------
if ( finChk == 'no' ) :
  rfsStr =  '<meta http-equiv="refresh" content="10;url=./cal_amc_3.cgi?ystime=' + ystime + '">'
  print rfsStr
  print '</head>'
  print '<body>'
  print '<br><br><br><br><center>'
  print '<b>Calibration Status</b><br>'
  print '<table border=0>'
  print '  <tr>'
  print '    <td align=left>'
  for i in range(len(staList_3)) :
    print staList_3[i][2:], '<br>'
  print '    </td>'
  print '  </tr>'
  print '</table><br><br>'
  print '<b>The module is still working..</b><br>'
  print '<img src="./img/loading.gif" width=100><br>'
  print '<b>Please wait..</b>'

else :
  cpCmd = 'cp ' + path + 'myOptPar.pys ./tmp/' + ystime + '/.'
  os.system(cpCmd)
  #----sim. & obs.
  simFile = open(path + 'stepl_rst.pys','r')
  simVal = simFile.readlines()
  simFile.close()
  obsFile = open(path + 'stepl_obs.pys','r')
  obsVal = obsFile.readlines()
  obsFile.close()

  for i in range(len(obsVal)) :
    obsVal[i] = obsVal[i].replace('\r','')
    obsVal[i] = obsVal[i].replace('\n','')
    simVal[i] = simVal[i].replace('\r','')
    simVal[i] = simVal[i].replace('\n','')
    obsVal[i] = float(obsVal[i])
    simVal[i] = float(simVal[i])
  ParName = ['Runoff (ac-ft)', 'Baseflow (ac-ft)', 'Nitrogen (lbs)', 'Phosphorus (lbs)', 'BOD (lbs)', 'Sediment (tons)']

  #--- opt. val
  optFile = open(path + 'myOptPar.pys','r')
  myVals = optFile.readlines()
  optFile.close()

  for i in range(len(myVals)) :
    myVals[i] = myVals[i].replace('\r','')
    myVals[i] = myVals[i].replace('\n','')
#    myVals[i] = '%.3f'%myVals[i]

  print '</head>'
  print '<br><br><center>'
  print '<hr>'
  print '<b>Calibration Report</b><br>'
  print '<table border=1 width=400>'
  print '  <tr>'
  print '    <td></td>'
  print '    <td align=center bgcolor=#BDBDBD>Observed</td>'
  print '    <td align=center bgcolor=#BDBDBD>Estimated</td>'
  print '    <td align=center bgcolor=#BDBDBD>Fractios</td>'
  print '  </tr>'
  for i in range(len(obsVal)) :
    if ( float(obsVal[i]) < 99999999.99 ) :
      print '  <tr>'
      print '    <td align=right bgcolor=#BDBDBD>', ParName[i], '</td>'
      print '    <td align=right>', '%.2f'%obsVal[i], '</td>'
      print '    <td align=right>', '%.2f'%simVal[i], '</td>'
      print '    <td align=right>', '%.3f'%float(myVals[i]), '</td>'
      print '  </tr>'

  print '</table><br>'

  print '<b>Model parameters have been calibrated. <br>'
  print 'Continue your simulation from the window for BMP set.'
  print '<body>'
#-----------------------------E Refresh or Print----------------------------------------------------------------




print '</body>'
print '</html>'


























