#!/usr/bin/python

# Import modules for CGI handling 
import cgi
import cgitb

import powpy
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
sph = form.getvalue('sph')
cyl  = form.getvalue('cyl')
axis = form.getvalue('axis')
fTilt = form.getvalue('fTilt')
pTilt = form.getvalue('pTilt')
n = form.getvalue('index')
ec = form.getvalue('ec')
eye = form.getvalue('eye')
#def effective(fTilt, pTilt, n, S, C, axis, eye):
header = ''
apow = ''
if float(ec) == 1:
	apow = powpy.effective(float(fTilt), float(pTilt), float(n), float(sph), float(cyl), float(axis), float(eye))
	header = 'Effective'
else:
	apow = powpy.compensated(float(fTilt), float(pTilt), float(n), float(sph), float(cyl), float(axis), float(eye))
	header = 'Compensated'
print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
print "<title>PoW</title>"
print "<meta name='description' content=''>"
print "<meta name='author' content=''>"
print "<meta name='viewport' content='width=device-width, initial-scale=1'>"
print "<link href='//fonts.googleapis.com/css?family=Raleway:400,300,600' rel='stylesheet' type='text/css'>"
print "<link rel='stylesheet' href='/brent/css/normalize.css'>"
print "<link rel='stylesheet' href='/brent/css/skeleton.css'>"
print "<link rel='icon' type='image/png' href='/images/favicon.png'>"
print "</head>"
print "<body>"
print "<div class='container' style='margin-top: 10%; margin-left: auto; margin-right: auto'>"
print "<h4>%s Power</h4>" % header
print "%s" % apow
print "<br> <a class='button button-primary' href='pow.html'>Back</a>"
print "<a class='button button-primary' href='/brent/calculators'>Calculation Home</a>"
print "</div>"
print "</body></html>"