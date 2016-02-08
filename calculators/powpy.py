import math


def effective(fTilt, pTilt, n, S, C, axis, eye):
	 
    fDegrees = (fTilt*math.pi)/180
    pDegrees = (pTilt*math.pi)/180
    theta = math.sqrt(math.pow(math.sin(fDegrees), 2) + math.pow(math.tan(pDegrees), 2))/math.cos(fDegrees)
    theta = (math.atan(theta)*180)/math.pi
    
    #find tc, sc, hc eq 12-14
    axisE = (theta * math.pi)/180
    tc = ((2*n) + math.pow(math.sin(axisE), 2))/((2*n)*(math.pow(math.cos(axisE), 2)))
    sc = 1 + (math.pow(math.sin(axisE), 2)/(2*n))
    hc = (tc + sc)/2
    
    #find a eq 19
    a = math.sin(pDegrees)/math.tan(fDegrees)
    a = (math.atan(a)*180)/math.pi
    
    	
    if eye == 1:
    	#dlfdj
    	a = 90 - a 
    
    #eq 16
   
    
    oa = axis - a
    #find px,py, pt eq 1-4
    oaDegrees = (oa * math.pi)/180
    px = S + (C * math.pow(math.sin(oaDegrees), 2))
    py = S + (C * math.pow(math.cos(oaDegrees), 2))
    pt = (-1 * C)*(math.sin(oaDegrees)) * (math.cos(oaDegrees))
    newPX=0.0
    newPY=0.0
    newPT=0.0
    
    if eye == 1:
    	#NSLog(@"px=%.2f py=%.2f pt=%.2f", px*sc, py*tc, pt*hc);
    	newPX = px*sc
    	newPY = py*tc
    	newPT = pt*hc
    else:
    	#NSLog(@"px=%.2f py=%.2f pt=%.2f", px*tc, py*sc, pt*hc);
    	newPX = px*tc
    	newPY = py*sc
    	newPT = pt*hc
    
    #eq 5-
    t = newPX + newPY
    d = (newPX*newPY) - (newPT * newPT)
    c = math.sqrt((math.pow(t, 2) - (4*d))) * -1
    s = (t - c)/2
    THETA = (s - newPX)/newPT
    THETA = (math.atan(THETA)*180)/math.pi
    #NSLog(@"THETA: %.2f",THETA);
    newAxis = math.tan(pDegrees)/math.sin(fDegrees)
    newAxis = (math.atan(newAxis)*180)/math.pi
    if eye == 1:
    	newAxis = 90 - newAxis
        #NSLog(@"left");

    
    #NSLog(@"A'':%.2f", newAxis);
    
    
    	if THETA < 0:
    		newAxis = 360 + THETA - 180 + newAxis
    	else:
    		newAxis = newAxis + THETA
        
    
    if newAxis > 180:
        newAxis = newAxis - 180
    
    return '%.2f %.2f X %.2f' % (s, c, newAxis)
   
def compensated(fTilt, pTilt, n, S, C, axis, eye):
	fDegrees = (fTilt * math.pi)/180
	pDegrees = (pTilt * math.pi)/180
	#find theta eq. 17
	theta = math.sqrt(math.pow(math.sin(fDegrees), 2) + math.pow(math.tan(pDegrees), 2))/math.cos(fDegrees)
	theta = (math.atan(theta)*180)/math.pi
	#NSLog(@"theta: %.2f", theta);
	#find tc, sc, hc eq 12-14
	axisE = (theta * math.pi)/180;
	tc = ((2*n) + math.pow(math.sin(axisE), 2))/((2*n)*(math.pow(math.cos(axisE), 2)))
	sc = 1 + (math.pow(math.sin(axisE), 2)/(2*n))
	hc = (tc + sc)/2
	#NSLog(@"tc: %.2f sc: %.2f hc: %.2f", tc, sc, hc);
	#find a eq 18
	a = math.tan(pDegrees)/math.sin(fDegrees)
	a = (math.atan(a)*180)/math.pi
	if eye == 1:
		#left eq 20
		a = 90 - a
	#eq 16
	oa = axis - a
	#find px,py, pt eq 1-4
	oaDegrees = (oa * math.pi)/180
	px = S + (C * math.pow(math.sin(oaDegrees), 2))
	py = S + (C * math.pow(math.cos(oaDegrees), 2))
	pt = (-1 * C)*(math.sin(oaDegrees)) * (math.cos(oaDegrees))
	newPX=0.0
	newPY=0.0
	newPT=0.0
	if eye ==1:
		#NSLog(@"px=%.2f py=%.2f pt=%.2f", px/sc, py/tc, pt/hc);
		newPX = px/sc
		newPY = py/tc
		newPT = pt/hc
	else:
		#NSLog(@"px=%.2f py=%.2f pt=%.2f", px/tc, py/sc, pt/hc);
		newPX = px/tc
		newPY = py/sc
		newPT = pt/hc
	#eq 5-9
	t = newPX + newPY
	d = (newPX*newPY) - (newPT * newPT)
	c = math.sqrt((math.pow(t, 2) - (4*d))) * -1
	s = (t - c)/2
	THETA = (s - newPX)/newPT
	THETA = (math.atan(THETA)*180)/math.pi
	#NSLog(@"THETA: %.2f",THETA);
	newAxis = math.sin(pDegrees)/math.tan(fDegrees)
	newAxis = (math.atan(newAxis)*180)/math.pi
	if eye == 1:
		newAxis = 90 - newAxis
		#NSLog(@"left");
	#NSLog(@"A'':%.2f", newAxis);
	if eye == 0 and THETA == 90:
		#NSLog(@"od axis %.2f", newAxis);
		newAxis = newAxis
		#new else for no cylinder
	else:
		if THETA < 0:
			newAxis = 360 + THETA - 180 + newAxis
				#NSLog(@"new axis theta < 0 %.2f", newAxis);
		else:
			newAxis = newAxis + THETA
	if newAxis > 180:
		newAxis = newAxis - 180
    
	return '%.2f %.2f X %.2f' % (s, c, newAxis)
	