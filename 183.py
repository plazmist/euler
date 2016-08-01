from decimal import *
import time
import thread

START = 5
END = 101

def findK(n):
	k = 1
	prev = 0
	next = n
	while (prev < next):
		k += 1
		prev = next
		next = Decimal( Decimal(1.0*n/k) **k)
	return k-1 

def terminating(a,b):
	if (len(str(1.0*a/b)) > 11) :
		return False
	else:
		return True

def testInt(threadName,startN,step,Sum):
	for N in xrange(startN,END,step):
		k = findK(N)
		if (terminating(N,k)):
			Sum -= N
		else:
			Sum += N
Sum1 = 0
Sum2 = 0
Sum3 = 0
Sum4 = 0

try:
   thread.start_new_thread( testInt, ("Thread-1", START,4, Sum1) )
   thread.start_new_thread( testInt, ("Thread-2", START+1,4, Sum2 ) )
   thread.start_new_thread( testInt, ("Thread-3", START+2,4, Sum3 ) )
   thread.start_new_thread( testInt, ("Thread-4", START+3,4, Sum4 ) )
except:
   print "Error: unable to start thread"

#while 1:
#   pass

print "sum = ", Sum1 + Sum2 + Sum3 + Sum4


# Sum = 0
# globalStartTime = time.time()
# for N in xrange(5,10001):
# 	startTime = time.time()
# 	k = findK(N)
# 	Pmax = (1.0*N/k)
# 	resultDelay = time.time() - startTime 
# 	print N, "k =",k, " M = (", N,"/",k,")**",k, "=", Pmax, terminating(N,k), "by", resultDelay

# 	if (terminating(N,k)):
# 		Sum -= N
# 	else:
# 		Sum += N

# print "Sum = ",Sum
# print "Global execution time =", time.time() - globalStartTime
# print len(str(1.0/3))