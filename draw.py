from PIL import Image, ImageDraw
im = Image.new('RGBA', (400, 400), (0, 0, 0, 0)) 
draw = ImageDraw.Draw(im) 
draw.line((0,0, 300,300), fill="red")
#draw. ellipse((10,10,300,300), fill="red", outline="red")

N = 22

for i in xrange(0,2*N+1):
	
	print "(",2**i % N,",",3**i % N,")"


del draw

im.save("test.png", "PNG")