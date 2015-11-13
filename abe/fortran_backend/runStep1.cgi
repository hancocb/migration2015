#!/usr/local/bin/python
print "Content-Type: application/json";

import cgi, cgitb, os, string, random, datetime, glob, locale
from string import split,join
from CLIGEN import genCLIGEN
from Run1 import run1

form = cgi.FieldStorage()
cgitb.enable()

fileNames = [
"Gully.txt",    'WildLife.txt',     "Reference.txt",
"Feedlot.txt",            "mainINP.txt",
"Septic.txt",   'LandRain_GW1.txt', "BMPs.txt",
]

#fileNames = ["Gully.txt"]

#print form.getvalue('pcp_FileName') + "\n"
#print form.getvalue('pcp_stateN') + "\n"
#print form.getvalue('pcp_countyN') + "\n"
#print form.getvalue('pcp_stationN') + "\n"
#print form.getvalue('from_id') + "\n"

FileName = form.getvalue('pcp_FileName')
stateN = form.getvalue('pcp_stateN') 
countyN = form.getvalue('pcp_countyN') 
stationN = form.getvalue('pcp_stationN') 
from_id = form.getvalue('from_id') 

genCLIGEN(FileName,stateN,countyN,stationN,from_id)

for name in fileNames:
    content = form.getvalue(name)
    #print "!!!"+name + "\n\n"
    #print content
    wfile = open( from_id + "/" + name, 'w')
    wfile.write(content)
    wfile.close()

ret = run1(from_id)

#parse myRST.csv and return
print "{\"status\":\"succ\"}"
