l = [15, 7, 27, 39]

p = int(input('Digite o 1º valor a procurar: '))
v = int(input('Digite o 2º valor a procurar: '))

achou = False
x = 0

while x < len(l):
    if l[x] == p:
        print(f'{p} encontrado na posição: {x}')
    if l[x] == v:
        print(f'{v} encontrado na posição: {x}')
    x += 1
