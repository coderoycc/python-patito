"""import sys
entrada = sys.stdin.readlines()
for linea in entrada:
	linea=linea.rstrip()
	numeros=linea.split()
	"""
import math
numeros=input().split()
k=int(numeros[1])
s=0
for i in range(int(numeros[0])):
	s=s+(i+k)/(2+i+k)
print(math.ceil(s))
