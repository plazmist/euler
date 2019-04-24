import time

def isPalindrom(num):
	return num == num[::-1]


n=4994
cnt=1
MAX_I = 50
LychCnt = 0
MAX = 10000
for x in xrange(10,MAX):
	n = x
	cnt = 1
	n +=  int(str(n)[::-1])
	while not isPalindrom(str(n)) and cnt < MAX_I:
		n +=  int(str(n)[::-1])
		#print cnt,": ",n,"(",len(str(n)),")"
		cnt+=1
	if not isPalindrom(str(n)):
		LychCnt += 1
		print x,"is Lychrel, with",cnt
print "There are",LychCnt,"below",MAX
		