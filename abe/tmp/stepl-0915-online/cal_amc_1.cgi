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

mkdirPath = 'mkdir ./tmp/' + ystime + '/cal'
chmodPath = 'chmod 777 ./tmp/' + ystime + '/cal'
cpOptPath = 'cp amc_stepl ./tmp/' + ystime + '/cal/.'
cpInpPath = 'cp ./tmp/' + ystime + '/inp/*.* ./tmp/' + ystime + '/cal/.'
cpPcpPath = 'cp ./tmp/' + ystime + '/cligen/pcp.txt ./tmp/' + ystime + '/cal/.'

#--del cal if exist
delPrvCal = glob.glob('./tmp/' + ystime + '/*')
PrvCalDir = ''
for i in range(len(delPrvCal)) :
  if ( delPrvCal[i][-3:] == 'cal' ) :
    DelStr = 'rm -rf ' + delPrvCal[i]
    print '<li>Previous calibration was deleted..'
    os.system(DelStr)
    PrvCalDir = delPrvCal[i]

path = './tmp/' + ystime + '/cal/'

os.system(mkdirPath)
os.system(chmodPath)
os.system(cpOptPath)
os.system(cpInpPath)
os.system(cpPcpPath)

#print '<li>', ystime, ystimeldc
#----E input----------------------------------------------------------------------------------------------------
#-----------------------S read flow and wq data from LDC--------------------------------------------------------
AnRuff = 0.0 
AnBsfl = 0.0
AnLoad = 0.0
sltWQname = ' '


if ( ystimeldc[0] == '2' ) : 								# 2013...
  ldcPath = '../pldc/tmp/' + ystimeldc + '/'

  sltWQnameFile = open(ldcPath + 'sltWQname.pys','r')					# N, P, B, S
  sltWQnameTmp = sltWQnameFile.readlines()
  sltWQnameFile.close()
  sltWQname = str(sltWQnameTmp[0][0])

  bfiFile = open(ldcPath + 'myBFIforSTEPL.txt','r')
  bfi = bfiFile.readline()
  bfiFile.close()
  bfi = float(bfi)

  simChk = glob.glob(ldcPath + '*.ind')							# LOADEST run ?
  myFlow = []

  if ( len(simChk) == 0 ) :								# if LOADEST not run
    myLoad = 0.0
    LoadCnt = 0
    ldcDataFile = open(ldcPath + 'LDCinput.txt','r')
    ldcData = ldcDataFile.readlines()
    ldcDataFile.close()
    for i in range(len(ldcData)) :
      ldcData[i] = ldcData[i].replace('\r','')
      ldcData[i] = ldcData[i].replace('\n','')
      ldcData[i] = ldcData[i].split('\t')
      myFlow.append(float(ldcData[i][1]))
      if ( str(ldcData[i][2]) != '' ) :
	myLoad += float(ldcData[i][1]) * float(ldcData[i][2]) * 5.3937			# unit: lb
        LoadCnt += 1
    AnLoad = myLoad / float(LoadCnt) * 365.0						# AnLoad is annual load
  else :										# if LOADEST run
    myLoad = 0.0
    indFile = open(simChk[0],'r')
    ind = indFile.readlines()
    indFile.close()
    for i in range(8,len(ind)) :							# actual result stars from line 8
      ind[i] = ind[i].split()
      myFlow.append(float(ind[i][2]))
      myLoad += float(ind[i][3])
    AnLoad = myLoad / float(len(ind)-8) * 365.0  
  if ( sltWQname == 'S' ) : 
    AnLoad = AnLoad * 0.000454								# sediment is ton in STEPL

  myBsfl = [0.0] * len(myFlow)
  myRuff = [0.0] * len(myFlow)
  myRuff[0] = myFlow[0]/2.0
  myBsfl[0] = myFlow[0]/2.0
  AnFlow = 0.0
  AnRuff = 0.0
  AnBsfl = 0.0
  for i in range(1,len(myFlow)) :
    tmpVal = (((1 - bfi) * 0.98 * myBsfl[i-1]) + ((1 - 0.98) * bfi * myFlow[i])) / (1-0.98*bfi)
    if ( myFlow[i] <= tmpVal ) :
      tmpVal = myFlow[i]
    myBsfl[i] = tmpVal
    myRuff[i] = myFlow[i] - myBsfl[i]
    AnBsfl += myBsfl[i] * 86400 * 0.000023						# cfs -> ac-ft
    AnRuff += myRuff[i] * 86400 * 0.000023
    AnFlow += myFlow[i] * 86400 * 0.000023
  AnFlow = AnFlow / float(len(myFlow)) * 365.0
  AnBsfl = AnBsfl / float(len(myFlow)) * 365.0						# annual flow in ac-ft
  AnRuff = AnRuff / float(len(myFlow)) * 365.0
