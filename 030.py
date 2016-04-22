
Sum = 0
for n in xrange(2,1000000):
    n2 = n
    s = 0
    while n:
        s += (n % 10)**5
        n //= 10
    if (s == n2): 
    	print "x = ",n2
    	Sum += n2
print "Grand total =", Sum
	
