#!/usr/local/bin/python
#------------------------------------------------------
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>"
#----------------------------------------------
#### Programmed by Youn Shik Park

import cgi, cgitb, os, string, random, datetime, glob
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#----S input----------------------------------------------------------------------------------------------------
ystime = str(form.getvalue('ystime'))
path = './tmp/' + ystime + '/cligen/' 

#----E input----------------------------------------------------------------------------------------------------

#----S WQ Distribution Plot-------------------------------------------------------------------------------------
CombinedData = open(path + 'pcp.txt','r')
dstData = CombinedData.readlines()
CombinedData.close()

wqUnitStr = 'mg/l'

dstDataFile = open(path + 'wqDstPlot.dat','w')
for i in range(len(dstData)) :
  dstDataFile.write(str(dstData[i]))
dstDataFile.close()
tmpVal = dstData[0].split('\t')
dstXrng_1 =tmpVal[0]
tmpVal = dstData[-1].split('\t')
dstXrng_2 = tmpVal[0]


dst = open(path + 'wqDstPlot.script','w')
dst.write('set key top left\n')
dst.write('show key\n')
dst.write('set grid\n')
dst.write('set terminal jpeg\n')
dst.write('set autoscale y\n') 
dst.write('set timefmt "%Y%m%d"\n') 
dst.write('set xdata time\n') 
tmpStr = 'set xrange ["'+ str(dstXrng_1) + '":"' + str(dstXrng_2) + '"]\n'
dst.write(tmpStr)
dst.write('set format x " "\n')
tmpStr = 'set output "' + path + 'wqDstPlot.jpg"\n'
dst.write(tmpStr)
dst.write('set xlabel "Time"\n')
dst.write('set ylabel "Rainfall(mm) "\n')
#tmpStr = 'set y2label "' + 'Rainfall' + '(' + str(wqUnitStr) + ')"\n'
#dst.write(tmpStr)
dst.write('set autoscale y \n')
#dst.write('set autoscale y2 \n')
#dst.write('set y2tics\n')
tmpStr = 'plot "' + path + 'wqDstPlot.dat" using 1:2 with lines lt 3 title \' Rainfall(mm) \' '
#tmpStr = tmpStr + '"' + path + 'wqDstPlot.dat" using 1:4 with points\n'
dst.write(tmpStr)

dst.close()

tmpStr = 'gnuplot ' + path + 'wqDstPlot.script'
os.system(tmpStr)

#----E WQ Distribution Plot-------------------------------------------------------------------------------------
#---------------S HTML------------------------------------------------------------------------------------------
print '<html>'
print '<head> <title>History Rainfalls</title> </head>'
print '<body>'
tmpStr = '<img src="' + path + 'wqDstPlot.jpg" border=1><br><br>'
print tmpStr
print '</body>'
print '</html>'

#---------------E HTML------------------------------------------------------------------------------------------