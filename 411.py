import math
N = 22
def Spath(N):
	path =set()
	points = set()
	for i in xrange(0,2*N+1):
		pp = (2**i % N,3**i % N)
		points.add(pp)
	
	while len(points)>1:
		bestPcnt = 0
		bestP = (N,N)
		for point in points:
			goodPcnt = 0
			for curP in points:
				if ((curP[0]>=point[0]) and (curP[1]>=point[1])):
					goodPcnt +=1
			if (goodPcnt>bestPcnt):
				bestPcnt = goodPcnt
				bestP = point
		#print "found",bestP, "with",bestPcnt
		path.add(bestP)
		for curP in points.copy():
			if ((curP[0]<bestP[0]) or (curP[1]<bestP[1])):
				points.remove(curP)
		points.remove(bestP)
	path.add(points.pop())

	#print "THE path is", path, "with", len(path)
	return len(path)

print "THE! = ",Spath(123)