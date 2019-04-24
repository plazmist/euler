points = set()

for x in xrange(1,4):
	pp = (x,x)
	points.add(pp)

print points

cnt = 0
for p1 in points:
	for p2 in points:
		print p1,p2
		cnt +=1

print "all =",cnt