#  print '<li>', AnBsfl, AnRuff, AnFlow 


#-----------------------E read flow and wq data from LDC--------------------------------------------------------
#----------------------------------------------------------S wqName selection-----------------------------------
sltWQnameArr = [' ', ' ', ' ', ' ']
if ( sltWQname == 'N' ) :
  sltWQnameArr[0] = ' selected'
elif ( sltWQname == 'P' ) :
  sltWQnameArr[1] = ' selected'
elif ( sltWQname == 'B' ) :
  sltWQnameArr[2] = ' selected'
elif ( sltWQname == 'S' ) :
  sltWQnameArr[3] = ' selected'
#----------------------------------------------------------E wqName selection-----------------------------------
#-----------------S HTML----------------------------------------------------------------------------------------
print '<html>'
print '<head>'
print '  <title>STEPL WEB Auto-Calibration Module</title>'
print '  <script language="JavaScript">'
print '    function convert() {'
print '      var myObj = document.CalMain.usrObj.value ;'
print '      var myVal = document.CalMain.usrVal.value ;'
print '      var myUnt = document.CalMain.usrUnit.value ;'
print '      myVal = myVal.replace(" ","");'
print '      myVal = myVal.replace(",","");'
print '      if ( myVal != "" ) {'				# if valid value
print '        myVal = myVal * 1.0 ;'				# convert to float
#----runoff
print '        if ( myObj == "R" ) {' 				# runoff
print '          if ( myUnt == "CM" ) {'			# cubic meter
print '            myVal = myVal * 0.000247 * 3.28084 ;'	
print '          } else if ( myUnt == "CF" ) {'			# cubic feet
print '            myVal = myVal * 0.000023 ;'
print '          } else {'
print '            alert("Select unit for annual runoff.");'
print '          }'
print '          myVal = Math.round(myVal*10000) / 10000 ;'
print '          document.CalMain.runoff.value = myVal ;'
#----baseflow
print '        } else if ( myObj == "B" ) {'
print '          if ( myUnt == "CM" ) {'                        # cubic meter
print '            myVal = myVal * 0.000247 * 3.28084 ;'
print '          } else if ( myUnt == "CF" ) {'         	# cubic feet
print '            myVal = myVal * 0.000023 ;'
print '          } else {'
print '            alert("Select unit for annual baseflow.");'
print '          }'
print '          myVal = Math.round(myVal*10000) / 10000 ;'
print '          document.CalMain.baseflow.value = myVal ;'
#----load
print '        } else {'
print '          myVal = myVal * 1.0 ;'
print '          var wqName = document.CalMain.usrObj.value ;'
print '          if ( myUnt == "LB" ) {'
print '            if ( myObj == "6" ) {'			# s
print '              myVal = myVal * 0.000454 ;'
print '            } else {'
print '              myVal = myVal ;'
print '            }'
print '            myVal = Math.round(myVal*10000) / 10000 ;'
print '            if ( wqName == "3" ) {'
print '              document.CalMain.myN.value = myVal ;'
print '            } else if ( wqName == "4" ) {'
print '              document.CalMain.myP.value = myVal ;'
print '            } else if ( wqName == "5" ) {'
print '              document.CalMain.myB.value = myVal ;'
print '            } else {'
print '              document.CalMain.myS.value = myVal ;'
print '           }'
print '          } else if ( myUnt == "KG" ) {'
print '            if ( myObj == "6" ) {'
print '              myVal = myVal * 0.001 ;'
print '            } else {'
print '              myVal = myVal * 2.204623 ;'
print '            }'
print '            myVal = Math.round(myVal*10000) / 10000 ;'
print '            if ( wqName == "3" ) {'
print '              document.CalMain.myN.value = myVal ;'
print '            } else if ( wqName == "4" ) {'
print '              document.CalMain.myP.value = myVal ;'
print '            } else if ( wqName == "5" ) {'
print '              document.CalMain.myB.value = myVal ;'
print '            } else {'
print '              document.CalMain.myS.value = myVal ;'
print '           }'
print '          } else {'
print '            alert("Select unit for annual load.");'
print '          }'


print '        }'
print '      } else {'
print '        alert("Empty Value");'
print '      }'


print '    }'
print '    function initVal() {'
tmpStr = '      document.CalMain.my' + sltWQname + '.value = ' + str(AnLoad) + ';'
print tmpStr
print '    }'

