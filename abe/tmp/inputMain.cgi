#!/usr/local/bin/python
#-------------------w3c Validated-----------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>";
#print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

# to jump, fine 'Step1', 'Step2',... no space

#----S input----------------------------------------------------------------------------------------------------
ystimeldc = str(form.getvalue('ystimeldc'))			# if from LDC
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

if rerun == 3:
  rerun = 2

if rerun == 0:
  ystime = str(datetime.datetime.now())
  ystime = ystime.replace('-','')
  ystime = ystime.replace(' ','')
  ystime = ystime.replace(':','')
  ystime = ystime.replace('.','')
  rdmNum = '%04i' % int(random.randint(0,9999))
  ystime = str(ystime) + '_' + str(rdmNum)
  #ystime = '1111111111'                                           # delete this line
  mkdirPath = 'mkdir ./tmp/' + ystime
  chmodPath = 'chmod 777 ./tmp/' + ystime
  os.system(mkdirPath)
  os.system(chmodPath)

  path = './tmp/' + ystime + '/'

  #----------------------------S myOptPar.pys default-------------------------------------------------------------
  OptPar = open(path + 'myOptPar.pys','w')
  for i in range(6) :
    OptPar.write('1.00\n')
  OptPar.close()
#----------------------------E myOptPar.pys default-------------------------------------------------------------

  cpCmd = 'cp stepl ' + path + '.'
  os.system(cpCmd)
elif rerun == 1:
  if histLog != None:
    ystime = histLog
  else:
    ystime = str(form.getvalue('ystime'))
else:
  if histLog != None:
    ystime = histLog
  else:
    ystime = str(form.getvalue('ystime'))

#print '<li>', numWSD, numGLY, numSTR
#----E input----------------------------------------------------------------------------------------------------


#----------------------------S Reload History Inputs------------------------------------------------------------
if rerun == 1 or rerun == 2 :
  path = './tmp/' + ystime + '/'
  inpPath = path + 'inp/'
  cligenPath = path + 'cligen/'
  table1list = [[0 for i in range(numWSD)] for i in range(8)]
  table2list = [[0 for i in range(numWSD)] for i in range(9)]
  table3list = [[0 for i in range(numWSD)] for i in range(5)]
  table4list = [[0 for i in range(numWSD)] for i in range(5)]

  try:
    mainINP = open(inpPath + 'mainINP.txt','r')
    basicInfo = mainINP.readline()
    numWSD = int(basicInfo[0])
    mainINP.readline()
  #--------------------table 1------------------------------------------------------------
    for i in range(0, numWSD):
      table1list[i] = mainINP.readline().split('\t')
    mainINP.readline()
    #--------------------table 2------------------------------------------------------------
    for i in range(0, numWSD):
      table2list[i] = mainINP.readline().split('\t')
    mainINP.readline()
    #--------------------table 3------------------------------------------------------------
    for i in range(0, numWSD): 
      table3list[i] = mainINP.readline().split('\t')
    mainINP.close()
  except:
    for i in range(0, numWSD):
      table1list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table2list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]
      table3list[i] = ["9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9", "9.9"]

#--------------------cligen & table 4------------------------------------------------------------
  try:
    stainfo = open(cligenPath + 'stainfo.txt', 'r')
    tmpStainfo= stainfo.readline().split('\t')
    cligenStation = tmpStainfo[1]
    tmpStainfo= stainfo.readline().split()
    cligenState = tmpStainfo[1]
    tmpStainfo= stainfo.readline().split()
    cligenCounty = tmpStainfo[1]
    stainfo.close()
  except:
    cligenStation = "Select CLIGEN Station"
    cligenState = "None"
    cligenCounty = "None"

else:
    path = './tmp/' + ystime + '/'
    inpPath = path + 'inp/'
#----------------------------E Reload History Inputs------------------------------------------------------------

#------------------S HTML---------------------------------------------------------------------------------------
print '<html>'
print '<head>'
#print '<meta charset="UTF-8">'
print '  <title>Web-based STEPL</title>'
print '  <title>' + str(rerun)   + '</title>'
print '  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>'
#------------------E HTML---------------------------------------------------------------------------------------
#----------------------------S Java Script----------------------------------------------------------------------
print '<script>'
for i in range(1,numWSD+1) :
  tmpStr = '  function totArea' + str('%02i'%i) + '() {'
  print tmpStr
  for j in range(1,7) :
    tmpStr = '    var tmpArea_' + str(j) + ' = document.inputMain.LuseAreaWSD_' + str(j) + str('%02i'%i) + '.value * 1.0 ;'
    print tmpStr
  print '    tmpTotArea = tmpArea_1 + tmpArea_2 + tmpArea_3 + tmpArea_4 + tmpArea_5 + tmpArea_6 ;'
  tmpStr = '    document.inputMain.TAreaWSD_' + str('%02i'%i) + '.value = tmpTotArea ;'
  print tmpStr
  print '  }'

print 'function updateSHG(){ '
print '     document.inputMain.HSG_' + str('%02i'%i) + '.value = document.inputMain.HSG_' + str('%02i'%i) + '.value;'
print '}'

print 'function tetratechLink(){'
print '     window.open("http://it.tetratech-ffx.com/steplweb/steplweb.html");'
print '}'


print 'function complete() {  '
print '  if ( '
print ' document.inputMain.TAreaWSD_' + str('%02i'%i) + '.value'
print '  == 0.0 ) '
print '   alert( "At least one input in Step 1 should not be 0. " );'
print '  else'
print '   if(document.inputMain.State.value == "" || document.inputMain.State.value == "None")'
print '     alert("Please select a station.");'
print '   else'
print '     document.inputMain.submit();'
print ' }  '
print 'function reloadPage() {'
print ' document.cleanForm.submit(); '
print '}'
print 'function rerunCligen() {'
if rerun == 1 or rerun == 2 :
  print ' document.inputMain.State.value = "' + cligenState + '";'
  print ' document.inputMain.CountyName.value = "' + cligenCounty + '";'
  print ' updateCounty(); '
  if rerun == 2:
    print 'setInterval(function () { complete(); }, 3000); '
print '}'

print 'function simpleGraph() {'
print ' window.open("", "GraphWindow", "status=0,toolbar=0,height=500px,width=710px" ); '
print ' document.graphForm.target = "GraphWindow"; '
print ' document.graphForm.submit(); '
print '}'

