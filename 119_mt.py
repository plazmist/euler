
import thread
import time

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


#cnt=1
def testInt(threadName,beginN,step):
	x = beginN
	global cnt
	while (cnt < 31):
		x += step
		ss = sum_digits(x)
		#print x, ss, " digits"
		if (ss != 1):
			mul = ss
			while (mul < x):
				mul *= ss
			if (mul == x):
				resultDelay = time.time() - startTime 
				print threadName," found",cnt," = ",x," sum =", ss, "mul =",mul, "with", resultDelay
				cnt += 1


cnt=16
Fnd = 205962876
#Fnd = 11
startTime = time.time()
# Create two threads as follows
try:
   thread.start_new_thread( testInt, ("Thread-1", Fnd,4 ) )
   thread.start_new_thread( testInt, ("Thread-2", Fnd+1,4 ) )
   thread.start_new_thread( testInt, ("Thread-3", Fnd+2,4 ) )
   thread.start_new_thread( testInt, ("Thread-4", Fnd+3,4 ) )
except:
   print "Error: unable to start thread"

while 1:
   pass

# Found 1  =  81  sum = 9 mul = 81
# Found 2  =  512  sum = 8 mul = 512
# Found 3  =  2401  sum = 7 mul = 2401
# Found 4  =  4913  sum = 17 mul = 4913
# Found 5  =  5832  sum = 18 mul = 5832
# Found 6  =  17576  sum = 26 mul = 17576
# Found 7  =  19683  sum = 27 mul = 19683
# Found 8  =  234256  sum = 22 mul = 234256
# Found 9  =  390625  sum = 25 mul = 390625
# Found 10  =  614656  sum = 28 mul = 614656
# Found 11  =  1679616  sum = 36 mul = 1679616
# Found 12  =  17210368  sum = 28 mul = 17210368
# Found 13  =  34012224  sum = 18 mul = 34012224
# Found 14  =  52521875  sum = 35 mul = 52521875
# Found 15  =  60466176  sum = 36 mul = 60466176
# Found 16  =  205962976  sum = 46 mul = 205962976
# Thread-1  found 17  =  612220032  sum = 18 mul = 612220032 with 31746.5279171
