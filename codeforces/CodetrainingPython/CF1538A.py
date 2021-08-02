n = int(input())
for j in range(n):
	s = int(input())
	numbers = (input().split(' '))
	dist_a=0
	dist_b=0
	print(len(numbers),s)
	for i in range(int(s/2)-1):
		if int(numbers[i])== 1 or int(numbers[i])==s:
			dist_a=i
		elif int(numbers[s-i])== 1 or int(numbers[s-i])==s:
			dist_b=i
		if dist_a !=0 and dist_b!=0:
			break
	dist_a+=1
	dist_b+=1
	f_dist_a = dist_a+dist_b
	f_dist_b = dist_a+abs(dist_a-dist_b)
	print(min(f_dist_a,f_dist_b))