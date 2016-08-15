import re
def sum_of_chars(wrd):
	sum = 0
	for x in xrange(0,len(wrd)):
		sum += ord(wrd[x]) - 64
	return sum
def print_word_counts(filename):
    s=open(filename).read()
    words=re.findall('[a-zA-Z]+', s)
    words.sort()
    sum = 0
    for x in xrange(0,len(words)):
    	#print x+1,"=",words[x], sum_of_chars(words[x])
    	sum += (x+1)*sum_of_chars(words[x])
    print "Sum =", sum

print_word_counts('022_names.txt')
