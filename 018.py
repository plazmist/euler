# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:

with open('p067_triangle.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]

print "Lines = ",len(array)

cur_line = len(array) - 2
#print len(array[cur_line])

while (cur_line >= 0):
	for j in xrange(0,cur_line +1):
		if (array[cur_line + 1][j] > array[cur_line + 1][j+1]):
			array[cur_line][j] += array[cur_line + 1][j]
		else:
			array[cur_line][j] += array[cur_line + 1][j+1]
	print array[cur_line]
	cur_line -= 1
