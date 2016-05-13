import numpy as np
import datetime

def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        if p % 2 == 1: 
	        for i in range(3, p,2):
	            if p % i == 0:
	                break
	        else:
	            return p
    return None

def find_next_prime2(n):
	while True:
		if n % 2 == 1: 
			for i in xrange(3,int(n**0.5),2):
				if n % i == 0:
					break
			else:
				return n
		n += 1
	return None

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

# represents the maximum number of repeated digits for an 
# n-digit prime where 
# d is the repeated digit
def M(n,d):
	cur = 10**(n-1)
	d_qt = 0
	d_qt_max = 0
	while (cur < 10**(n)):
		cur = find_next_prime(cur+1)
		print cur
		cur_tmp = cur
		while (cur_tmp>0):
			if (cur_tmp%10 == d):
				d_qt += 1
			cur_tmp /= 10
		if (d_qt > d_qt_max): d_qt_max = d_qt
	return d_qt_max

#def N(n,d): #represents the number of such primes

def M2_brut(n):
	cnt = 0
	cur = 10**(n-1)
	d_qt = [0] * 10
	d_qt_max = [0] * 10
	N = [0] * 10
	S = [0] * 10
	cur = find_next_prime2(cur)
	while (cur < 10**(n)):
		#print "[",cnt,"]", cur
		d_qt = [0] * 10
		cur_tmp = cur
		
		while (cur_tmp>0):
			d_qt[cur_tmp%10] += 1
			cur_tmp /= 10

		for x in xrange(0,10):
			if (d_qt[x] > d_qt_max[x]): 
				d_qt_max[x] = d_qt[x]
				N[x] = 0
				S[x] = 0
			if (d_qt[x] == d_qt_max[x]):
				 N[x] += 1
				 S[x] += cur
		cur = find_next_prime2(cur+1)
		cnt += 1
	Sum = 0	
	for x in xrange(0,10):
		print x, d_qt_max[x], N[x], S[x]
		Sum += S[x]
	print "Grand total =", Sum
	return 0

def isPrime(n):
	if (n%2 == 0):
		return False 
	for i in xrange(3,int(n**0.5),2):
		if n % i == 0:
			return False
	else:
		return True

def M2_reverces(n):
	min_q = n-2
	cnt = 0
	cur = 10**(n-1)+1
	d_qt_max = [min_q] * 10
	N = [0] * 10
	S = [0] * 10
	#cur = find_next_prime2(cur)
	while (cur < 10**(n)):

		d_qt = [0] * 10
		cur_tmp = cur
		while (cur_tmp>0):
			d_qt[cur_tmp%10] += 1
			cur_tmp /= 10

		cont = False
		for x in xrange(0,10):
			if (d_qt[x] >= d_qt_max[x]):
				cont = True

		if ((cont) and isPrime(cur)):
			cnt += 1
			#print "[",cnt,"]", cur, "is prime"
			#print d_qt
			for x in xrange(0,10):
				if (d_qt[x] > d_qt_max[x]): 
					d_qt_max[x] = d_qt[x]
					N[x] = 0
					S[x] = 0
				if (d_qt[x] == d_qt_max[x]):
				 	N[x] += 1
				 	S[x] += cur
		cur += 2

	Sum = 0	
	for x in xrange(0,10):
		print x, d_qt_max[x], N[x], S[x]
		Sum += S[x]
	print "Grand total =", Sum
	return 0

def M2_generate(n):
	min_q = n-2
	for repearter in xrange(0,10):
		pass





n = 10
print "N = ", n
start = datetime.datetime.now()
M2_reverces(n)
print "Elasped:",(datetime.datetime.now() - start)
print "----------------------------"
#start = datetime.datetime.now()
#M2_brut(n)
#print (datetime.datetime.now() - start)