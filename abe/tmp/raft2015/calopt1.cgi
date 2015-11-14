#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob, math
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
ystimeldc = str(form.getvalue('ystimeldc'))

gabtn = '<input type=button style=\'width:200;height:30;cursor:hand\' value=\'Genetic Algorithm\' '
gabtn += 'onClick="javascript:window.open(\'./cal_1.cgi?ystime='
gabtn += ystime
gabtn += '&ystimeldc='
gabtn += ystimeldc
gabtn += '\');">'

amcbtn = '<input type=button style=\'width:200;height:30;cursor:hand\' value=\'Bisection Method\' '
amcbtn += 'onClick="javascript:window.open(\'./cal_amc_1.cgi?ystime='
amcbtn += ystime
amcbtn += '&ystimeldc='
amcbtn += ystimeldc
amcbtn += '\');">'
#----E input----------------------------------------------------------------------------------------------------
#---------------------S HTML------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL Auto-Calibration Option</title>'
print '</head>'
print '<body>'
print '<br><br><center>'
print '<b><font face="Times New Roman">Auto-Calibration Module Option</font></b><br><br>'
print '<table border=0 width=600>'
print '  <tr>'
print '    <td align=left>'
print '      <font face="Times New Roman">'
print '      Two methods are provided. Select one of them. <br>'
print '      Both methods calibrate :'
print '      <li><b>Curve Numbers</b> for annual runoff<br>'
print '      <font size=2>("Input Form" - "Change Optional Input" - "Step 6. Reference runoff curve number")</font>'
print '      <li><b>Soil Infiltration Fraction for Precipitation</b> for annual baseflow<br>'
print '      <font size=2>("Input Form" - "Soil Infiltration Fraction for Precipitation")</font>'
print '      <li><b>Nutrient Concentration</b> for annual nutrient loads<br>'
print '      <font size=2>("Input Form" - "Change Optional Input" - "Step 7" and "Step 7a")</font>'
print '      </font>'
print '    </td>'
print '  </tr>'
print '</table><br>'
print '<table border=1 width=600>'
print '  <tr>'
print '    <td align=center bgcolor=#BDBDBD><font face="Times New Roman">Genetic Algorithm</font></td>'
print '    <td align=center bgcolor=#BDBDBD><font face="Times New Roman">Bisection Method</font></td>'
print '  </tr>'
print '  <tr>'
print '    <td align=center>', gabtn, '</td>'
print '    <td align=center>', amcbtn, '</td>'
print '  </tr>'
print '  <tr>'
print '    <td valign=top width=300>'
print '      <font face="Times New Roman">'
print '      Genetic Algorithm calibrates the model parameters.<br>'
print '      Annual runoff and baseflow will be calibrated.'
print '      <font color=red>Only one </font>pollutant load '
print '      (i.e. nitrogen or phosphorus or BOD or sediment) will be calibrated.'
print '      It will take <font color=red>20-30 minutes</font> to finish calibration, the module will send you an e-mail'
print '      when calibration is finished. Once you received an e-mail from the module,'
print '      you may continue your simulation from the window "BMP Sets".'
print '      Note that you can NOT turn off the web browsers for "Input Form" and "BMP Sets".'
print '      </font>'
print '    </td>'
print '    <td valign=top width=300>'
print '      <font face="Times New Roman">'
print '      Annual runoff and baseflow will be calibrated.'
print '      As long as observed loads are given, <font color=red>any </font>'
print '      or <font color=red>all</font> pollutant loads will be calibrated.'
print '      It will take <font color=red>2-3 minutes</font> to finish calibration. After calibration is done,'
print '      continue your simulation from "BMP Sets".<br>'
print '      Changing the model parameters, the module runs STEPL to find the model parameter leading to '
print '      the least difference between the observed and the estimated loads, similarly to manual calibration.'
print '      As the developer of the model, <b>the method is recommended</b>.'
print '      </font>'
print '    </td>'
print '  </tr>'
print '</table>'
print '</body>'
print '</html>'
#---------------------E HTML------------------------------------------------------------------------------------






