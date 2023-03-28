while True:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("""ESCOLHA UMA OPERAÇÃO\n0 - SAIR\n1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - DIVISÃO\n4 - MULTIPLICAÇÃO
    """)
    opcao = int(input('Digite sua opção: '))
    match opcao:
        case 0:
            break
        case 1:
            for i in range(11):
                for j in range(11):
                    if i == 0:
                        pass
                    elif j == 0:
                        pass
                    else:
                        print(f'{i} + {j} = {i + j}')
                print('\n')
        case 2:
            for i in range(11):
                for j in range(11):
                    if i == 0:
                        pass
                    elif j == 0:
                        pass
                    else:
                        print(f'{i} - {j} = {i - j}')
                print('\n')
        case 3:
            for i in range(11):
                for j in range(11):
                    if i == 0:
                        pass
                    elif j == 0:
                        pass
                    else:
                        print(f'{i} / {j} = {i / j}')
                print('\n')
        case 4:
            for i in range(11):
                for j in range(11):
                    if i == 0:
                        pass
                    elif j == 0:
                        pass
                    else:
                        print(f'{i} * {j} = {i * j}')
                print('\n')
