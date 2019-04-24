import itertools
import resource

def makeMaxed(n):
	res = ""
	for x in xrange(10,-1,-1):
		for i in range(0,len(n)):
			if (int(n[i]) == x):
				res += str(x)
	return res

def isCube(x):
    return int(round(x ** (1. / 3))) ** 3 == x

def otherCubes(cub1):
	for x in xrange(100,10000):
		cubX = makeMaxed(str(x**3))
		if (cubX == cub1):
			print x, x**3

def minCub5():
	Cubes = {}
	for x in xrange(340,10000):
		cub1 = makeMaxed(str(x**3))
		#print x, str(x**3), cub1
		if cub1 in Cubes:
			Cubes[cub1] +=1
			if (Cubes[cub1] == 5):
				minCub5 = cub1
				break
		else:
			Cubes[cub1] =1
	return minCub5

otherCubes(minCub5())