print '   function validateFormValues() {'
print '     if (document.CalMain.runoff.value == "" || document.CalMain.baseflow.value == "" || parseFloat(document.CalMain.runoff.value) <= 0 || parseFloat(document.CalMain.baseflow.value) <= 0) {'
print '       alert("Value of Runoff and Baseflow should be larger than 0.");'
print '     } else {'
print '       if ( parseFloat(document.CalMain.myN.value) == 0 &&  parseFloat(document.CalMain.myP.value) <= 0 &&  parseFloat(document.CalMain.myB.value) <= 0 &&  parseFloat(document.CalMain.myS.value) <= 0) {'
print '         var r = confirm("Because they are blank, no loads will be calibrated. Is that your intent?");'
print '         if (r == true) {'
print '           document.CalMain.submit();'
print '         }'
print '       }'
print '       else{'
print '         document.CalMain.submit();'
print '       }'
print '     }'
print '   }'

print '  </script>'
print '</head>'
if ( ystimeldc[0] == '2' ) :
  print '<body onLoad="initVal();">'
else : 
  print '<body>'
print '<form name=CalMain method=POST action="./cal_amc_2.cgi"><center><br><br>'

print '<hr>'

print '<table border=1 width=600>' 
print '<tr>'
print '  <td align=center colspan=2 bgcolor=#BDBDBD>'
print '    <b>Annual Runoff, Baseflow, and Pollutant Loads for Model Calibration</b>'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual Runoff:</td>'
print '  <td align=right>'
print '    <input type=text name=runoff size=10 value="' + str(AnRuff) + '" style="text-align:right" required> &nbsp; ac-ft'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual Baseflow:</td>'
print '  <td align=right>'
print '    <input type=text name=baseflow size=10 value="' + str(AnBsfl) + '" style="text-align:right" required> &nbsp; ac-ft'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual Nitrogen</td>'
print '  <td align=right>'
print '    <input type=text name=myN size=10 value="0.0" style="text-align:right"><b><sup>*</sup></b> &nbsp; lbs/yr'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual Phosphorus</td>'
print '  <td align=right>'
print '    <input type=text name=myP size=10 value="0.0" style="text-align:right"><b><sup>*</sup></b> &nbsp; lbs/yr'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual BOD</td>'
print '  <td align=right>'
print '    <input type=text name=myB size=10 value="0.0" style="text-align:right"><b><sup>*</sup></b> &nbsp; lbs/yr'
print '  </td>'
print '</tr>'
print '<tr>'
print '  <td align=right bgcolor=#BDBDBD>Annual Sediment</td>'
print '  <td align=right>'
print '    <input type=text name=myS size=10 value="0.0" style="text-align:right"><b><sup>*</sup></b> &nbsp; ton/yr'
print '  </td>'
print '</tr>'

print '</table>'
print '<table border=0 width=600>'
print '  <tr>'
print '    <td align=right><sup>*</sup>If the value is zero(i.e. 0), the water quality parameter will not be calibrated.'
print '  </tr>'
print '</table><br>'


if ( ystimeldc[0] == '2' ) :
  print '<font size=2 color="tomato">'
  print '"Annual Runoff", "Annual Baseflow", and "Annual Loads" were calculated by LDC results.<br>'
  print '</font>'

print '<hr>'

tmpStr = '<input type=hidden name=ystime value="' + ystime + '">'
print tmpStr
print '<input type=button onclick="validateFormValues()" style=\'width:200;height:30;cursor:hand\' value=\'Calibrate\'>'


#----Unit converter
print '<br><br><hr>'
print '<table width=600 border=1>'
print '  <tr>'
print '    <td colspan=2 bgcolor=#BDBDBD>'
print '      <center><b>Unit Converter (Optional)</b></center>'
print '      <font size=2>The values in the table above needs to be "ac-ft", "lbs", or "tons".'
print '      If you need to convert the value you have, this will be helpful.'
print '      1) Define what you want to convert, 2) input the value, 3) define the unit of the value you inputted.'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>Select Objective : </td>'
print '    <td align=center><select name=usrObj>'
print '                       <option value="R">Annual Runoff'
print '                       <option value="B">Annual Baseflow'
print '                       <option value="3">Annual Nitrogen'
print '                       <option value="4">Annual Phosphorus'
print '                       <option value="5">Annual BOD'
print '                       <option value="6">Annusl Sediment'
print '                     </select>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>Input Value : </td>'
print '    <td align=center><input type=text name=usrVal size=10>'
print '  </tr>'
print '  <tr>'
print '    <td align=right>Unit :</td>'
print '    <td align=center><select name=usrUnit>'
print '                       <option value="CF">cubic feet'
print '                       <option value="CM">cubic meter'
print '                       <option value="LB">pounds'
print '                       <option value="KG">killo grams'
print '                     </select>'
print '    </td>'
print '  </tr>'
print '  <tr>'
print '    <td align=center colspan=2>'
print '      <input type=button style="width:180;height:24;cursor:hand" value="Convert" onClick="javascript:convert()">'
print '    </td>'
print '  </tr>'
print '</table>'

print '</form>'
print '</body>'
print '</html>'

#-----------------E HTML----------------------------------------------------------------------------------------



























