import math


def weight(f1_sag, r_1,f2_sag, r_2, min_blank, et, n ):
#front volume
	
	min_blank = min_blank * 2
	r_1cm = r_1/10
	f1_sagcm = f1_sag/10

	f1_volume = (math.pi/3)*(math.pow(f1_sagcm,2))*((3 * r_1cm)-f1_sagcm)


	#back volume
	

	r_2cm = r_2/10
	f2_sagcm = f2_sag/10

	f2_volume = (math.pi/3)*(math.pow(f2_sagcm,2))*((3 * r_2cm)-f2_sagcm)

#	cyl volum

	cyl_volume = (math.pi * math.pow(min_blank,2) * et)/4000

	total_volume = f1_volume - f2_volume + cyl_volume



	specific_gravity = 0
	if n == 1.498:
		specific_gravity = 1.32

	if n == 1.527:
		specific_gravity = 1.11
	if n == 1.537:
		specific_gravity = 1.2
	if n == 1.586:
		specific_gravity = 1.21
	if n == 1.595:
		specific_gravity = 1.34
	if n == 1.592:
		specific_gravity = 1.30
	if n == 1.658:
		specific_gravity = 1.35
	if n == 1.661:
		specific_gravity = 1.37
	if n == 1.732:
		specific_gravity = 1.47

	weight = total_volume * specific_gravity
	return round(weight, 2)
