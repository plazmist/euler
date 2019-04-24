file_handle = open("185.txt", "r")

sqLen = 16
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
		if (koef == 0):
			prob[y][int(lines_list[x][y])] = 0
		else:
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
# 584[56]859[46]472285[56]7
# 5841859[4,6]473285[5,6]7 - this is what I get
# 5841859447328557
# 5841859447328567
# 5841859647328557
# 5841859647328567

# test
# 584[56]859[46]472285[56]7
#res1 = '5845859447228557'
#res1 = '5845859447228567'
#res1 = '5845859647228557'
#res1 = '5845859647228567'
#res1 = '5846859447228557'
#res1 = '5846859447228567'
#res1 = '5846859647228557'
res1 = '5846859647228567'

for x in xrange(0,lines_num):
	cnt = 0
	for y in xrange(0,sqLen):
		if (lines_list[x][y] == res1[y]):
			cnt +=1
	if (cnt < int(lines_list[x][sqLen+2])):
		concl = 'FAIL'
	else:
		concl = 'ok'
	print lines_list[x][0:-8], cnt, concl
	