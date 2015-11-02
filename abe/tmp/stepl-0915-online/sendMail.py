#!/usr/local/bin/python
#------------------------------------------------------
# programmed by Youn Shik Park, caronys@nate.com

import cgi, cgitb, os, string, random, datetime
import time, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

time.sleep(10)	 						# 10 sec. sleep before start

#----S Wait GA run--------------------------------------------------------------------------------
LoopNum = 0

GAstatus = glob.glob('./status*.pys')

while ( LoopNum < 40 and len(GAstatus) < 10 ) :			# maximum waiting time: 40 min 
  GAstatus = glob.glob('./status*.pys')
  LoopNum = LoopNum + 1
  time.sleep(60)						# sleep 60 sec.

#----E Wait GA run--------------------------------------------------------------------------------
#-------------------------S send mail-------------------------------------------------------------
infoFile = open('./mailinfo.pys','r')
info = infoFile.readlines()
infoFile.close()

for i in range(len(info)) :
  info[i] = info[i].replace('\n','')
ystime = str(info[0])						# scenario name
mailAdd = str(info[1])						# user's e-mail address

mailc = open('./mailTxt.pys','w')
mailc.write('Dear User\n')
mailc.write('STEPL WEB Auto-Calibration has been finished.\n')
mailc.write('Your secnario name is ' + str(ystime) + '.\n')
mailc.write('Now, you can see the results via following page.\n')
tmpStr = 'https://engineering.purdue.edu/mapserve/ldc/STEPL/cal_4.cgi?ystime=' + str(ystime) 
mailc.write(tmpStr)
mailc.write('\n\n')
mailc.write('Do NOT reply.\n')
mailc.close()

mailcm = 'mailx -s "STEPL_WEB_AutoCalibration" ' + str(mailAdd) + ' < ./mailTxt.pys'
os.system(mailcm)

cpParFile = 'cp ./myOptParFinal.pys ../myOptPar.pys'
os.system(cpParFile)
#-------------------------E send mail-------------------------------------------------------------
#---------------------------------------------S record E-mail address-----------------------------
usrInfoFile = open('../../../usersInfo.pys','r')
usrInfo = usrInfoFile.readlines()
usrInfoFile.close()

usrInfo.append(str(mailAdd) + '\t' + str(ystime) + '\n')
usrInfo.sort()

usrInfoFile = open('../../../usersInfo.pys','w')
for i in range(len(usrInfo)) :
  usrInfoFile.write(usrInfo[i])
usrInfoFile.close()
#---------------------------------------------E record E-mail address-----------------------------





























