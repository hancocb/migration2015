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
Stn = str(form.getvalue('Stn'))
if ( Stn == '' or Stn == 'None' ) :
  Stn = '0 Default'
else : 
  Stn = Stn.replace(' ','')
#----E input----------------------------------------------------------------------------------------------------
Rval = [0.0] * 2
Rval[0] = 0.814
Rval[1] = 0.424
#-----------------------------S Read myCountyData_DB.txt--------------------------------------------------------
myDBFile = open('./myCountyData_DB.txt','r')
myDB = myDBFile.readlines()
myDBFile.close()

StnNameOri = []
StnNameNS = []
for i in range(len(myDB)) :
  myDB[i] = myDB[i].replace('\n','')
  myDB[i] = myDB[i].split('\t')
  tmpStr = str(myDB[i][6].replace(' ',''))
  StnNameNS.append(tmpStr)
  StnNameOri.append(myDB[i][6])

for i in range(len(myDB)) :
  if ( Stn == StnNameNS[i] ) :
    Rval[0] = myDB[i][7]
    Rval[1] = myDB[i][8]

#-----------------------------E Read myCountyData_DB.txt--------------------------------------------------------

#---------------S HTML------------------------------------------------------------------------------------------
print '<body onLoad="init();">'
print '<form name=StnForm action="./CountyData_2.cgi" method=POST>'
print '  <input type=hidden size=6 name=Rval_1 value=', Rval[0], '>'
print '  <input type=hidden size=6 name=Rval_2 value=', Rval[1], '>'
print '  <select name=Stn onChange="javascript:StnSelected();">'
for i in range(1,len(StnNameNS)) :
  if ( Stn == StnNameNS[i] ) :
    tmpStr = '<option value=' + str(StnNameNS[i]) + ' selected>' + str(StnNameOri[i])
  else :
    tmpStr = '<option value=' + str(StnNameNS[i]) + '>' + str(StnNameOri[i])
  if ( StnNameNS[i] != '' ) :
    print tmpStr
print '  </select>'

print '</form>'
print '</body>'
print '<script language="JavaScript">'
print 'function init() {'
print '  top.document.CountyData_3_Frame.CountyData_3.AnnualRF.value = document.StnForm.Rval_1.value ;'
print '  top.document.CountyData_3_Frame.CountyData_3.RDaysF.value = document.StnForm.Rval_2.value ;'
print '}'
print 'function StnSelected() {'
print '  document.StnForm.submit() ;' 
print '}'
print '</script>'
#---------------E HTML------------------------------------------------------------------------------------------


