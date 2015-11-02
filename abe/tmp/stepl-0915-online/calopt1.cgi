#!/usr/local/bin/python
#-----------------w3c Validated-------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
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
gabtn += '&amp;ystimeldc='
gabtn += ystimeldc
gabtn += '\');">'

amcbtn = '<input type=button style=\'width:200;height:30;cursor:hand\' value=\'Bisection Method\' '
amcbtn += 'onClick="javascript:window.open(\'./cal_amc_1.cgi?ystime='
amcbtn += ystime
amcbtn += '&amp;ystimeldc='
amcbtn += ystimeldc
amcbtn += '\');">'
#----E input----------------------------------------------------------------------------------------------------
#---------------------S HTML------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '  <title>STEPL Auto-Calibration Option</title>'
print '</head>'
print '<body>'
print '<br><br>'
print '<div style="font-weight:bold; text-align:center;">Auto-Calibration Module Option</div><br>'
print '<table style=" width:600px; border:0; margin:0 auto;">'
print '  <tr>'
print '    <td style="text-align:left; ">'
print '      Two methods are provided. Select one of them. <br>'
print '      Both methods calibrate :'
print '      <ul> '
print '      <li><span style="font-weight:bold;">Curve Numbers</span> for annual runoff<br>'
print '      <span style="font-size:0.82em">("Input Form" - "Change Optional Input" - "Step 6. Reference runoff curve number")</span>'
print '      <li><span style="font-weight:bold;">Soil Infiltration Fraction for Precipitation</span> for annual baseflow<br>'
print '      <span style="font-size:0.82em">("Input Form" - "Soil Infiltration Fraction for Precipitation")</span>'
print '      <li><span style="font-weight:bold;">Nutrient Concentration</span> for annual nutrient loads<br>'
print '      <span style="font-size:0.82em">("Input Form" - "Change Optional Input" - "Step 7" and "Step 7a")</span>'
print '      </ul> '
print '    </td>'
print '  </tr>'
print '</table>'
print '<table border=1 style=" width:600px;  margin:0 auto;">'
print '  <tr>'
print '    <td style="text-align:center; background-color:#BDBDBD;  ">Bisection Method</td>'
print '  </tr>'
print '  <tr>'
print '    <td style="text-align:center;">', amcbtn, '</td>'
print '  </tr>'
print '  <tr>'
print '    <td style="vertical-align:top; width:300px;">'
print '      Annual runoff and baseflow will be calibrated.<br>'
print '      When observed loads are given, <span style="color:red">those </span>pollutant loads will be calibrated.<br><br>'
print '      It will take <span style="color:red">2-3 minutes</span> to finish calibration. After calibration is done,'
print '      continue your simulation from the open browser page "BMP Sets".<br><br>'
print '      The calibration iterates through the model parameters. The module runs STEPL to find the model parameter '
print '      leading to the least difference between the observed and the estimated loads, similar to a manual calibration.<br>'
print '      The bisection method is a simple and straightforward numerical method, is applicable to continuous functions, '
print '      and has been applied to solve simple problems (Ashkar and Mahdi, 2006; Hong et al., 2006; Neupauer and Brochers, 2001).<br><br>'
print '      The method sets intervals and selects the midpoint which shows the least error during iteration, narrowing the intervals. Initial '
print '      intervals (e.g. 50% to 150% for CNs) need to be set, and iterative computations are required until the error (e.g. difference between '
print '      observed annual direct runoff and estimated annual direct runoff) is zero or less than a specified tolerance. <br><br>'
print '      The module in STEPL WEB performs the iterations until the intervals are in the thousandth digits for the fractions in equation 5.8-11.<br><br>'
print '      <p>Calibrated CN = Fr<sub>cn</sub>&#8901Default CN<span style="float:right">Eq. 5.8</span></p>'
print '      <p>Coeff.<sub>cal.</sub> = Fr<sub>nt,i</sub>&#8901Coeff.<sub>default</sub><span style="float:right">Eq. 5.9</span></p>'
print '      <p>SDR = Fr<sub>sdr</sub>&#8901 0.42 &#8901 A<sup>-0.135</sup> - 0.127, if A >= 0.81<span style="float:right">Eq. 5.10</span></p>'
print '      <p style="text-indent: 50px;">Fr<sub>sdr</sub>&#8901 0.42 &#8901 A<sup>-0,125</sup>, if A < 0.81<span style="float:right">Eq. 5.11</span></p><br>'
print '      Where, Fr<sub>cn</sub> is calibration parameter or fraction for CN, Fr<sub>nt,i</sub> is calibration parameter for pollutant coefficients, Fr<sub>sdr</sub> '
print '      is calibration parameter for SDR, and A is watershed area in square kilometers.'
print '    </td>'
print '  </tr>'
print '</table>'
print '<table style=" width:600px; border:0; margin:0 auto;">'
print '  <tr>'
print '    <td style="text-align:left; ">'
print '<p>[ <a href="http://docs.lib.purdue.edu/dissertations/AAI3636487/">Park Thesis</a> | <a href="https://engineering.purdue.edu/mapserve/ldc/STEPL/referenceList.html">References</a> ]</p>'
print '		<a href="https://engineering.purdue.edu/mapserve/ldc/ "><p style="text-align:left">Purdue Load duration Curve</p></a>'
print '		<a href="https://engineering.purdue.edu/~what/ "><p style="text-align:left">WHAT Hydrologic Separation</p></a>'
print '    </td>'
print '  </tr>'
print '</table>'
print '</body>'
print '</html>'
#---------------------E HTML------------------------------------------------------------------------------------






