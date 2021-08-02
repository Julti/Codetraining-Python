import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	q = int(input())
	s = [0]*q
	a = 0
	while(a<q):
		v = input().strip().split(' ')
		print(v)
		for i in v:
			print(a)
			s[a]=int(i)
			a=a+1
	print(s)
if __name__ == '__main__':
	Main()