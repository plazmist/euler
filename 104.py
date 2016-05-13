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

F1 = 1
F2 = 1
cnt = 3
for x in xrange(1,535):
	F = F2 + F1
	F_str = str(F)
	F_len = len(F_str)
	F1 = F2
	F2 = F
	cnt += 1

head = False
tail = False
while not (head and tail):
	F = F2 + F1
	F_str = str(F)
	F_len = len(F_str)
	#print "Fib ",cnt, "(",len(str(F)),") =", F
	head = dgt_in_num(int(F_str[0:9])) 
	tail = dgt_in_num(int(F_str[(F_len-9):(F_len)])) 
	if (head or tail): 
		print "Fib [",cnt,"] lng = ",F_len, head, tail
	F1 = F2
	F2 = F
	cnt += 1

print "The end!", cnt-1, "has HEAD and TAIL"