print '</script>'
#----------------------------E Java Script----------------------------------------------------------------------
print '</head>'

print '<body onload=" '
for i in range(1,numWSD+1) :
  print 'totArea' + str('%02i'%i) + '(); '
print 'rerunCligen();'

print '"> '
print '  <div style="text-align:center">'
print '  <a href="index.html">'
print '  <img src="./img/STEPL_WEB_title.jpg" width=400 alt=""><br><br>'
print '  </a>'
print '  <div style="font-family:Times New Roman"><b>Input Form</b></div>'
if rerun == 2:
  print '<br><span style="color:red;"> -------------------------------------------- </span><br><br><span style="color:red;"> Redirecting... Please wait</span><br><br><span style="color:red;"> -------------------------------------------- </span><br><br>'
print '  </div><HR><br>'

if rerun == 2:
  print '<form name=inputMain method="POST" action="./bmpMain.cgi" target="_self">'
else:
  print '<form name=inputMain method="POST" action="./bmpMain.cgi" target="new">'
LdcLnkStr = '  <input type=hidden name=ystimeldc value="' + ystimeldc + '">'
print LdcLnkStr
allPctStr = '  <input type=hidden name=allPct value="' + allPct + '">'
print allPctStr

#-----------------------------------------------------------------------------------------------------------------------Step1
print '  <div style="color:blue;"><span style="font-weight:bold;">Step 1. Input watershed land use area (ac) </span></div>'
print '  <table style=" width:1000px; border:0;">'
print '    <tr>'
print '      <td style="text-align:right">'
print '        <input type=checkbox name=gwOpt checked>Groundwater load calculation'
print '      </td>'
print '      <td style="text-align:right">'
print '        <input type=checkbox name=swsOpt checked>Treat all the subwatersheds as parts of a single watershed'
print '      </td>'
print '    </tr>'
print '  </table><br>'


print '  '
print '  <table border=1 style="margin: 0 auto; width:1000px;">'
print '    <tr style="text-align:center;">'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Soil Hydrologic Group</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Urban</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Cropland</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Pastureland</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Forest</td>'

print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">User Defined</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Feedlots</td>'
print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Feedlot<br>Percent<br>Paved</td>'



print '      <td style="text-align:center; background-color:#BDBDBD; font-size:0.82em">Total</td>'
print '    </tr>'
for i in range(1,numWSD+1) :
  tmpStrW = 'W' + str(i)
  print '    <tr style="text-align:center">'
  print '      <td style="text-align:center">',tmpStrW,'</td>'
  print '      <td style = "text-align:center; border-left: solid 1px black; border-top: solid 1px black; border-right: solid 1px black; border-bottom: solid 1px black;"><select name=HSG_' + str('%02i'%i) + '><option value="1">A<option value="2">B<option value="3">C<option value="4">D</select></td>'
  for j in range(1,7) : 
    luseTmpStr = 'LuseAreaWSD_' + str(j) + str('%02i'%i)
    js_totArea = 'totArea' + str('%02i'%i)
    tmpStr = '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" name=' + luseTmpStr

    if rerun == 0:
      tmpStr = tmpStr + ' size=5 onChange="javascript:' + js_totArea +'()" value=0.0>'
    else:
      tmpStr = tmpStr + ' size=5  onChange="javascript:' + js_totArea +'()" value='+ table1list[i-1][j-1] +'>'

    print '      <td style="text-align:center;">'
    print tmpStr
    print '      </td>'
  print '      <td style="text-align:center;">'
  fdlTmpStr = '        <select name=PctFeedlot_' + str('%02i'%i) + '>'
  print fdlTmpStr
  if rerun == 0:
    print '          <option value="20">0-24 %</option>'
    print '          <option value="30">25-49 %</option>'
    print '          <option value="60">50-74 %</option>'
    print '          <option value="80">75-100 %</option>' 
  else:
    if float(table1list[i-1][6]) == 20:
      print '          <option selected="selected" value="20">0-24 %</option>'
      print '          <option value="30">25-49 %</option>'
      print '          <option value="60">50-74 %</option>'
      print '          <option value="80">75-100 %</option>' 
    elif float(table1list[i-1][6]) == 30:
      print '          <option value="20">0-24 %</option>'
      print '          <option selected="selected" value="30">25-49 %</option>'
      print '          <option value="60">50-74 %</option>'
      print '          <option value="80">75-100 %</option>'
    elif float(table1list[i-1][6]) == 60:
      print '          <option value="20">0-24 %</option>'
      print '          <option value="30">25-49 %</option>'
      print '          <option selected="selected" value="60">50-74 %</option>'
      print '          <option value="80">75-100 %</option>'
    else:
      print '          <option value="20">0-24 %</option>'
      print '          <option value="30">25-49 %</option>'
      print '          <option value="60">50-74 %</option>'
      print '          <option selected="selected" value="80">75-100 %</option>'
  print '        </select>'
  print '      </td>'
  print '      <td style="text-align:center;">'
  tmpStr = '        <input type=text style="text-align:right;border-width:0px;font-size:11pt" name=TAreaWSD_' + str('%02i'%i) + ' size=5 readonly value=0.0>'
  print tmpStr
  print '      </td>'
  print '    </tr>'
print '  </table>'
print '<table style="font-size:0.82em; color:red; margin: 0 auto; width:1000px; text-align:right;"><tr><td>&nbsp;&nbsp;*at least ONE input should not be 0.</td></tr></table>'

print '<hr><br><br>'


#-----------------------------------------------------------------------------------------------------------------------Step1a

tmpStr = '    <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'County Data\''
tmpStr = tmpStr + ' onClick="javascript:window.open(\'./CountyData.cgi?numWSD=' + str(numWSD) + '\','
tmpStr = tmpStr + '\'CountyData\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=400,width=780\');"><br>'


# This doesn't exist in EPA STEPL. This tool uses CLIGEN for annual flow.
print '  <div>For precipitation data we use CLIGEN 100 year synthetic precipitation based on the geographic location you select.</div>'
print '  <table style="width:800px; border:0;">'
print '    <tr style="text-align:center">'
#print '      <td style="text-align:right">Location of Selected Station : </td>'
print '      <td style="text-align:left">'

