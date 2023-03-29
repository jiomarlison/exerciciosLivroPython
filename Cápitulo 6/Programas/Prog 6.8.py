prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f'\nExistem \033[31m{len(pilha)}\033[m pratos na pilha')
    print(f'Pilha atual: \033[32m{pilha}\033[m')
    print('Digite \033[34mE\033[m para empilhar um novo prato,'
          '\033[34mD\033[m para desempilhar um e \033[34mS\033[m para sair.')
    operacao = input('Operação (\033[34mE, D\033[m ou \033[34mS\033[m): ').upper()
    if operacao[0] == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f'\033[33mPrato {lavado} lavado.\033[m')
        else:
            print('\033[31mPilha vazia, nenhum prato para lavar!\033[m')
    elif operacao == 'E':
        prato += 1  # NOVO PRATO
        pilha.append(prato)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida! Digite apenas E, D ou S!')
