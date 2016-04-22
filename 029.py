

my_list = []

for a in xrange(2,100+1):
	for b in xrange(2,100+1):
		x = a**b
		if x not in my_list:
			my_list.append(x)

print my_list
print "Len = ",len(my_list)
