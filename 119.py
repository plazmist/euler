# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. 
# Another example of a number with this property is 614656 = 284.
# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
# You are given that a2 = 512 and a10 = 614656.
# Find a30.

import math

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

cnt=1
x = 80
#for x in xrange(10,614657):
while (cnt < 31):
	x += 1
	ss = sum_digits(x)
	#print x, ss, " digits"
	if (ss != 1):
		mul = ss
		while (mul < x):
			mul *= ss
		if (mul == x):
			print "Found",cnt," = ",x," sum =", ss, "mul =",mul
			cnt += 1