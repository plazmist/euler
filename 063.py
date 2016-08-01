
from math import log10

def try1():
	cnt = 0
	for power in xrange(1,1000):
		x = 0
		ll = 0
		while ll < power:
			x += 1
			ll = len(str(x**power))
		
		while (ll == power):
			print x, "^", power, "=", x**power, "[",ll,"]"
			cnt +=1
			x += 1
			ll = len(str(x**power))
	print "Cnt =", cnt


def try2():
	cnt = 0
	for x in xrange(1,10):
		power = 1
		ll = 0
		while ll < power:
			power += 1
			ll = len(str(x**power))
		if (ll == power):
			print x, "^", power, "=", x**power, "[",ll,"]"
			cnt +=1

	print "Cnt =", cnt

try1()
