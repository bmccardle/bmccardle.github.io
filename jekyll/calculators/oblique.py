import math



#convert axis to degrees

def oblique(sph, cyl, axis, powerAt):
	convert_deg = 180/math.pi
	convert_rad = math.pi/180

	alpha = math.pow(math.sin((powerAt - axis) * convert_rad),2)
	meridian = (cyl * alpha) + sph

	return meridian