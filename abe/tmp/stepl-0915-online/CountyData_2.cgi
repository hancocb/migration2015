#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
#----------------------------------------------

import cgi, cgitb, os, string, random
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
State = str(form.getvalue('State'))
County = str(form.getvalue('County'))
numWSD = int(form.getvalue('numWSD'))
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

temp = 0
try:
  temp = round(float(USLE[3]) * 100) / 100
  if (temp < 0.2):
    temp = 0.2
except:
  temp = 0

total = Rval[0] + Rval[1] + USLE[0] + USLE[1] + USLE[2] + USLE[3] + USLE[4]

for i in range(1,numWSD+1) :
  if (State != '' and County != '' and total != 0) :
    print str(USLE[0]).rstrip('\r\n'), 
    print str(USLE[1]).rstrip('\r\n'),
    print str(USLE[2]).rstrip('\r\n'),
    print temp,
    print str(USLE[4]).rstrip('\r\n'),
    print str(USLE[0]).rstrip('\r\n'),
    print str(USLE[1]).rstrip('\r\n'),
    print str(USLE[2]).rstrip('\r\n'),
    print 0.04,
    print str(USLE[4]).rstrip('\r\n'),
    print str(USLE[0]).rstrip('\r\n'),
    print str(USLE[1]).rstrip('\r\n'),
    print str(USLE[2]).rstrip('\r\n'),
    print 0.003,
    print str(USLE[4]).rstrip('\r\n'),
    print str(USLE[0]).rstrip('\r\n'),
    print str(USLE[1]).rstrip('\r\n'),
    print str(USLE[2]).rstrip('\r\n'),
    print str(USLE[3]).rstrip('\r\n'),
    print str(USLE[4]).rstrip('\r\n'),
  elif (State != "" and County != '' and total == 0) :
    print 0,
    print 0,
    print 0,
    print temp,
    print 0,
    print 0,
    print 0,
    print 0,
    print 0.04,
    print 0,
    print 0,
    print 0,
    print 0,
    print 0.003,
    print 0,
    print 0,
    print 0,
    print 0,
    print 0,
