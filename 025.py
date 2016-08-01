F1 = 1
F2 = 1
n = 2
while len(str(F2)) < 1000:
	F3 = F2 + F1
	n += 1
	F1 = F2
	F2 = F3
	#print n,F3
print "[",n,"]result = ",F2