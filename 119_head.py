def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
# digits number in result
DGT = 15
results = []
for x in xrange(2,9*DGT):
	for y in xrange(2,10):
		z = x**y
		if (sum_digits(z) == x):
			if z not in results:
				results.append(z)

results.sort()
i=1
for x in results:
	print i,"=",x
	i+=1