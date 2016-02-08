
import math

def minBlank(a, dbl, pd):
	
	if pd > 40:
		min_blank = ((a + dbl) - pd)
		min_blank = (min_blank + a)/2
		return min_blank
		
	else:
		pd = pd * 2
		min_blank = ((a + dbl) - pd)
		min_blank = (min_blank + a)/2
		return min_blank