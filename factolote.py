def esFacto(numero):
	facto=2
	i=3
	while facto < numero:
		facto=facto*i
		i+=1

	if facto==numero:
		return (i-1)
	return -1


n = int(input())
cont=1
while n!=-1:
	r=esFacto(n)
	print("Case#", cont)
	if r != -1:
		print(f'El numero {n} = {r}!.')
	else:
		print(f'El numero {n} no es un factorial.')
	n=int(input())
	cont+=1
print("---------FIN DE ARCHIVO---------")