#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import math
import oblique
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
sph = form.getvalue('sph')
cyl  = form.getvalue('cyl')
axis = form.getvalue('axis')
powerAt = form.getvalue('powerAt')





meridian = oblique.oblique(float(sph), float(cyl), float(axis), float(powerAt))

#def oblique(sph, cyl, axis, powerAt):

print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
print "<title>Brent's Page</title>"
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
print "<h2>Power At %.2f: %.2f</h2>" % (float(powerAt),meridian)
print " <a class='button button-primary' href='oblique-meridian.html'>Back</a>"
print "<a class='button button-primary' href='/brent/calculators'>Calculation Home</a>"
print "</div>"
print "</body></html>"

#print "Content-type:text/html\r\n\r\n"
#print "<html>"
#print "<head>"
#print "<title>Answer</title>"
#print "</head>"
#print "<body>"
#print "<h2>Power At %.2f: %.2f</h2>" % (float(powerAt),meridian)
#print "</body>"
#print "</html>"