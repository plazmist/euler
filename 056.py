# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

sum_max = 0
for a in xrange(2,101):
	for b in xrange(1,101):
		x = a ** b
		summ = 0
		while (x > 0) :
			dd = x%10
			summ += dd
			x /=10
		if (summ > sum_max):
			sum_max = summ
			print a,b," sum = ", sum_max
