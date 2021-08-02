import sys
import queue
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	n = int(input())
	ans=''
	for i in range(n):
		input()
		sx1=0
		sy1=0
		sx2=0
		sy2=0
		xl1,yl1,xr1,yr1 = map(int,input().split(' '))
		xl2,yl2,xr2,yr2 = map(int,input().split(' '))
		sol=True
		if(xl2>=xr1 or xl1>=xr2):
			sol=False
		elif(yl2>=yr1 or yl1>=yr2):
			sol=False
		else:
			sx1=max(xl1,xl2)
			sy1=max(yl1,yl2)
			sx2=min(xr1,xr2)
			sy2=min(yr1,yr2)
		
		if sol==True:
			ans=ans+(str(sx1)+' '+str(sy1)+' '+str(sx2)+' '+str(sy2))
		else:
			ans=ans+('No Overlap')
			
		if i<n-1:
			ans=ans+'\n\n'
	print(ans)
if __name__ == '__main__':
	Main()