# changes 1
#print '        <input type=text size=30 style="text-align:right;border-width:0px;font-size:11pt" '
#print '        name="LocName" value="Select CLIGEN Station">'


teststr = '<input type=text size=30 style="text-align:left;width:150px;border-width:0px;font-size:11pt"'
if rerun == 0:
  teststr += '        name="LocName" value="Select CLIGEN Station"></td> '
else:
  teststr += '        name="LocName" value="' + cligenStation + '""></td> '
teststr += '<td><input type=hidden name="State" value="None"></td> ' 
teststr += '<td><input type=hidden name="CountyName" value="None"></td> ' 

CLIGEN_Str = '<td> <input type=hidden name="GraphButton" style=\'width:200px;height:30px;cursor:hand\' value=\'History Rainfalls\''
CLIGEN_Str += '        onClick="simpleGraph()");"> '
CLIGEN_Str += '</td>'

CLIGEN_Str += '    <td><input type=button style=\'width:200px;height:30px;cursor:hand\' value=\'CLIGEN Map\''
CLIGEN_Str += ' onClick="javascript:window.open(\'./CLIGEN/\', \'CLIGENmap\',\'status=0,toolbar=1,location=0,menubar=0,'
CLIGEN_Str += 'scrollbars=1crolling=1,height=600,width=780\');"></td>'

CLIGEN_Str += ' <td style=" text-align:left; font-size:0.82em; padding:20px; color:red; "> *The state and county of the CLIGEN station will be the default for soil data properties. '

teststr2 = '<script> '
teststr2 += 'function updateCounty() { '
teststr2 += ' var gbutton = document.getElementsByName("GraphButton")[0];'
teststr2 += ' gbutton.type = \'button\';'
teststr2 += ''
teststr2 += ''
teststr2 += ''
teststr2 += ''
teststr2 += ''
teststr2 += ''
teststr2 += '   var state = document.getElementsByName("State")[0].value;'
teststr2 += '   var countyName = document.getElementsByName("CountyName")[0].value;'
teststr2 += '   $.ajax({ url:"CountyData_2.cgi", type:"GET", data:{"State": state, "County": countyName, "numWSD" :' +  str(numWSD) + '}, success:function(response){'
#teststr2 += '   document.getElementsByName("usleCropland_101")[0].value = response;'
#teststr2 += '     alert(response);'
teststr2 += '     var str = response.split(" ");'
#teststr2 += '     if (str.length < 2) {'
#teststr2 += '       return;'
#teststr2 += '     }'
teststr2 += '     for (var i = 0; i < ' + str(numWSD) + '; i++) {'
teststr2 += '       document.getElementsByName("usleCropland_1" + ("0" + ( i + 1)) .slice(-2))[0].value = str[0 + i * 20];'
teststr2 += '       document.getElementsByName("usleCropland_2" + ("0" + ( i + 1)) .slice(-2))[0].value = str[1 + i * 20];'
teststr2 += '       document.getElementsByName("usleCropland_3" + ("0" + ( i + 1)) .slice(-2))[0].value = str[2 + i * 20];'
teststr2 += '       document.getElementsByName("usleCropland_4" + ("0" + ( i + 1)) .slice(-2))[0].value = str[3 + i * 20];'
teststr2 += '       document.getElementsByName("usleCropland_5" + ("0" + ( i + 1)) .slice(-2))[0].value = str[4 + i * 20];'
teststr2 += '       document.getElementsByName("uslePasture_1" + ("0" + ( i + 1)) .slice(-2))[0].value = str[5 + i * 20];'
teststr2 += '       document.getElementsByName("uslePasture_2" + ("0" + ( i + 1)) .slice(-2))[0].value = str[6 + i * 20];'
teststr2 += '       document.getElementsByName("uslePasture_3" + ("0" + ( i + 1)) .slice(-2))[0].value = str[7 + i * 20];'
teststr2 += '       document.getElementsByName("uslePasture_4" + ("0" + ( i + 1)) .slice(-2))[0].value = str[8 + i * 20];'
teststr2 += '       document.getElementsByName("uslePasture_5" + ("0" + ( i + 1)) .slice(-2))[0].value = str[9 + i * 20];'
teststr2 += '       document.getElementsByName("usleForest_1" + ("0" + ( i + 1)) .slice(-2))[0].value = str[10 + i * 20];'
teststr2 += '       document.getElementsByName("usleForest_2" + ("0" + ( i + 1)) .slice(-2))[0].value = str[11 + i * 20];'
teststr2 += '       document.getElementsByName("usleForest_3" + ("0" + ( i + 1)) .slice(-2))[0].value = str[12 + i * 20];'
teststr2 += '       document.getElementsByName("usleForest_4" + ("0" + ( i + 1)) .slice(-2))[0].value = str[13 + i * 20];'
teststr2 += '       document.getElementsByName("usleForest_5" + ("0" + ( i + 1)) .slice(-2))[0].value = str[14 + i * 20];'

teststr2 += '       document.getElementsByName("usleUser_1" + ("0" + ( i + 1)) .slice(-2))[0].value = str[15 + i * 20];'
teststr2 += '       document.getElementsByName("usleUser_2" + ("0" + ( i + 1)) .slice(-2))[0].value = str[16 + i * 20];'
teststr2 += '       document.getElementsByName("usleUser_3" + ("0" + ( i + 1)) .slice(-2))[0].value = str[17 + i * 20];'
teststr2 += '       document.getElementsByName("usleUser_4" + ("0" + ( i + 1)) .slice(-2))[0].value = str[18 + i * 20];'
teststr2 += '       document.getElementsByName("usleUser_5" + ("0" + ( i + 1)) .slice(-2))[0].value = str[19 + i * 20];'
teststr2 += '     }'
teststr2 += '   }, error:function(xhr) {}});'
#teststr2 += '   var xmlhttp = new XMLHttpRequest();'
#teststr2 += '   xmlhttp.open("GET", "CountyData_2.cgi", true);'
#teststr2 += '   xmlhttp.send();'

