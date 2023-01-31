deposito = float(input('Digite o valor inicial depositado: '))
taxa_juros = float(input('Digite a taxa de juros: '))
taxa_juros = taxa_juros / 100
x = 1
print(f'\nValor Inicial: {deposito}\n')
while x <= 24:
    print(f'Mês {x}:')
    if x > 1:
        adicional = float(input('Valor depositado nesse mês: '))
        deposito += adicional
    deposito += (deposito * taxa_juros)
    print(f'Valor: {deposito:5.2f}')
    x += 1
print(f'\nValor Final Após {x-1} Meses: {deposito:5.2f}\n')
