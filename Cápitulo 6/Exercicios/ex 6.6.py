ultimo1 = 0
ultimo2 = 0
fila1 = list()
fila2 = list()
while True:
    print(f'\nExistem {len(fila1)} clientes na fila 1')
    print(f'Existem {len(fila2)} clientes na fila 2')
    print(f'Fila 1 atual: {fila1}')
    print(f'Fila 2 atual: {fila2}')
    print('DIGITE F para adicionar um cliente ao fim da fila 1,'
          ' FF para 2 clientes, FFF para 3 clientes e assim por diante.')
    print('DIGITE A para realizar um atendimento da fila 1, AA para 2 atendimentos,'
          ' AAA para 3 e assim por diante. S para sair. ')
    print('DIGITE G para adicionar um cliente ao fim da fila 2,'
          ' GG para 2 clientes, GGG para 3 clientes e assim por diante.')
    print('DIGITE B para realizar um atendimento para a fila 2, BB para 2 atendimentos,'
          ' BBB para 3 e assim por diante. S para sair. ')
    print('EX: FFFAAAS, para adicionar 3 clientes e atender 3 clientes')
    print('Digite S para sair\n')
    operacao = str(input('Operações (F, A ou S): ')).upper()

    x = 0
    for x in range(len(operacao)):
        if operacao[x] == 'A':
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f'Cliente {atendido}, fila 1 atendido')
                x += 1
            else:
                print('Fila 1 vazia! Ninguem para atender')
                x += 1
        elif operacao[x] == 'F':
            ultimo1 += 1  # INCREMENTA O NOVO CLIENTE A SER ATENDIDO
            fila1.append(ultimo1)
            x += 1
        elif operacao[x] == 'B':
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f'Cliente {atendido}, fila 2 atendido')
                x += 1
            else:
                print('Fila 2 vazia! Ninguem para atender')
                x += 1
        elif operacao[x] == 'G':
            ultimo2 += 1  # INCREMENTA O NOVO CLIENTE A SER ATENDIDO
            fila2.append(ultimo2)
            x += 1
        elif operacao[x] == 'S':
            break
        else:
            print('Operação invalida! Digite apenas F, G, A, B ou S!')

    if operacao[len(operacao)-1] == 'S':
        break
