import sys
import queue
input = lambda: sys.stdin.readline()

def Main():
	n = int(input())
	d = [None]*n
	for i in range(n):
		d[i]=input().strip()
	valx = d[0][0]
	valr = d[0][1]
	work = True
	for i in range(n):
		for j in range(n):
			if (i==j or j==(n-(i+1))):
				
				if d[i][j]!= valx:
					work=False
			else:
				
				if d[i][j]!= valr:
					work=False
	if valx==valr:
		work=False
	if work==True:
		print('YES')
	else:
		print('NO')
if __name__ == '__main__':
	Main()