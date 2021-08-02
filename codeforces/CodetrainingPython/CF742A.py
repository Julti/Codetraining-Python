import sys
import queue
input = lambda: sys.stdin.readline()

def Main():
	n = int(input())
	d = [8,4,2,6]
	x = d[(n%4)-1]
	if n==0:
		x=1
	print(x)
if __name__ == '__main__':
	Main()