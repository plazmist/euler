file_handle = open("185text.py", "r")

sqLen = 5
lines_list = file_handle.readlines()
file_handle.close()
lines_num = len(lines_list)

couldBe = [ [] for row in xrange(sqLen+1)]
prob = [ ([0]*10) for row in xrange(sqLen+1)]
for x in xrange(0,lines_num):
	for y in xrange(0,sqLen+1):
		if (lines_list[x][y] not in couldBe[y]):
			couldBe[y].append(lines_list[x][y])
for x in xrange(0,lines_num):
	for y in xrange(0,sqLen+1):
		if (lines_list[x][sqLen+2] == '0'):
			couldBe[y].remove(lines_list[x][y])			
#print lines_list
for x in xrange(0,sqLen):
	print "for",x,"dgt = ",sorted(couldBe[x])


for x in xrange(0,lines_num):
	koef = int(lines_list[x][sqLen+2])
	for y in xrange(0,sqLen):
		#print "line",x,"digit",y,"=",int(lines_list[x][y])
		prob[y][int(lines_list[x][y])] += koef

for x in xrange(0,sqLen):
	#print "for dgt",x,prob[x]
	maxVx = 0
	for y in xrange(1,10):
		if (prob[x][maxVx] < prob[x][y]):
			maxVx = y
	print "for dgt",x,"could be",
	for y in xrange(1,10):
		if (prob[x][maxVx] == prob[x][y]):
			print y,
	print