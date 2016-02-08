#!/usr/bin/python

# Import modules for CGI handling 
import cgi
import cgitb 

import thickness
import oblique
import min_blank
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

	



sph = form.getvalue('sph')
cyl  = form.getvalue('cyl')
axis = form.getvalue('axis')
minThick = form.getvalue('minThick')
#index = form.getvalue('index')
a = form.getvalue('a')
dbl = form.getvalue('dbl')
bc = form.getvalue('bc')
pd = form.getvalue('pd')
#def oblique(sph, cyl, axis, powerAt):

	

horizontalPower = oblique.oblique(float(sph), float(cyl), float(axis), 180.0)
#def thickness(minthickness, bc, index, min_blank, power):
#def minBlank(a, dbl, pd):
min_blank = min_blank.minBlank(float(a), float(dbl), float(pd))


#<option id="index" value="1.498">CR-39</option>
#<option id="index" value="1.527">Trivex</option>
#<option id="index" value="1.537">Spectralite</option>
#<option id="index" value="1.586">Polycarbonate</option>
#<option id="index" value="1.595">MR-6</option>
#<option id="index" value="1.592">MR-8</option>
#<option id="index" value="1.658">MR-7</option>
#<option id="index" value="1.661">MR-10</option>
#<option id="index" value="1.732">MR 174</option>

index = [1.498, 1.527, 1.537, 1.586, 1.595,  1.592, 1.658, 1.661, 1.732]
thickArray = []
nameArray = ['<td>CR-39</td>', '<td>Trivex</td>', '<td>Spectralite</td>', '<td>Polycarbonate</td>', '<td>MR-6</td>', '<td>MR-8</td>', '<td>MR-7</td>', '<td>MR-10</td>', '<td>MR 174</td>']
i = 0
for n in index:
	aThickness = thickness.thickness(float(minThick),float(bc), n, min_blank, horizontalPower)
	thickArray.insert(i, ('<tr>' + nameArray[i] + aThickness + '</tr>'))
	
	i = i+1
	
thickArray = ''.join(thickArray)	
print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
print "<title>Thickness</title>"
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
print "<h4>Lens Analysis</h4>"
print "<ul><li>Power at 180&deg %s</li><li>Minimum Blank %s mm</li><li>Base Curve %s D</li>" % (str(horizontalPower), str(min_blank), bc )
print "<table class='u-full-width'><thead><tr><th>Material Name</th><th>Index</th><th>ET</th><th>CT</th><th>Weight</th></tr></thead><tbody>"
print "%s" % thickArray
print "</tbody></table>"
print "<br> <a class='button button-primary' href='thickness.html'>Back</a>"
print "<a class='button button-primary' href='/brent/calculators'>Calculation Home</a>"
print "</div>"
print "</body></html>"