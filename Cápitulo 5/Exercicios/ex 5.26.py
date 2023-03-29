n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

if n1 >= n2:
    while n1 >= n2:
        n1 -= n2
    print('Resto: ', n1)
else:
    print('Resto: ', n1)
