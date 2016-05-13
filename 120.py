total = 0
for a in xrange(3,1001):
	rMax = 0
	for n in xrange(1,2000):
		r = ((a-1)**n + (a+1)**n) % (a**2)
		if (r > rMax):
			rMax=r
	total += rMax

	#print "for a =",a," rMax = ",rMax
print total