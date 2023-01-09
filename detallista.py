a=int(input())
if(a % 2 == 0 or a % 3 == 0):
	print(a, 'es divisible emtre 2 o 3.')
else:
	print(a, 'no es divisible entre 2 y 3.')

if((a%2==0 and a%3!=0) or (a%2!=0 and a%3==0)):
	print(a, 'es divisible entre 2 o 3, pero no ambos.')
elif(a%2==0 and a%3==0):
	print(a, 'es divisible entre 2 y 3.')

"""
if (a%2 == 0 and a%3 == 0):
	print(a, 'es divisible entre 2 y 3.')
if (a%2 == 0 or a%3 == 0):
	print(a, 'es divisible entre 2 o 3.')
if (a%2!=0 and a%3!=0):
	print(a,'no es divisible entre 2 y 3.')
if((a%2==0 and a%3!=0) or (a%2!=0 and a%3==0)):
	print(a, 'es divisible entre 2 o 3, pero no ambos.')
"""