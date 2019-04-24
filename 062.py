# this approach is f*cking not optimal 
from datetime import datetime
import thread,sys,time
import itertools

def isCube(x):
    return int(round(x ** (1. / 3))) ** 3 == x

def otherCubes(threadName,cub1):
	perLst = list(map("".join, itertools.permutations(str(cub1**3))))
	cubes = []
	for x in perLst:
		if isCube(int(x)):
			cc = int(round((int(x)**(1./3.))))
			#print cc, int(x)
			if (cc not in cubes):
				cubes.append(cc)
	if len(cubes) > 2 :
		print threadName,cub1,"^3 =",cub1**3,"with",len(cubes),":", cubes, "Elasped", datetime.now() - start
	return len(cubes)

def testInt(threadName,beginN,step):
	curCub = beginN + step
	while True:
		if (curCub % 10 != 0):
			curCubCnt = otherCubes(threadName,curCub)
			# if ( curCubCnt > maxCube):
			# 	maxCube = curCubCnt
		curCub += step

# maxCube = 0
# curCub = 4
# while (maxCube < 8):
# 	if (curCub % 10 != 0):
# 		curCubCnt = otherCubes(curCub)
# 		if ( curCubCnt > maxCube):
# 			maxCube = curCubCnt
# 	curCub += 1


start = datetime.now()
START = 340
END = 1000000
try:
   thread.start_new_thread( testInt, ("Thread-1", START,4 ) )
   thread.start_new_thread( testInt, ("Thread-2", START+1,4 ) )
   thread.start_new_thread( testInt, ("Thread-3", START+2,4 ) )
   thread.start_new_thread( testInt, ("Thread-4", START+3,4 ) )
except:
   print "Error: unable to start thread"

while 1:
    time.sleep(3)