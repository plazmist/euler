from __future__ import print_function
import string


f = open('p059_cipher.txt', 'r')
# "0"=48 "9"=57
# "A"=65 "Z"=90
# "a"=97 "z"=122prinatble S

def decodePrint(key):
	keyLen = len(key)
	pointer = 0
	keyPointer = 0
	Sum = 0
	while (pointer < len(fields)):
		symbl = int(fields[pointer]) ^ ord(key[keyPointer])
 		print('{}'.format(chr(symbl)), end="")
 		Sum += symbl
 		pointer += 1
 		if (keyPointer == keyLen-1):
 			keyPointer = 0
 		else:
 			keyPointer +=1
 	print("\nSum = {}".format(Sum))


def decodeAnalize(x1,x2,x3):
	x = 0
	falseChar = False
	upperCase = 0
	lowerCase = 0
	punct = 0
	while (x < len(fields)-2):
 		ch1 = int(fields[x+0]) ^ x1
 		ch2 = int(fields[x+1]) ^ x2
 		ch3 = int(fields[x+2]) ^ x3
	 	if ((chr(ch1) not in string.printable) or (chr(ch2) not in string.printable) or (chr(ch3) not in string.printable)):
			falseChar = True
			break
		# upperCase
	 	if (chr(ch1) in string.ascii_uppercase):
	 		upperCase += 1
	 	if (chr(ch2) in string.ascii_uppercase):
	 		upperCase += 1
	 	if (chr(ch3) in string.ascii_uppercase):
	 		upperCase += 1
	 	#lowerCase
	 	if (chr(ch1) in string.ascii_lowercase):
	 		lowerCase += 1
	 	if (chr(ch2) in string.ascii_lowercase):
	 		lowerCase += 1
	 	if (chr(ch3) in string.ascii_lowercase):
	 		lowerCase += 1
	 	# punctuations	
	 	if (chr(ch1) in string.punctuation):
	 		punct += 1
	 	if (chr(ch2) in string.punctuation):
	 		punct += 1
	 	if (chr(ch3) in string.punctuation):
	 		punct += 1
 		x +=3
 	ratio = 1.0*100*(upperCase + lowerCase) / len(fields)
 	if (not falseChar) and (ratio > 70) and (punct < 100):
 		print ('Key \"{}{}{}\" upperCase = {} lowerCase = {} punct = {} ratio = {}'.format(chr(x1),chr(x2),chr(x3),upperCase,lowerCase,punct,ratio))


for line in f:
    fields = line.strip().split(",")

print("Total = {}".format(len(fields)))
for x1 in xrange(ord("a"),ord("z")+1):
	for x2 in xrange(ord("a"),ord("z")+1):
		for x3 in xrange(ord("a"),ord("z")+1):
			decodeAnalize(x1,x2,x3)

decodePrint("god")

