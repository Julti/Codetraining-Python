import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	n = int(input());
	for i in range(n):
		m = input().split(" ")
		cout =0
		for j in range(int(m[0]),int(m[1])+1):
			if(getgn(j)==int(m[2])):
				cout=cout+1
		print(cout)
def getgn(n):
	if n<10:
		return n
	else:
		sr = str(n)
		nn=1
		for i in range(len(sr)):
			if(int(sr[i])>0):
				nn=nn*int(sr[i])
		return getgn(nn)
if __name__ == '__main__':
	Main()