#teststr2 += '  document.CountyFrame_2.CountyForm.State.value = state; '
#teststr2 += '  document.CountyFrame_2.CountyForm.County.value = countyName; '
#teststr2 += '  document.CountyFrame_2.CountyForm.submit(); '
#teststr2 += '  document.CountyData_3_Frame.sendPcpInfo(); '
#teststr2 += ' alert(  "State: " +  document.CountyFrame_2.CountyForm.State.value + " County: " + document.CountyFrame_2.CountyForm.County.value  ); '
teststr2 += '} '
teststr2 += ' </script>'

print teststr, #changes 2
print CLIGEN_Str, '</td>'
print '    </tr>'
print '  </table>'
print '<hr><br><br>'

print teststr2,
#print statestr,

#-----------------------------------------------------------------------------------------------------------------------Step2 

print '  <span style="font-weight:bold; color:blue;">Step 2. Input agricultural animals</span> (Optional)'

tetratech_str = '    <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Tetratech Online Database\''
tetratech_str += ' onClick="tetratechLink()">'
print tetratech_str

print '  <table border=1 style="margin: 0 auto; width:1000px;">'
print '    <tr style="text-align:center;">'
print '      <td style="text-align:center; background-color:#BDBDBD">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Beef Cattle</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Dairy Cattle</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Swine (Hog)</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Sheep</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Horse</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Chicken</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Turkey</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Duck</td>'
print '      <td style="text-align:center; background-color:#BDBDBD"># of months<br>manure applied</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '  <tr>'
  tmpStrW = 'W' + str(i)
  print '    <td style="text-align:center;">', tmpStrW, '</td>'
  for j in range(1,9) :
    tmpStr = '<td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" name='
    if rerun == 0:
      tmpStr = tmpStr + 'Animals_' + str(j) + str('%02i'%i) + ' size=5 value=0></td>'
    else:
      tmpStr = tmpStr + 'Animals_' + str(j) + str('%02i'%i) + ' size=5 value='+ table2list[i-1][j-1] +'></td>'
    print tmpStr
  tmpStr = '<td style="text-align:center;"><input type=text style="text-align:right;border-width:0px;font-size:11pt" name='
  if rerun == 0:
    tmpStr = tmpStr + 'NumMonManure_' + str('%02i'%i) + ' size=5 value=0></td>'
  else:
    tmpStr = tmpStr + 'NumMonManure_' + str('%02i'%i) + ' size=5 value='+ table2list[i-1][8] +'></td>'
  print tmpStr
  print '  </tr>'

print '  </table>'

print '<hr><br><br>'

#-----------------------------------------------------------------------------------------------------------------------Step3
print '  <span style="font-weight:bold; color:blue;">Step 3. Input septic system and illegal direct wastewater discharge data</span> (Optional)'

tetratech_str = '    <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Tetratech Online Database\''
tetratech_str += ' onClick="tetratechLink()">'
print tetratech_str

print '  <table border=1 style="margin: 0 auto; width:1000px">'
print '    <tr style="text-align:center">'
print '      <td style="text-align:center; background-color:#BDBDBD">Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">No. of Septic Systems</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Population per Septic System</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Septic Failure Rate, %</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Wastewater Direct Discharge, # of People</td>'
print '      <td style="text-align:center; background-color:#BDBDBD">Direct Discharge Reduction, %</td>'
print '    </tr>'

for i in range(1,numWSD+1) :
  print '    <tr>'
  tmpStrW = 'W' + str(i)
  print '      <td style="text-align:center;">', tmpStrW, '</td>'
  if rerun == 0:
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=NumSpSys_' + str('%02i'%i) + ' size=5 value=0></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=PpSpSys_' + str('%02i'%i) + ' size=5 value=0></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=SpFailRate_' + str('%02i'%i) + ' size=5 value=0></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=NumPpDrtDc_' + str('%02i'%i) + ' size=5 value=0></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=RdcDrtDc_' + str('%02i'%i) + ' size=5 value=0></td>'
    print tmpStr
  else:
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=NumSpSys_' + str('%02i'%i) + ' size=5 value='+ table3list[i-1][0] +'></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=PpSpSys_' + str('%02i'%i) + ' size=5 value='+ table3list[i-1][1] +'></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=SpFailRate_' + str('%02i'%i) + ' size=5 value='+ table3list[i-1][2] +'></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=NumPpDrtDc_' + str('%02i'%i) + ' size=5 value='+ table3list[i-1][3] +'></td>'
    print tmpStr
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:11pt" name=RdcDrtDc_' + str('%02i'%i) + ' size=5 value='+ table3list[i-1][4] +'></td>'
    print tmpStr
  print '    </tr>'
print '  </table>'

print '<hr><br><br>'


#-----------------------------------------------------------------------------------------------------------------------Step4
print '  <span style="font-weight:bold; color:blue;">Step 4. Modify the Universal Soil Loss Equation (USLE) parameters</span>'
tmpStr = '    <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'County Data\''
tmpStr = tmpStr + ' onClick="javascript:window.open(\'./CountyData.cgi?numWSD=' + str(numWSD) + '\','
tmpStr = tmpStr + '\'CountyData\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=400,width=780\');">'
tmpStr += ' <span style=" font-size:0.82em; color:red;"> *The state and county of the CLIGEN station will be the default for soil data properties. </span> <br>'
print tmpStr, ''
print '  <table border=1 style="margin: 0 auto; width:1000px">'
print '    <tr style="text-align:middle">'
print '      <td style="text-align:center; background-color:#BDBDBD; width:50px" rowspan=2>Watershed</td>'
print '      <td style="text-align:center; background-color:#BDBDBD" colspan=5>Cropland</td>'
print '      <td style="text-align:center; background-color:#BDBDBD" colspan=5>Pastureland</td>'
print '      <td style="text-align:center; background-color:#BDBDBD" colspan=5>Forest</td>'


print '      <td style="text-align:center; background-color:#BDBDBD" colspan=5>User Defined</td>'
print '    </tr>'

print '    <tr>'
for i in range(4) :
  print '      <td style="text-align:center; background-color:#BDBDBD">R</td>'
  print '      <td style="text-align:center; background-color:#BDBDBD">K</td>'
  print '      <td style="text-align:center; background-color:#BDBDBD">LS</td>'
  print '      <td style="text-align:center; background-color:#BDBDBD">C</td>'
  print '      <td style="text-align:center; background-color:#BDBDBD">P</td>'
print '    </tr>'

# Read state and county from step 2---------------------------------------------------



