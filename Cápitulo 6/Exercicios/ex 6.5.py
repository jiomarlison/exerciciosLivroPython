ultimo = 0
fila = list()
while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('DIGITE F para adicionar um cliente ao fim da fila,'
          ' FF para 2 clientes, FFF para 3 clientes e assim por diante.')
    print('DIGITE A para realizar um atendimento, AA para 2 atendimentos,'
          ' AAA para 3 e assim por diante. S para sair. ')
    print('EX: FFFAAAS, para adicionar 3 clientes e atender 3 clientes')
    print('Digite S para sair\n')
    operacao = str(input('Operações (F, A ou S): ')).upper()

    x = 0
    for x in range(len(operacao)):
        if operacao[x] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'Cliente {atendido} atendido')
                x += 1
            else:
                print('Fila vazia! Ninguem para atender')
                x += 1
        elif operacao[x] == 'F':
            ultimo += 1  # INCREMENTA O NOVO CLIENTE A SER ATENDIDO
            fila.append(ultimo)
            x += 1
        elif operacao[x] == 'S':
            break
        else:
            print('Operação invalida! Digite apenas F, A ou S!')

    if operacao[len(operacao)-1] == 'S':
        break
