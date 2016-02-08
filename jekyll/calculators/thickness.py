import math
import weight

def sign(x): 
	if x==0.0: 
		return 0.0 
	elif x>0.0: 
		return 1.0 
	else: 
		return -1.0
			
			
def Thickness(power, ref_front, index, min_blank, f1_sag, thick, minthickness):
		nameArray = ['<td>CR-39</td>', '<td>Trivex</td>', '<td>Spectralite</td>', '<td>Polycarbonate</td>', '<td>MR-6</td>', '<td>MR-8</td>', '<td>MR-7</td>', '<td>MR-10</td>', '<td>MR 174</td>']
		ref_back = power - ((ref_front)/(1 - (((thick/1000)/index))*ref_front))
		f2_radius = ((1-index)/ref_back)*1000
		f2_sag = f2_radius - (sign(f2_radius) * math.sqrt(math.pow(f2_radius,2) - math.pow(min_blank,2)))
		#'ref back ' +  str(ref_back)
		f1_radius = ((index - 1)/ref_front)*1000
		#def weight(f1_sag, r_1,f2_sag, r_2, min_blank, et )
		if power > 0:
			#print 'CT: ' + str(f1_sag - f2_sag + minthickness) + '\n' + 'ET: ' + str(minthickness)
			ct = f1_sag - f2_sag + minthickness
			et = minthickness
			ct = round(ct, 2)
			et = round(et, 2)
			#thickArray.insert(0,et)
			#thickArray.insert(1, ct)
			aweight = weight.weight(f1_sag, f1_radius, f2_sag, f2_radius, min_blank, et, index)
			htmlString =  "<td>" + str(index) + " heD</td><td>" + str(et) + " mm</td><td>" + str(ct) + " mm</td><td>" + str(aweight) + " grams</td>"
			
			return htmlString
			
			
			
		else:
			#print 'ET: ' + str(f2_sag - f1_sag + minthickness) + '\n' + 'CT: ' + str(minthickness)
			ct = minthickness
			et = f2_sag - f1_sag + minthickness
			#thickArray.insert(0,et)
			#thickArray.insert(1, ct)
			#return lens_thick
			#return "<h2>Edge Thickness </h2>" + str(et) + "<br>" + "<h2>Center Thickness </h2>" + str(ct)
			aweight = weight.weight(f1_sag, f1_radius, f2_sag, f2_radius, min_blank, et, index)
			htmlString =  "<td>" + str(index) + " heD</td><td>" + str(et) + " mm</td><td>" + str(ct) + " mm</td><td>" + str(aweight) + " grams</td>"
			return htmlString
		i = i + 1
def thickness(minthickness, bc, index, min_blank, power):
	
	ref_front = ((bc*(index-1))/0.53) + 0.00001
	f1_radius = ((index - 1)/ref_front)*1000
	back = (power-ref_front)/1
	back_radius = ((1-index)/back)*1000
	f1_sag = f1_radius - math.sqrt(math.pow(f1_radius,2) - math.pow(min_blank,2))
	
	
	 

	back_sag = back_radius - (sign(back_radius) * math.sqrt(math.pow(back_radius,2) - math.pow(min_blank,2)))
	app_thickness = 0
	y = 0
	
	

	
		
	if (f1_sag - back_sag) <= 0:
	#Thickness = minthickness
		
		#Thickness(minthickness)
		return Thickness(power, ref_front, index, min_blank, f1_sag, minthickness, minthickness)

	
	else:
		app_thickness = minthickness + (math.pow(min_blank,2) * power)/(2000 * (index-1))
	
		y = app_thickness + 1
	
		
		#def Thickness(power, ref_front, index, min_blank, f1_sag, thick):
		while True:
		
		
		
			back = power - ((ref_front)/(1-(((app_thickness/1000)/index))*ref_front))
			f2_radius = ((1-index)/back)*1000
			f2_sag = f2_radius - (sign(f2_radius) * math.sqrt(math.pow(f2_radius,2) - math.pow(min_blank,2)))
			y = f1_sag - f2_sag + minthickness
			app_thickness = app_thickness + (y - app_thickness)/2
			#'back ' + str(back) + ' f2_radius ' + str(f2_radius) + ' f2_sag ' + str(f2_sag) + ' y ' + str(y) + ' app_thickness ' + str(app_thickness)
			if (y - app_thickness) <= 0.05:
				
				return Thickness(power, ref_front,index, min_blank, f1_sag, app_thickness, minthickness)
				
				break
    
	