# ------------------------------------------------------------------------------------

for i in range(1,numWSD+1) :
  print '    <tr>'
  tmpStrW = 'W' + str(i)
  print '      <td style="text-align:center">', tmpStrW, '</td>'
  for j in range(1,6) :
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:8pt" name='
    tmpStr = tmpStr + 'usleCropland_' + str(j) + str('%02i'%i) +' size=3 value=0.0></td>'
    print tmpStr
  for j in range(1,6) :
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:8pt" name='
    tmpStr = tmpStr + 'uslePasture_' + str(j) + str('%02i'%i) +' size=3 value=0.0></td>'
    print tmpStr
  for j in range(1,6) :
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:8pt" name='
    tmpStr = tmpStr + 'usleForest_' + str(j) + str('%02i'%i) +' size=3 value=0.0></td>'
    print tmpStr
  for j in range(1,6) :
    tmpStr = '      <td align=center><input type=text style="text-align:right;border-width:0px;font-size:8pt" name='
    tmpStr = tmpStr + 'usleUser_' + str(j) + str('%02i'%i) +' size=3 value=0.0></td>'
    print tmpStr

  print '    </tr>'
print '  </table>'



print '<hr><br><br>'

print '  <span style="color:blue; font-style:italic">If you want to change Optional Input Data, click this button . </span>'
#print '    <input type=button style=\'width:200;height:30px;cursor:hand\' value=\'Change Optional Input\''
#print '    onClick="javascript:window.open(\'./optMain.cgi?numWSD=\','
#print '    \'STEPL_DB_online\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1\');">'
tmpStr = '    <input type=button style=\'width:250x;height:30px;cursor:hand;\' value=\'Change soil type and CN inputs\''
tmpStr = tmpStr + ' onClick="updateSHG();javascript:window.open(\'./optMain.cgi?numWSD=' + str(numWSD)
tmpStr = tmpStr + '\',\'STEPL_DB_online\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=400,width=900\');">'
print tmpStr
print '<hr>'

#----DB
print '  <div style="color:blue; font-style:italic">If you want to change DBs, click button. </div>'
print '  '
print '  <table style="margin: 0 auto; border:0">'
print '    <tr>'
print '      <td style="text-align:center">'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Soil Infiltration Fraction for Precipitation\''
print '        onClick="javascript:window.open(\'./gwInfRatio.cgi\','
print '        \'Groundwater_Infiltration_Rate\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=340,width=500\');">'
print '      </td>'
print '      <td style="text-align:center">'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Wildlife density in cropland\''
print '        onClick="javascript:window.open(\'./WildLife.html\','
print '        \'Wildlife_Density\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=300,width=500\');">'
print '      </td>'
print '      <td style="text-align:center">'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Standard Animal Weight Table\''
print '        onClick="javascript:window.open(\'./Reference.html\','
print '        \'Reference\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=550,width=900\');">'
print '      </td>'
print '    </tr>'
print '    <tr>'
print '      <td  style="text-align:center">'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Septic DB Table\''
print '        onClick="javascript:window.open(\'./Septic.html\','
print '        \'Septic_Table\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=320,width=900\');">'
print '      </td>'
print '      <td>'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Feedlot DB Table\''
print '        onClick="javascript:window.open(\'./Feedlot.html\','
print '        \'Feedlot\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=470,width=700\');">'
print '      </td>'
print '      <td>'
print '        <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Gully&amp;Streambank DB Table\''
print '        onClick="javascript:window.open(\'./GullyDB.html\','
print '        \'Gully\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,scrolling=1,height=640,width=710\');">'
print '      </td>'
print '    </tr>'
print '  </table>'
print '  <hr>'

print '  <span style="color:blue; font-style:italic">If you want to input Gully and Streambank Erosion, click the button.</span>'
glyBtn = '  <input type=button style=\'width:240px;height:30px;cursor:hand\' value=\'Gully &amp; Streambank Erosion\''
glyBtn += ' onClick="javascript:window.open(\'./GS1.cgi?numWSD=' 
glyBtn += str(numWSD) + '&amp;numSTR=' + str(numSTR) + '&amp;numGLY=' + str(numGLY) + '\','
glyBtn += '\'Gully_Streambank\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,'
glyBtn += 'scrolling=1,height=600,width=900\');"><hr>'
print glyBtn

#print '  <font color=blue><i>If you want to update Reference Soil Infiltration Fraction for Precipitation, '
#print '  click the button.</i></font>'
#gwBtn = '  <input type=button style=\'width:240px;height:30px;cursor:hand\' '
#gwBtn += 'value=\'Soil Infiltration Fraction for Precipitation\' onClick="javascript:window.open(\'./GW1.cgi\','
#gwBtn += '\'GW_db\',\'status=0,toolbar=1,location=0,menubar=0,scrollbars=1,'
#gwBtn += 'scrolling=1,height=340,width=500\');"><hr>'
#print gwBtn


#print '<br><br><div style="text-align:center"><input style="WIDTH:200px;height:30px;CURSOR:hand" type=submit value="Next"></div><br><br>'
print '<br><br><div style="text-align:center">'
print '<input style="WIDTH:200px;height:30px;CURSOR:hand" type=button onClick="reloadPage()" value="Clear the fields">'
print '<input style="WIDTH:200px;height:30px;CURSOR:hand" type=button onClick="complete()" value="Next"></div><br><br>'
#-----------------------------------------------------------------------------------------------------------------------hidden
tmpStr = '<input type=hidden name=ystime value="' + str(ystime) + '">'
print tmpStr
tmpStr = '<input type=hidden name=numWSD value="' + str(numWSD) + '">'
print tmpStr
tmpStr = '<input type=hidden name=numGLY value="' + str(numGLY) + '">'
print tmpStr
tmpStr = '<input type=hidden name=rerun value="' + form.getvalue('rerun') + '">'
print tmpStr
tmpStr = '<input type=hidden name=numSTR value="' + str(numSTR) + '">'
print tmpStr
tmpStr = '<input type=hidden name=simLog value="' + str(form.getvalue('simLog')) + '">'
print tmpStr
print '<input type=hidden name=status value="0">'

