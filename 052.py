#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def dgt_in_num(val):
	dgt = [1,2,3,4,5,6,7,8,9]
	while (val > 0) :
		dd = val%10
		if dd in dgt: dgt.remove(dd)
		val /=10
	if not dgt:
		return True
	else:
		return False

dgt = []
dgtK = []
x = 125873
while True:
	x += 1
	dgt = []
	x_str = str(x)
	for i in xrange(0,len(x_str)):
		dgt.append(x_str[i:(i+1)])
	for k in xrange(2,7):
		dgtK = []
		k_str = str(x*k)
		for i in xrange(0,len(k_str)):
			dgtK.append(k_str[i:(i+1)])
		if (set(dgt) != set(dgtK)):
			break
	if (set(dgt) == set(dgtK)):
		print x, dgt
