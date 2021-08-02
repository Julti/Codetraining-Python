import sys
input = lambda: sys.stdin.readline()
def Main():
	while True:
		try:
			a = input()
			print(a)
		except EOFError:
			break
if __name__ == '__main__':
	Main()