#----Step5
for i in range(1,numWSD+1) :											# Step5
  tmpStr = '<input type=hidden name=SoilN_' + str('%02i'%i) + ' value=0.080>' 
  tmpStr = tmpStr + '<input type=hidden name=SoilP_' + str('%02i'%i) + ' value=0.031><input type=hidden name=SoilB_' + str('%02i'%i) + ' value=0.160>'
  print tmpStr

#----Step6
print '<input type=hidden name=CN_urban_A value=83><input type=hidden name=CN_urban_B value=89>'
print '<input type=hidden name=CN_urban_C value=92><input type=hidden name=CN_urban_D value=93>'
print '<input type=hidden name=CN_crop_A value=67><input type=hidden name=CN_crop_B value=78>'
print '<input type=hidden name=CN_crop_C value=85><input type=hidden name=CN_crop_D value=89>'
print '<input type=hidden name=CN_past_A value=49><input type=hidden name=CN_past_B value=69>'
print '<input type=hidden name=CN_past_C value=79><input type=hidden name=CN_past_D value=84>'
print '<input type=hidden name=CN_frst_A value=39><input type=hidden name=CN_frst_B value=60>'
print '<input type=hidden name=CN_frst_C value=73><input type=hidden name=CN_frst_D value=79>'
print '<input type=hidden name=CN_wetl_A value=77><input type=hidden name=CN_wetl_B value=77>'
print '<input type=hidden name=CN_wetl_C value=84><input type=hidden name=CN_wetl_D value=90>'
print '<input type=hidden name=CN_user_A value=50><input type=hidden name=CN_user_B value=70>'
print '<input type=hidden name=CN_user_C value=80><input type=hidden name=CN_user_D value=85>'

#----Step6a
print '<input type=hidden name=CN_comm_A value=89><input type=hidden name=CN_comm_B value=92>'
print '<input type=hidden name=CN_comm_C value=94><input type=hidden name=CN_comm_D value=95>'
print '<input type=hidden name=CN_indu_A value=81><input type=hidden name=CN_indu_B value=88>'
print '<input type=hidden name=CN_indu_C value=91><input type=hidden name=CN_indu_D value=93>'
print '<input type=hidden name=CN_inst_A value=81><input type=hidden name=CN_inst_B value=88>'
print '<input type=hidden name=CN_inst_C value=91><input type=hidden name=CN_inst_D value=93>'
print '<input type=hidden name=CN_tran_A value=98><input type=hidden name=CN_tran_B value=98>'
print '<input type=hidden name=CN_tran_C value=98><input type=hidden name=CN_tran_D value=98>'
print '<input type=hidden name=CN_mult_A value=77><input type=hidden name=CN_mult_B value=85>'
print '<input type=hidden name=CN_mult_C value=90><input type=hidden name=CN_mult_D value=92>'
print '<input type=hidden name=CN_sing_A value=57><input type=hidden name=CN_sing_B value=72>'
print '<input type=hidden name=CN_sing_C value=81><input type=hidden name=CN_sing_D value=86>'
print '<input type=hidden name=CN_urcu_A value=67><input type=hidden name=CN_urcu_B value=78>'
print '<input type=hidden name=CN_urcu_C value=85><input type=hidden name=CN_urcu_D value=89>'
print '<input type=hidden name=CN_vade_A value=77><input type=hidden name=CN_vade_B value=85>'
print '<input type=hidden name=CN_vade_C value=90><input type=hidden name=CN_vade_D value=92>'
print '<input type=hidden name=CN_open_A value=49><input type=hidden name=CN_open_B value=69>'
print '<input type=hidden name=CN_open_C value=79><input type=hidden name=CN_open_D value=84>'

#----Step7
print '<input type=hidden name=ntLcrop_1_N value=1.9><input type=hidden name=ntLcrop_1_P value=0.3><input type=hidden name=ntLcrop_1_B value=4.0>'
print '<input type=hidden name=ntLcrop_2_N value=8.1><input type=hidden name=ntLcrop_2_P value=2.0><input type=hidden name=ntLcrop_2_B value=12.3>'
print '<input type=hidden name=ntMcrop_1_N value=2.9><input type=hidden name=ntMcrop_1_P value=0.4><input type=hidden name=ntMcrop_1_B value=6.1>'
print '<input type=hidden name=ntMcrop_2_N value=12.2><input type=hidden name=ntMcrop_2_P value=3.0><input type=hidden name=ntMcrop_2_B value=18.5>'
print '<input type=hidden name=ntHcrop_1_N value=4.4><input type=hidden name=ntHcrop_1_P value=0.5><input type=hidden name=ntHcrop_1_B value=9.2>'
print '<input type=hidden name=ntHcrop_2_N value=18.3><input type=hidden name=ntHcrop_2_P value=4.0><input type=hidden name=ntHcrop_2_B value=24.6>'
print '<input type=hidden name=ntPast_N value=4.0><input type=hidden name=ntPast_P value=0.3><input type=hidden name=ntPast_B value=13.0>'
print '<input type=hidden name=ntFrst_N value=0.2><input type=hidden name=ntFrst_P value=0.1><input type=hidden name=ntFrst_B value=0.5>'

print '<input type=hidden name=ntWetl_N value=0.0><input type=hidden name=ntWetl_P value=0.0><input type=hidden name=ntWetl_B value=0.0>'
print '<input type=hidden name=ntUser_N value=0.0><input type=hidden name=ntUser_P value=0.0><input type=hidden name=ntUser_B value=0.0>'

#----Step7a
print '<input type=hidden name=GntUrbn_N value=1.5><input type=hidden name=GntUrbn_P value=0.063><input type=hidden name=GntUrbn_B value=0.0>'
print '<input type=hidden name=GntCrop_N value=1.44><input type=hidden name=GntCrop_P value=0.063><input type=hidden name=GntCrop_B value=0.0>'
print '<input type=hidden name=GntPast_N value=1.44><input type=hidden name=GntPast_P value=0.063><input type=hidden name=GntPast_B value=0.0>'
print '<input type=hidden name=GntFrst_N value=0.11><input type=hidden name=GntFrst_P value=0.009><input type=hidden name=GntFrst_B value=0.0>'
print '<input type=hidden name=GntWetl_N value=0.0><input type=hidden name=GntWetl_P value=0.0><input type=hidden name=GntWetl_B value=0.0>'
print '<input type=hidden name=GntFeed_N value=6.0><input type=hidden name=GntFeed_P value=0.007><input type=hidden name=GntFeed_B value=0.0>'
print '<input type=hidden name=GntUser_N value=0.0><input type=hidden name=GntUser_P value=0.0><input type=hidden name=GntUser_B value=0.0>'

