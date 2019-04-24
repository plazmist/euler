import math

def check(val):
	if (val[18] == '0') and (val[16] == '9') and (val[14] == '8')and (val[12] == '7')and (val[10] == '6')and (val[8] == '5')and (val[6] == '4')and (val[4] == '3')and (val[2] == '2')and (val[0] == '1'):
		print "Found", val


#1_2_3_4_5_6_7_8_9_0
#print math.sqrt(1020304050607080900)
#print math.sqrt(1929394959697989990)

min = 1010101010
max = 1389026623

#for x in xrange(min,max):
#	check(str(x**2))
print math.sqrt(1929374254627488900)