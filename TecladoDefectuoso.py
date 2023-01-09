"""import sys
texto=sys.stdin.readlines()
for linea in texto:
	linea=linea.rstrip()
"""

linea=input()
sw=True
final=''
arm=''
for l in linea:
	if l != '[' and l != ']':
		arm=arm+l
	else:
		if sw:
			final=arm+final
		else:
			final=final+arm

		if l=='[':
			sw=True
		else:
			sw=False
		arm=''

if sw:
	final=arm+final
else:
	final=final+arm

print(final)


#palabraFinal---> Sea]]el]]quien[[juzgue