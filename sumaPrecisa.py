"""import sys
entrada=sys.stdin.readlines()
for p in entrada:
	p=p.rstrip()
	"""
p=int(input())
up=4
down=2
suma=0
incremento=3
fiboa=0
fibob=1
for n in range(p):
	#print(up)
	suma=suma+up/down
	down+=2
	up=up+incremento
	incremento=incremento+(fiboa+fibob)
	fiboa, fibob = (fiboa+fibob), fiboa

print("{0:.4f}".format(suma))
#redondea a 4 decimales