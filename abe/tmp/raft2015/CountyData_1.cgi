#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------

import cgi, cgitb, os, string, random
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
State = str(form.getvalue('State'))
County = str(form.getvalue('County'))
if ( State == '' or State == 'None' ) :
  State = ''
else :
  State = State.replace(' ','')
if ( County == '' or County == 'None' ) :
  County = ''
#----E input----------------------------------------------------------------------------------------------------
Rval = [0.0] * 2
USLE = [0.0] * 5
#-----------------------------S Read myCountyData_DB.txt--------------------------------------------------------
myDBFile = open('./myCountyData_DB.txt','r')
myDB = myDBFile.readlines()
myDBFile.close()

CtNameOti = []
CtNameNS = []
for i in range(len(myDB)) :
  myDB[i] = myDB[i].replace('\n','')
  myDB[i] = myDB[i].split('\t')
  tmpStr_1 = str(myDB[i][0].replace(' ','')) 
  if ( State == tmpStr_1 ) :
    tmpStr_2 = str(myDB[i][1].replace(' ',''))
    CtNameNS.append(str(tmpStr_2))
    CtNameOti.append(str(myDB[i][1]))

if ( State != '' and County != '' ) :
  for i in range(len(myDB)) :
    tmpStr_1 = str(myDB[i][0].replace(' ',''))
    tmpStr_2 = str(myDB[i][1].replace(' ',''))
    #print '<li>', State, '::', County
    if ( State == tmpStr_1 and County == tmpStr_2 ) :
      Rval[0] = myDB[i][3]
      Rval[1] = myDB[i][4]
      USLE[0] = myDB[i][9]
      USLE[1] = myDB[i][10]
      USLE[2] = myDB[i][11]
      USLE[3] = myDB[i][12]
      USLE[4] = myDB[i][13]

#-----------------------------E Read myCountyData_DB.txt--------------------------------------------------------

#---------------S HTML------------------------------------------------------------------------------------------
print '<body onLoad="init();">'
print '<form name=CountyForm action=CountyData_1.cgi method=POST>'
print '  <input type=hidden size=10 name=State value=', State, '>'
print '  <input type=hidden name=Rval_1 value=', Rval[0], '>'
print '  <input type=hidden name=Rval_2 value=', Rval[1], '>'
print '  <input type=hidden name=USLE_1 value=', USLE[0], '>'
print '  <input type=hidden name=USLE_2 value=', USLE[1], '>'
print '  <input type=hidden name=USLE_3 value=', USLE[2], '>'
print '  <input type=hidden name=USLE_4 value=', USLE[3], '>'
print '  <input type=hidden name=USLE_5 value=', USLE[4], '>'
print '  <select name=County onChange="javascript:CtSelected();">'
print '    <option value=None>Select'
if ( 0 < len(CtNameNS) ) :
  for i in range(len(CtNameNS)) :
    if ( County == CtNameNS[i] ) :
      tmpStr = '<option value="' + str(CtNameNS[i]) + '" selected>' + str(CtNameOti[i])
      print tmpStr
    else :
      tmpStr = '<option value="' + str(CtNameNS[i]) + '">' + str(CtNameOti[i])
      print tmpStr
else :
  print '  <option value=None>-----------'
print '  </select>'



print '</form>'
print '</body>'
print '<script language="JavaScript">'
print 'function init() {'
print '  top.document.CountyData_3_Frame.CountyData_3.usleR.value = document.CountyForm.USLE_1.value ;'
print '  top.document.CountyData_3_Frame.CountyData_3.usleK.value = document.CountyForm.USLE_2.value ;'
print '  top.document.CountyData_3_Frame.CountyData_3.usleLS.value = document.CountyForm.USLE_3.value ;'
print '  top.document.CountyData_3_Frame.CountyData_3.usleC.value = document.CountyForm.USLE_4.value ;'
print '  top.document.CountyData_3_Frame.CountyData_3.usleP.value = document.CountyForm.USLE_5.value ;'
print '}'
print 'function CtSelected() {'
print '  document.CountyForm.submit() ;'
print '}'
print '</script>'
#---------------E HTML------------------------------------------------------------------------------------------


