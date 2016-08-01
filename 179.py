import datetime

def dividors(n):
	cnt = 2
	for x in xrange(2,n/2):
		if (n % x == 0):
			cnt += 1
	return cnt

start = datetime.datetime.now()
d1 = 0
d2 = 0
cnt = 0
for x in xrange(2,10**7+1):
	d1 = d2
	d2 = dividors(x)
	if (d1 == d2):
		cnt += 1
		print x-1,"and",x,"has",d1,"dividors Elasped:",(datetime.datetime.now() - start)
print "Found", cnt, "integers"
