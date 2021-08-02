import sys
input = lambda: sys.stdin.readline()

def Main():
	rectangles = []
	while True:
		line = input().strip()
		if line=='*':
			break
		else:
			data = line.split(' ')
			rectangles.append(data)
	figure = 0
	while True:
		figure =figure+1
		x,y = map(float,input().split(' '))
		if x ==9999.9 and y==9999.9:
			break
		contained = False
		for i in range(len(rectangles)):
			if((y>float(rectangles[i][4]) and y<float(rectangles[i][2])) and (x>float(rectangles[i][1]) and x<float(rectangles[i][3]))):
				contained = True
				print('Point '+str(figure)+' is contained in figure '+str(i+1))
		if contained==False:
			print('Point '+str(figure)+' is not contained in any figure')
if __name__ == '__main__':
	Main()