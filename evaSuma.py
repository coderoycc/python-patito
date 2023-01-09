a=int(input())
signo=1
elemento=2
cadena=''
suma=0
for i in range(a):
	if i%2==0:
		signo=abs(signo)
		suma=suma+signo*elemento
		cadena=cadena+" + "+str(elemento)
		elemento=elemento-1
	else:
		signo=signo*(-1)
		suma=suma+signo*elemento
		cadena=cadena+" - "+str(elemento)
		elemento=elemento+3

cadena=cadena[3:]
print(f'{cadena} = {suma}')