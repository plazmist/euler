import numpy as np


def reminder(n,p):
#	print "n =",n, "p =",p
	res = (p-1)**n + (p-1)**n
	res %= p**2
	return res

def main():
    n = input('Find the next prime number greater great than: ')
    print find_next_prime(n+1)

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

#[ 7037 ] =  71059 reminder =  1000084366
prime_n = 7037
prime = 71059

#for x in xrange(1,100):
while (prime < 31000):
	print "[",prime_n,"] = ", prime
	prime = find_next_prime(prime+1)
	prime_n += 1

reminder = 0
while (reminder < 10000000000):
	reminder = ((prime-1)**prime_n + (prime+1)**prime_n) % (prime**2)
	print "[",prime_n,"] = ", prime, "reminder = ", reminder
	prime = find_next_prime(prime+1)
	prime_n += 1
		