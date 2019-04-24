import math

def isclose(a, b, E=1e-07):
	return True if (abs(a - b) < E) else False

def trngl(r_lim,bak):
	cnt = 0
	a = 1
	b = a+1
	r = 0
	kMAX = 0
	while (r <= r_lim):
		r = 0
		while ((r <= r_lim) and (b < bak*a)):
			c = math.sqrt(a**2 + b**2 - a*b)
			r = a*b*math.sqrt(3)/(2.*(a+b+c))
			#print "test",a,b,c, "r =",r
			if (isclose(math.floor(c),c) and (r < r_lim)):
				cnt += 1
				k = b/a
				if (k>kMAX):
					kMAX=k
				print "Found (",a,b,c, ") "
			b +=1
		a +=1
		b = a+1
		c = math.sqrt(a**2 + b**2 - a*b)
		r = a*b*math.sqrt(3)/(2.*(a+b+c))
	print "b/a = ",bak," T(",r_lim,") =", cnt, "kMAX =", kMAX
#for x in xrange(2,100):
#	trngl2(x)
#trngl2(51)

trngl(100,200)


#1000 Totally found 20669 kMAX = 299
# T( 1000 ) = 21544 kMAX = 499
# b/a = 1000 T( 1000 ) = 22278 kMAX = 998
#b/a =  2000  T( 1000 ) = 22767 kMAX = 1732
