lugares_vagos = [10, 2, 1, 3, 0]
lugares = 0
while True:
    sala = int(input('Sala (0 para sair): '))
    if sala == 0:
        print('Fim')
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida!')
    elif lugares_vagos[sala-1] == 0:
        print('Desculpe, Sala lotada!')
    else:
        lugares = int(input(f'Quantos lugares deseja ({lugares_vagos[sala-1]}vagos):'))
    if lugares > lugares_vagos[sala-1]:
        print('Esse número de lugar não esta disponivel.')
    elif lugares < 0:
        print('Número invalido!')
    else:
        lugares_vagos[sala-1] -= lugares
        print(f'{lugares} lugares vendidos')
print('Utilização de salas')
for x, l in enumerate(lugares_vagos):
    print(f'Sala {x+1} - {l} lugar(es) vazio(s)')

