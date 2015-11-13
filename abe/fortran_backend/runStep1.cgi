#!/usr/local/bin/python
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>"

import cgi, cgitb, os, string, random, datetime, glob, locale
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

fileNames = [
"Gully.txt",    'WildLife.txt',     "Reference.txt",
"Feedlot.txt",  'pcp.txt',          "mainINP.txt",
"Septic.txt",   'LandRain_GW1.txt', "BMPs.txt",
]

for name in fileNames:
    content = form.getvalue(name)
    file = open(name,'w')
    file.write(content)

print "{\"status\":\"succ\"}"