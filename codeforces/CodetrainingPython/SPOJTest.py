import sys
input = lambda: sys.stdin.readline()

def Main():
	
	while True:
		a = int(input())
		if(a==42):
			break
		else:
			print(a)
	
if __name__ == '__main__':
	Main()