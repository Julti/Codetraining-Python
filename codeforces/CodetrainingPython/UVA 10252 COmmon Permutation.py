import sys
input = lambda: sys.stdin.readline()
def Main():
	while True:
		try:
			a = input()
			b = input()
		except:
			break
		dicta = {}
		dictb = {}
		maxval = max(len(a),len(b))
		for i in range(maxval):
			if(i<len(a)):
				if a[i] in dicta and a[i] in b:
					dicta[a[i]]= dicta[a[i]]+1
				else:
					dicta[a[i]]=1
			if(i<len(b)):
				if b[i] in dictb and b[i] in a:
					dictb[b[i]]= dictb[b[i]]+1
				else:
					dictb[b[i]]=1
		sol=[]
		for i in dicta:
			if i in dictb:
				sol.append(i*min(dicta[i],dictb[i]))
		sol.sort()
		print(''.join(sol).strip())
if __name__ == '__main__':
	Main()