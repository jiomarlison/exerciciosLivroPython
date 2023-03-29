# APRESENTAÇÃO DE NUMEROS

numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f'Número {x+1}: '))
    x += 1

while True:
    escolhido = int(input('Digite qual posição deseja ver (0 para sair): '))
    if escolhido == 0:
        break
    elif escolhido > len(numeros):
        print(f'Não existe número na posição {escolhido}, apenas numeros nas posições de 1 até {len(numeros)}')
    else:
        print(f'Você escolheu o número: {numeros[escolhido - 1]}')