n=input()
numeros=n.split()
salida=''
for i in range(1, int(numeros[1])+1):
	print(str(int(numeros[0])*i), end=" ")
