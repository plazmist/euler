from __future__ import print_function
import time,math
from datetime import datetime

def isSquare(x):
    return int(round(x ** (1. / 2))) ** 2 == x

maxX = 0
for D in xrange(62,1000):
	if (not isSquare(D)):
		x = int(math.sqrt(D))+1
		while True:
			if ( ((x*x - 1) % D == 0) and isSquare((x*x - 1)/D) ):
				print('{} {}'.format(D,x))
				if (x > maxX):
					maxX = x
					maxD = D
				break
			else:
				x +=1
print('MaxD ={}'.format(maxD))
