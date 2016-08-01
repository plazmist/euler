from datetime import datetime
import thread,sys,time
#import threading

def relativelyPrimeNum(a,b):
	ll = min(a,b)
	for x in xrange(2,ll+1):
		if (a % x == 0) and (b % x == 0):
			return False
	return True

# RP = []
# maxF = 0
# maxFn = 0
# for n in xrange(2,5000):
# 	RP = []
# 	for x in xrange(1,n):
# 		if relativelyPrimeNum(n,x):
# 			RP.append(x)
# 	res = float(n)/len(RP)
# 	#print n, RP, len(RP), res
# 	if (maxF < res):
# 		maxF = res
# 		maxFn = n
# print "Elasped", datetime.now()-start
# print "for n = ",maxFn," res = ", maxF

def testInt(threadName,beginN,step):
	maxF = 0
	maxFn = 0
	for n in xrange(beginN,END,step):
		cnt = 0
		for x in xrange(1,n):
			if relativelyPrimeNum(n,x):
				cnt += 1
		res = float(n)/cnt
		#print n, RP, len(RP), res
		if (maxF < res):
			maxF = res
			maxFn = n
			print threadName, "Found: for n = ",maxFn," res = ", maxF
	print threadName, "for n = ",maxFn," res = ", maxF
	print threadName, "Elasped", datetime.now() - start

start = datetime.now()
START = 1
END = 1000000
try:
   thread.start_new_thread( testInt, ("Thread-1", START,4 ) )
   thread.start_new_thread( testInt, ("Thread-2", START+1,4 ) )
   thread.start_new_thread( testInt, ("Thread-3", START+2,4 ) )
   thread.start_new_thread( testInt, ("Thread-4", START+3,4 ) )
except:
   print "Error: unable to start thread"

#testInt("Thread-1", START,4)
while 1:
    time.sleep(3)

