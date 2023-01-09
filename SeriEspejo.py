n=int(input())
a=1
for i in range(n):
	if i%2==1:
		a=a*(-1)
		print(a, end=" ")
		a=a*(-1)
		a+=1
	else:
		print(a, end=" ")