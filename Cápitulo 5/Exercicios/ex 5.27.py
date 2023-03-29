n = int(input('Digite o numero: '))
n = str(n)
print(n)

inverso = n[::-1]
print(inverso)

if inverso == n:
    print('É palindromo')
else:
    print('Não é palindromo')