#----Step8
for i in range(1,numWSD+1) :
  tmpStr = '<input type=hidden name=dist_1' + str('%02i'%i) + ' value=15>'
  tmpStr = tmpStr + '<input type=hidden name=dist_2' + str('%02i'%i) + ' value=10>' 
  tmpStr = tmpStr + '<input type=hidden name=dist_3' + str('%02i'%i) + ' value=10>'
  tmpStr = tmpStr + '<input type=hidden name=dist_4' + str('%02i'%i) + ' value=10>'
  tmpStr = tmpStr + '<input type=hidden name=dist_5' + str('%02i'%i) + ' value=10>'
  tmpStr = tmpStr + '<input type=hidden name=dist_6' + str('%02i'%i) + ' value=30>'
  tmpStr = tmpStr + '<input type=hidden name=dist_7' + str('%02i'%i) + ' value=5>'
  tmpStr = tmpStr + '<input type=hidden name=dist_8' + str('%02i'%i) + ' value=5>'
  tmpStr = tmpStr + '<input type=hidden name=dist_9' + str('%02i'%i) + ' value=5>'
  print tmpStr

#----Step9
for i in range(1,numWSD+1) :
  for j in range(1,5) :
    tmpStr = '<input type=hidden name=IrrVal_' + str(j) + str('%02i'%i) + ' value=0>'
    print tmpStr

#----GullyDB
print '<input type=hidden name=GullyDB_011 value=0.0350><input type=hidden name=GullyDB_012 value=1.15>'
print '<input type=hidden name=GullyDB_021 value=0.0375><input type=hidden name=GullyDB_022 value=1.15>'
print '<input type=hidden name=GullyDB_031 value=0.0500><input type=hidden name=GullyDB_032 value=0.85>'
print '<input type=hidden name=GullyDB_041 value=0.0450><input type=hidden name=GullyDB_042 value=0.85>'
print '<input type=hidden name=GullyDB_051 value=0.0110><input type=hidden name=GullyDB_052 value=1.50>'
print '<input type=hidden name=GullyDB_061 value=0.0550><input type=hidden name=GullyDB_062 value=0.85>'
print '<input type=hidden name=GullyDB_071 value=0.0450><input type=hidden name=GullyDB_072 value=0.85>'
print '<input type=hidden name=GullyDB_081 value=0.0525><input type=hidden name=GullyDB_082 value=0.85>'
print '<input type=hidden name=GullyDB_091 value=0.0425><input type=hidden name=GullyDB_092 value=1.00>'
print '<input type=hidden name=GullyDB_101 value=0.0400><input type=hidden name=GullyDB_102 value=1.00>'
print '<input type=hidden name=GullyDB_111 value=0.03><input type=hidden name=GullyDB_121 value=0.13>'
print '<input type=hidden name=GullyDB_131 value=0.40><input type=hidden name=GullyDB_141 value=0.50>'

#----Septic
print '<input type=hidden name=Septic_11 value=60><input type=hidden name=Septic_12 value=40>'
print '<input type=hidden name=Septic_21 value=23.5><input type=hidden name=Septic_22 value=8>'
print '<input type=hidden name=Septic_31 value=245><input type=hidden name=Septic_32 value=220>'
print '<input type=hidden name=Septic_41 value=70><input type=hidden name=Septic_42 value=75>'

#----WildLife
print '<input type=hidden name=WildLife_1 value=0><input type=hidden name=WildLife_2 value=0>'
print '<input type=hidden name=WildLife_3 value=0><input type=hidden name=WildLife_4 value=0>'
print '<input type=hidden name=WildLife_5 value=0>'

#----Feedlot
print '<input type=hidden name=Feedlot_011 value=1><input type=hidden name=Feedlot_012 value=1>'
print '<input type=hidden name=Feedlot_013 value=1><input type=hidden name=Feedlot_014 value=1>'
print '<input type=hidden name=Feedlot_021 value=0.5><input type=hidden name=Feedlot_022 value=0.51>'
print '<input type=hidden name=Feedlot_023 value=0.5><input type=hidden name=Feedlot_024 value=0.5>'
print '<input type=hidden name=Feedlot_031 value=1.853><input type=hidden name=Feedlot_032 value=0.92>'
print '<input type=hidden name=Feedlot_033 value=1.4><input type=hidden name=Feedlot_034 value=1.96>'
print '<input type=hidden name=Feedlot_041 value=0.662><input type=hidden name=Feedlot_042 value=0.33>'
print '<input type=hidden name=Feedlot_043 value=0.5><input type=hidden name=Feedlot_044 value=0.7>'
print '<input type=hidden name=Feedlot_051 value=0.306><input type=hidden name=Feedlot_052 value=0.27>'
print '<input type=hidden name=Feedlot_053 value=0.388><input type=hidden name=Feedlot_054 value=0.17>'
print '<input type=hidden name=Feedlot_061 value=0.076><input type=hidden name=Feedlot_062 value=0.07>'
print '<input type=hidden name=Feedlot_063 value=0.097><input type=hidden name=Feedlot_064 value=0.04>'
print '<input type=hidden name=Feedlot_071 value=0.124><input type=hidden name=Feedlot_072 value=0.06>'
print '<input type=hidden name=Feedlot_073 value=0.075><input type=hidden name=Feedlot_074 value=0.18>'
print '<input type=hidden name=Feedlot_081 value=0.882><input type=hidden name=Feedlot_082 value=0.42>'
print '<input type=hidden name=Feedlot_083 value=1.063><input type=hidden name=Feedlot_084 value=0.42>'
print '<input type=hidden name=Feedlot_091 value=0.01><input type=hidden name=Feedlot_092 value=0.01>'
print '<input type=hidden name=Feedlot_093 value=0.008><input type=hidden name=Feedlot_094 value=0.01>'
print '<input type=hidden name=Feedlot_101 value=0.018><input type=hidden name=Feedlot_102 value=0.03>'
print '<input type=hidden name=Feedlot_103 value=0.013><input type=hidden name=Feedlot_104 value=0.02>'
print '<input type=hidden name=Feedlot_111 value=0.018><input type=hidden name=Feedlot_112 value=0.01>'
print '<input type=hidden name=Feedlot_113 value=0.011><input type=hidden name=Feedlot_114 value=0.01>'

