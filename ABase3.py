n=int(input())
resultado=''
while n>=3:
	resultado = str(n%3)+resultado
	n=n//3

resultado=str(n)+resultado
print(resultado)