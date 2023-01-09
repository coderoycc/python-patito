import sys
texto=sys.stdin.readlines()
for linea in texto:
	linea=linea.rstrip()
	numeros=linea.split()
	if int(numeros[0]) % int(numeros[1]) == 0:
		print(f'La división es exacta. Cociente: {int(numeros[0]) // int(numeros[1])}')
	else:
		print(f'La división no es exacta. Cociente: {int(numeros[0]) // int(numeros[1])} Resto: {int(numeros[0]) % int(numeros[1])}')