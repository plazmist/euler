x0 = 0
y0 = 0
cnt = 0
with open('p102_triangles.txt') as f:
	for line in f:
		row = line.split(',')
		x1 = int(row[0])
		y1 = int(row[1])
		x2 = int(row[2])
		y2 = int(row[3])
		x3 = int(row[4])
		y3 = int(row[5])
		p1 = (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
		p2 = (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
		p3 = (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)
		if ( ((p1 > 0) and (p2 > 0) and (p3 > 0)) or ((p1 < 0) and (p2 < 0) and (p3 < 0)) ):
			cnt += 1
print "cnt =",cnt
