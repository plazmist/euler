import numpy as np

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    print sieve
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def primesfrom3to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a array of primes, p < n """
    assert n>=100
    sieve = np.ones(n/2, dtype=np.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return np.r_[2, 2*np.nonzero(sieve)[0][1::]+1]  

def find_next_prime2(n):
	while True:
		if n % 2 == 1: 
			for i in xrange(3,n,2):
				if n % i == 0:
					break
			else:
				return n
		n += 1
	return None

print primesfrom2to(1100)
print find_next_prime2(1000)
