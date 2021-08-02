import sys
t = int(sys.stdin.readline())
for i in range(t):
	a,b = map(int,sys.stdin.readline().split(" "))
	n = int(input())
	res =''
	count=0
	while res!='WRONG_ANSWER\n' and count<n:
		count=count+1
		guess = (int)((b+(a+1))/2)
		print(str(guess))
		sys.stdout.flush()
		res = sys.stdin.readline()
		if res=='CORRECT\n':
			break
		elif res=='TOO_BIG\n':
			b=guess
		elif res=='TOO_SMALL\n':
			if guess==b-1:
				a=b
			else:
				a=guess
		else:
			break
