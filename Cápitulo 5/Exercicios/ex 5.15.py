soma = 0
while True:

    num_produto = int(input('Digite um numero: '))

    if num_produto == 1:
        soma += 0.50
    elif num_produto == 2:
        soma += 1.00
    elif num_produto == 3:
        soma += 4.00
    elif num_produto == 5:
        soma += 7.00
    elif num_produto == 9:
        soma = soma + 8.00
    elif num_produto == 0:
        print(f'Soma Total dos produtos: {soma}')
        break
    else:
        print("Código invalido!")