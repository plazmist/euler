
def check(value):
	for x in xrange(0,len(value)-2):
		if (int(value[x]) + int(value[x+1]) + int(value[x+2]) > 9):
			return False
	return True

duples = set()
fiftes = set()
triples = set()
sixtes = set()

for a0 in xrange(1,10):
	for a1 in xrange(0,10):
		if ((a0+a1) <=9):
			duples.add(str(a0)+str(a1))
print "Duples =",len(duples)

# for a0 in xrange(1,10):
# 	for a1 in xrange(0,10):
# 		for a2 in xrange(0,10):
# 			for a3 in xrange(0,10):
# 				for a4 in xrange(0,10):
# 					if ((a0+a1+a2 <=9) and (a1+a2+a3 <=9) and (a2+a3+a4 <=9)):
# 						#print str(a0)+str(a1)+str(a2)+str(a3)+str(a3)
# 						fiftes.add(str(a0)+str(a1)+str(a2)+str(a3)+str(a4))

for a0 in xrange(0,10):
	for a1 in xrange(0,10):
		for a2 in xrange(0,10):
			if (a0+a1+a2 <=9):
				triples.add(str(a0)+str(a1)+str(a2))
print "Triples =", len(triples)

for tr1 in triples:
	for tr2 in triples:
		if check(tr1+tr2):
			sixtes.add(tr1+tr2)
print "Sxites =", len(sixtes)


itsok=0
curr=0

for dup in duples:
	print "... pocessing",round(100.*curr/len(duples), 1),"%"
	curr +=1
	for six1 in sixtes:
		for six2 in sixtes:
			for six3 in sixtes:
				if check(dup+six1+six2+six3):
					itsok+=1

# for fif in fiftes:
# 	print "... pocessing",round(100.*fif_cnt/len(fiftes), 1),"%"
# 	fif_cnt+=1
# 	for tr1 in triples:
# 		for tr2 in triples:
# 			for tr3 in triples:
# 				for tr4 in triples:
# 					for tr5 in triples:
# 						if check(fif+tr1+tr2+tr3+tr4+tr5):
# 							itsok+=1

print "itsok =",itsok, "ratio =", 100.*itsok/ (len(duples)*len(sixtes)),"%"