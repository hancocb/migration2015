#!/usr/local/bin/python
print "Content-Type: text/html\n\n";
print "<!DOCTYPE html>"

import cgi, cgitb, os, string, random, datetime, glob, locale
from string import split,join
form = cgi.FieldStorage()
cgitb.enable()

#"Gully.txt":Gully,      'WildLife.txt':WildLife,        "Reference.txt" : Reference,
#            "Feedlot.txt":Feedlot,  'pcp.txt':pcp,                  "mainINP.txt" : mainINP,
#            "Septic.txt":Septic,    'LandRain_GW1.txt':LandRain_GW1, "BMPs.txt" : BMPs,

print 'haha'
test = form.getvalue('WildLife.txt')
print test
test = form.getvalue('GullyDB.txt')
print test