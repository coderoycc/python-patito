cont = 0
may = 0
n = 0
def efe(nn):
	if(nn%2==0 and nn>=0):
		cont+=1
	else:
		if cont>may:
			may=cont
		cont=0

while n!=-9999:
	n = int(input())
	efe(n)
print(may)