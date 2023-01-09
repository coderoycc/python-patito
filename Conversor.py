n=int(input())
k=n//100000
m=(n%100000)//100
c=((n%100000)%100)
print(f'{n} centímetros son {k} km {m} m {c} cm')