#--gwInfoRatio
print '<input type=hidden name=gwInft_11 value=0.36><input type=hidden name=gwInft_12 value=0.24>'
print '<input type=hidden name=gwInft_13 value=0.12><input type=hidden name=gwInft_14 value=0.06>'
print '<input type=hidden name=gwInft_21 value=0.45><input type=hidden name=gwInft_22 value=0.30>'
print '<input type=hidden name=gwInft_23 value=0.15><input type=hidden name=gwInft_24 value=0.075>'
print '<input type=hidden name=gwInft_31 value=0.45><input type=hidden name=gwInft_32 value=0.30>'
print '<input type=hidden name=gwInft_33 value=0.15><input type=hidden name=gwInft_34 value=0.075>'
print '<input type=hidden name=gwInft_41 value=0.45><input type=hidden name=gwInft_42 value=0.30>'
print '<input type=hidden name=gwInft_43 value=0.15><input type=hidden name=gwInft_44 value=0.075>'
print '<input type=hidden name=gwInft_51 value=0.45><input type=hidden name=gwInft_52 value=0.30>'
print '<input type=hidden name=gwInft_53 value=0.15><input type=hidden name=gwInft_54 value=0.075>'

#--Reference
print '<input type=hidden name=Reference_011 value=1000><input type=hidden name=Reference_012 value=1.6>'
print '<input type=hidden name=Reference_013 value=1.28><input type=hidden name=Reference_014 value=467.1>'
print '<input type=hidden name=Reference_021 value=1400><input type=hidden name=Reference_022 value=1.6>'
print '<input type=hidden name=Reference_023 value=2.24><input type=hidden name=Reference_024 value=818>'
print '<input type=hidden name=Reference_031 value=200><input type=hidden name=Reference_032 value=3.1>'
print '<input type=hidden name=Reference_033 value=0.42><input type=hidden name=Reference_034 value=153>'
print '<input type=hidden name=Reference_041 value=100><input type=hidden name=Reference_042 value=1.2>'
print '<input type=hidden name=Reference_043 value=0.07><input type=hidden name=Reference_044 value=26>'
print '<input type=hidden name=Reference_051 value=1000><input type=hidden name=Reference_052 value=1.7>'
print '<input type=hidden name=Reference_053 value=1.7><input type=hidden name=Reference_054 value=621>'
print '<input type=hidden name=Reference_061 value=4><input type=hidden name=Reference_062 value=3.3>'
print '<input type=hidden name=Reference_063 value=0.01><input type=hidden name=Reference_064 value=5>'
print '<input type=hidden name=Reference_071 value=10><input type=hidden name=Reference_072 value=2.1>'
print '<input type=hidden name=Reference_073 value=0.03><input type=hidden name=Reference_074 value=11>'
print '<input type=hidden name=Reference_081 value=4><input type=hidden name=Reference_082 value=0>'
print '<input type=hidden name=Reference_083 value=0><input type=hidden name=Reference_084 value=0>'
print '<input type=hidden name=Reference_091 value=6><input type=hidden name=Reference_092 value=0>'
print '<input type=hidden name=Reference_093 value=0><input type=hidden name=Reference_094 value=0>'
print '<input type=hidden name=Reference_101 value=40><input type=hidden name=Reference_102 value=0>'
print '<input type=hidden name=Reference_103 value=0><input type=hidden name=Reference_104 value=0>'
print '<input type=hidden name=Reference_111 value=15><input type=hidden name=Reference_112 value=0>'
print '<input type=hidden name=Reference_113 value=0><input type=hidden name=Reference_114 value=0>'
print '<input type=hidden name=Reference_121 value=7><input type=hidden name=Reference_122 value=0>'
print '<input type=hidden name=Reference_123 value=0><input type=hidden name=Reference_124 value=0>'
print '<input type=hidden name=Reference_131 value=0><input type=hidden name=Reference_132 value=0>'
print '<input type=hidden name=Reference_133 value=0><input type=hidden name=Reference_134 value=0>'

#--Gully & Streambank
for i in range(1,numGLY+1) :
  for j in range(1,10) : 				# 9 values for gully
    tmpStr = '<input type=hidden name=GS1_' + str('%02i'%i) + str(j) + ' value=0 size=2>'
    print tmpStr
for i in range(1,numSTR+1) :
  for j in range(1,8) : 				# 7 values for streambank
    tmpStr = '<input type=hidden name=GS2_' + str('%02i'%i) + str(j) + ' value=0 size=2>'
    print tmpStr

print '</form>'

print '<form name=cleanForm method="POST" action="./inputMain.cgi" target="_self">'
print '<input type=hidden name=numWSD  value=' + str(numWSD) + '>'
print '<input type=hidden name=numGLY  value=0>'
print '<input type=hidden name=numSTR  value=0>'
print '<input type=hidden name=rerun value=0>'
print '<input type=hidden name=ystimeldc value="noldc">'
print '</form>'

print '<form name=graphForm method="POST" action="./simpleGraph.cgi">'
print '<input type=hidden name=ystime value="' + str(ystime) + '">'
print '</form>'

print '<hr>'
print '<div style="text-align:center; font-size:0.82em;">'
print '  <div style="color:gray">'
print '    Copyright &copy; 2015, Purdue University and Kangwon National University, all rights reserved. <br>'
print '    Purdue University is an equal access/equal opportunity university.<br>'
print '  </div>'
print '  Contact <a href=mailto:engelb@purdue.edu>Dr. Bernie Engel</a>'
print '  or <a href=mailto:theller@purdue.edu>Larry Theller</a> for more details if you need any help with STEPL WEB. '
print '  <br>'
print '  This implementation of the classic EPA model was designed by Dr. <a href=mailto:ysparkwithyou@gmail.com>Youn Shik Park</a>, Assistant Professor, Kongju National University, South-Korea.'
print '  <br>Programmatic support from US EPA, Illinois-Indiana Sea Grant,  and US Army Corp of Engineers.'
print '</div><br>'
print ''

print '</body>'
print '</html>'



