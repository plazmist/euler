from usefullFunctions import isPrime2
import time

startTime = time.time()

nn = 0
for x in xrange(1,1000000):
	if isPrime2(x):
#		print ('{},'.format(x)),
		nn += 1
print "\nNum = ",nn

resultDelay = time.time() - startTime 
print "Time =", resultDelay
