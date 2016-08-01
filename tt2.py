import itertools

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

dgt = '1234567'
N = len(dgt)
comb = []
comb += itertools.permutations(dgt)
print "======"

#Numbers ending with digit 0, 2, 4, 5, 6 or 8 are never prime
notPrimes = ['0','2','4','5','6','8']
for n in xrange(0,len(comb)):
	if (comb[n][N-1] not in notPrimes):
		num = 0
		for i in xrange(0,N):
			num += int(comb[n][i]) * 10**(N-i-1)
		print num, isPrime2(num)