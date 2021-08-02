import sys
from math import sqrt
input = lambda: sys.stdin.readline()

def Main():
	stri = ''
	while True:
		a,b = map(str,(input().strip()).split(" "));
		
		if(a=="0" and b=="0"):
			break
		elif (a=="0" or b=="0"):
			stri=stri+'No carry operation.\n'
		else:
			carries=0
			carry=0
			to=0
			if(len(a)>len(b)):
				to=len(b)
			else:
				to=len(a)
			for i in range(1,to+1):
				val= (int(a[len(a)-i])+int(b[len(b)-i])+carry)
				if val>=10:
					carries=carries+1
					carry=1
				else:
					carry=0
			if(len(a)>len(b)):
				for i in range(to+1,len(a)+1):
					val= (int(a[len(a)-i])+carry)
					if val>=10:
						carries=carries+1
						carry=1
					else:
						carry=0
			elif(len(b)>len(a)):
				for i in range(to+1,len(b)+1):
					val= (int(b[len(b)-i])+carry)
					if val>=10:
						carries=carries+1
						carry=1
					else:
						carry=0
			if carries==0:
				stri=stri+'No carry operation.\n'
			elif carries==1:
				stri=stri+'1 carry operation.\n'
			else:
				stri=stri+str(carries)+" carry operations.\n"
	print(stri.strip())
if __name__ == '__main__':
	Main()