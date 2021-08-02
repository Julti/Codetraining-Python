import sys
import queue
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	while True:
		n,m = map(int,input().split(' '))
		if (n==0 and m==0):
			break
		incoming = [0]*n
		G = [None]*n
		for i in range(n):
			G[i]=[]
		for i in range(m):
			i,j = map(int,input().split(' '))
			incoming[j-1] = incoming[j-1]+1
			G[i-1].append(j-1)
		q = queue.Queue()
		for i in range(n):
			if incoming[i]==0:
				q.put(i)
		ans=''
		while q.empty()==False:
			x = q.get()
			ans=ans+str(x+1)+' '
			vals = G[x]
			for i in range(len(vals)):
				incoming[vals[i]]=incoming[vals[i]]-1
				if incoming[vals[i]]==0:
					q.put(vals[i])
		print(ans[:(len(ans)-1)])
if __name__ == '__main__':
	Main()