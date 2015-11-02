#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
numWSD = int(form.getvalue('numWSD'))
#----E input----------------------------------------------------------------------------------------------------
#---------------S HTML------------------------------------------------------------------------------------------
print '<html>'
print '<head> <title>Urban BMP</title> </head>'
print '<body onLoad="init(); LoadBack();">'
print '<form name=main>'
print '<br><center>'
print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=10><font color=blue>Urban pollutant <b>concentration</b> in runoff (mg/l)</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center>TN</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_11></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_12></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_13></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_14></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_15></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_16></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_17></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_18></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_19></td>'
print '    </tr>'
print '      <td align=center>TP</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_21></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_22></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_23></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_24></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_25></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_26></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_27></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_28></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_29></td>'
print '    </tr>'
print '      <td align=center>BOD</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_31></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_32></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_33></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_34></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_35></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_36></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_37></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_38></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_39></td>'
print '    </tr>'
print '      <td align=center>TSS</td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_41></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_42></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_43></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_44></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_45></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_46></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_47></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_48></td>'
print '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=UrbnConc_49></td>'
print '    </tr>'
print '  </table>'
print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Update" onClick="javascript:returnConc()">'
print '  <hr><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=11><font color=blue>Effective BMP application <b>area</b> (ac)</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
for i in range(1,numWSD) :
  print '  <tr>'
  tmpStr = 'W' + str(i)
  print '    <td align=center>', tmpStr, '</td>'

  print ' <td><input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=ubArea_' + str(i) +' value=0.0 readonly></td>'

  for j in range(1,10) :
    tmpName = 'UrbanBMP_1_' + str('%02i' % int(i)) + str(j) 
    tmpStr = 'onClick="javascript:window.open(\'./urBMP_onClick.cgi?i='+ str(i) + '&j=' + str(j) + '\'' +  ',\'BMPwindos\', \'status=0,toolbar=0,height=200,width=500\');"'
    print '    <td align=center>'
    print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0 ', tmpStr, '>'
    print '    </td>'
  print '  </tr>'
print '  </table><br><br>'

print '  <hr><font color=tomato>'
print '  Following tables will be updated, depends on the \'<b>Effective BMP application area (ac)</b>\' table.'
print '  </font><hr><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=10><font color=blue>Selected urban <b>N</b> reduction efficiency</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
for i in range(1,numWSD) :
  print '  <tr>'
  tmpStr = 'W' + str(i)
  print '    <td align=center>', tmpStr, '</td>'
  for j in range(1,10) :
    tmpName = 'UrbanBMP_2_' + str('%02i' % int(i)) + str(j)
    print '    <td align=center>'
    print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0>'
    print '    </td>'
  print '  </tr>'
print '  </table><br><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=10><font color=blue>Selected urban <b>P</b> reduction efficiency</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
for i in range(1,numWSD) :
  print '  <tr>'
  tmpStr = 'W' + str(i)
  print '    <td align=center>', tmpStr, '</td>'
  for j in range(1,10) :
    tmpName = 'UrbanBMP_3_' + str('%02i' % int(i)) + str(j)
    print '    <td align=center>'
    print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0>'
    print '    </td>'
  print '  </tr>'
print '  </table><br><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=10><font color=blue>Selected urban <b>BOD</b> reduction efficiency</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
for i in range(1,numWSD) :
  print '  <tr>'
  tmpStr = 'W' + str(i)
  print '    <td align=center>', tmpStr, '</td>'
  for j in range(1,10) :
    tmpName = 'UrbanBMP_4_' + str('%02i' % int(i)) + str(j)
    print '    <td align=center>'
    print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0>'
    print '    </td>'
  print '  </tr>'
print '  </table><br><br>'

print '  <table border=1>'
print '    <tr>'
print '      <td align=center colspan=10><font color=blue>Selected urban <b>TSS</b> reduction efficiency</td>'
print '    </tr>'
print '    <tr>'
print '      <td align=center bgcolor=#BDBDBD><b>Landuse</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Commercial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Industrial</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Institutional</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Transportation</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Multi-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Single-Family</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Urban-Cultivated</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Vacant (developed)</td>'
print '      <td align=center bgcolor=#BDBDBD><b>Open Space</td>'
print '    </tr>'
for i in range(1,numWSD) :
  print '  <tr>'
  tmpStr = 'W' + str(i)
  print '    <td align=center>', tmpStr, '</td>'
  for j in range(1,10) :
    tmpName = 'UrbanBMP_5_' + str('%02i' % int(i)) + str(j)
    print '    <td align=center>'
    print '      <input type=text style="text-align:right;border-width:0px;font-size:11pt" size=5 name=', tmpName, ' value=0.0>'
    print '    </td>'
  print '  </tr>'
print '  </table><br><hr><br>'

print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Load Previous Set" onClick="javascript:LoadBack()">'
print '  <input style="WIDTH:200;height:30;CURSOR:hand" type=button value="Set" onClick="javascript:returnVal()">'
print '</form>'
print '</body>'
print '<script language="JavaScript">'
print 'function init() {'
for i in range(1,5) :
  for j in range(1,10) :
    tmpStr = '  document.main.UrbnConc_' + str(i) + str(j) + '.value = opener.document.bmpMain.UrbnConc_' + str(i) + str(j) + '.value ;'
    print tmpStr

for i in range(1,numWSD):
  print 'document.main.ubArea_' + str(i) + '.value = opener.document.ubForm.ubArea_0' + str(i) + '.value ;'

print '}'
print 'function returnConc() {'
for i in range(1,5) :
  for j in range(1,10) :
    tmpStr = '  opener.document.bmpMain.UrbnConc_' + str(i) + str(j) + '.value = document.main.UrbnConc_' + str(i) + str(j) + '.value ;'
    print tmpStr
print '}'

print 'function returnVal() {'
for i in range(1,numWSD) :
  for j in range(1,6) :
    for k in range(1,10) :
      tmpName = 'UrbanBMP_' + str(j) + '_' + str('%02i' % int(i)) + str(k)
      sndStr_1 = '  opener.document.bmpMain.' + tmpName + '.value = '
      sndStr_2 = 'document.main.' + tmpName + '.value ;'
      print sndStr_1, sndStr_2

      #Change value on page urBMP
      tmpName = 'UrbanBMP_1_' + str('%02i' % int(i)) + str(k)
      sndStr_1 = '  opener.document.bmpMain.' + 'UrbanBMP_1_0' + str('%02i' % int(i)) + str(k) + '.value = '
      sndStr_2 = 'document.main.' + tmpName + '.value ;'
      print sndStr_1, sndStr_2

      print ' if (document.main.' + tmpName + '.value != 0 )'
      print '   opener.document.bmpMain.urBMP_' + str(i) + '.value = "Selected";'
      print '   opener.document.bmpMain.urBMP_' + str(i) + '.style = "text-align:right;border-width:0px;font-size:11pt;color:black;";'

print ' alert("Done"); '
print ' window.close(); '
print '}'
print 'function LoadBack() {'
for i in range(1,numWSD) :
  for j in range(1,6) :
    for k in range(1,10) :
      tmpName = 'UrbanBMP_' + str(j) + '_' + str('%02i' % int(i)) + str(k)
      sndStr_1 = 'opener.document.bmpMain.' + tmpName + '.value ;'
      sndStr_2 = '  document.main.' + tmpName + '.value = '
      print sndStr_2, sndStr_1
print '}'
print '</script>'
print '</html>'
#---------------E HTML------------------------------------------------------------------------------------------















