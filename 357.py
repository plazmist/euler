import time

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

N = 1000

def ChekThisN(n):
#    if not isPrime2(n+1):
#        print "xxx"
#        return False
	for d in range(2,n):
		if n%d == 0:
			ss = d + n/d
			if not isPrime2(ss):
				return False
	return True	

Sum = 0
startTime = time.time()
# for n in xrange(2,200000):
# 	Sum += (n if ChekThisX(n) else 0)
n = 2
while (n < N):
    n = find_next_prime(n+1)
    if ChekThisN(n-1):
        print "Found ",n-1
        Sum += n-1 


print "Time =",  time.time() - startTime 

print "Sum = ",Sum

