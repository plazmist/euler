# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
import numpy

N = 11
#Matrix = N*[N*[0]] #numpy.zeros((N, N))
Matrix = [[0 for i in range(N)] for j in range(N)]

def zeroFill(Mtr):
	for i in xrange(N):
		for j in xrange(N):
			Mtr = np.append(X, [[i, j]], axis=0)

def printMatrix(Matrix):
	# i = 0
	# for x in xrange(0,N):
	# 	for y in xrange(0,N):
	# 		print Matrix[x][y],
	# 		i += 1
	# 	print ""
	max_digits = len(str(N*N-1))    # for pretty printing
	print('\n'.join([' '.join(['{:0{pad}d}'.format(val, pad=max_digits) for val in row]) for row in Matrix]))

def spiralStartFill(Matrix):
	cnt=1
	for gl in xrange(0,N/2):
		for i in xrange(0+gl,N-gl):
			Matrix[gl][i] = cnt
			cnt += 1
		for i in xrange(1+gl,N-gl):
			Matrix[i][N-gl-1] = cnt
			cnt += 1
		for i in xrange(N-2-gl,gl,-1):
			Matrix[N-1-gl][i] = cnt
			cnt += 1
		for i in xrange(N-gl-1,gl,-1):
			Matrix[i][gl] = cnt
			cnt += 1
	if (N%2 == 1):
		Matrix[N/2][N/2]=cnt
			

def test(Matrix):
	i = 0
	for x in xrange(0,N):
		for y in xrange(0,N):
			Matrix[x][y] = i
			i += 1

def spiralCenterFill(Matrix):
	cnt=1
	if (N%2 == 1):
		Matrix[N/2][N/2] = cnt
	cnt += 1

	for gl in xrange(0,N/2):
		for i in xrange(N/2-gl,N/2+gl+2):
			Matrix[i][N/2+1+gl] = cnt
			cnt += 1
		for i in xrange(N/2+gl,N/2-2-gl,-1):
		  	Matrix[N/2+gl+1][i] = cnt
		  	cnt += 1
		for i in xrange(N/2+gl,N/2-gl-2,-1):
		 	Matrix[i][N/2-gl-1] = cnt
		 	cnt += 1
		for i in xrange(N/2-gl,N/2+gl+2):
			Matrix[N/2-gl-1][i]=cnt
			cnt += 1

spiralCenterFill(Matrix)
printMatrix(Matrix)
sum = 0
for i in xrange(0,N):
	sum += Matrix[i][i] + Matrix[i][N-i-1]
sum -= 1
print "Sum = ",sum

real_sum = 0
calc_sum = 0
for i in xrange(0,N):
	print Matrix[i][i],
	real_sum += Matrix[i][i]

print "real_sum =", real_sum

for i in xrange(0,N/2):
	print (13 + 10+ i*8),

