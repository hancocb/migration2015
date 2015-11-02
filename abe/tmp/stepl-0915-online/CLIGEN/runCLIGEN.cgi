#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"button2.css\">\n" ;
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
myFile = str(form.getvalue('FileName'))
ystime = str(form.getvalue('ystime'))
stateN = str(form.getvalue('stateN'))
countyN = str(form.getvalue('countyN'))
stationN = str(form.getvalue('stationN'))
#----E input----------------------------------------------------------------------------------------------------
print '<html>'
print '<head><title>Web-based LDC Tool</title></head>'
print '<body><br><br><br><br><hr>'
#------------------S Copy Required Files and Run----------------------------------------------------------------
print '<li> Preparing CLIGEN running..'
myFile = myFile.replace(' ','')
dirName = myFile[:2].lower()

path = '../tmp/' + str(ystime) + '/'
mkdirPath = 'mkdir ' + path  + 'cligen'
os.system(mkdirPath)
path = path + 'cligen/'
cpCLIGEN = 'cp ./cligen_exe ' + path + '/.'
os.system(cpCLIGEN)
myFilePath = 'cp ./parFiles/' + dirName + '/' + myFile + ' ' + path + 'rawPcp.txt'
os.system(myFilePath)
chmod777 = 'chmod 777 ' + path + '/*'
os.system(chmod777)

os.chdir(path)
#print '<li>', os.getcwd()
print '<li> CLIGEN running..'
os.system('./cligen_exe -b1 -y100 -irawPcp.txt -orawOut.txt -F >> tmp.txt')
#------------------E Copy Required Files and Run----------------------------------------------------------------
#---------------------------------------------------S Read CLIGEN Output and Write pcp.txt----------------------
print '<li> Writing Precipitation File..'
rawDataPath = open('./rawOut.txt','r')
rawData = rawDataPath.readlines()
rawDataPath.close()

sttLine = 0 
myData = []
for i in range(len(rawData)) :
  rawData[i] = rawData[i].split()
  if ( 5 < len(rawData[i]) and str(rawData[i][0]) == '1' and str(rawData[i][1]) == '1' and str(rawData[i][2]) == '1' and sttLine < 1 ) : 
    sttLine = i
  if ( sttLine != 0 and 5 < len(rawData[i]) ) :
    tmpStr = str('%04i'%int(rawData[i][2])) + str('%02i'%int(rawData[i][1])) + str('%02i'%int(rawData[i][0])) + '\t' + str(rawData[i][3])
    myData.append(tmpStr)

pcp = open('./pcp.txt','w')
for i in range(len(myData)) :
  pcp.write(str(myData[i]) + '\n')
pcp.close()

chmod777 = 'chmod 777 ./*.txt'
os.system(chmod777)
#---------------------------------------------------E Read CLIGEN Output and Write pcp.txt----------------------
#-----------------------------------------------S Read CLIGEN Output and Write stainfo.txt----------------------
stainfo = open('./stainfo.txt', 'w')
stainfo.write("Station:\t" + str(stationN) + '\n' )
stainfo.write("State:\t" + str(stateN) + '\n')
stainfo.write("County:\t" + str(countyN) )
stainfo.close()

chmod777 = 'chmod 777 ./*.txt'
os.system(chmod777)
#-----------------------------------------------E Read CLIGEN Output and Write stainfo.txt----------------------

print '</body>'
print '<script language="JavaScript">'
print '  self.close();'
print '</script>'
print '</html>'
