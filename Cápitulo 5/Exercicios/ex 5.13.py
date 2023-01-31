import math
div_inicial = float(input('Digite o valor da divida: '))
taxa_juros = float(input('Digite a taxa de juros: '))
pagamento_mensal = float(input('Digite o valor pago mensalmente: '))

taxa_juros = taxa_juros / 100
meses = math.ceil((div_inicial + (div_inicial * taxa_juros))/pagamento_mensal)

total_pago = 0
juros_pagos = 0
x = 1

print(f'\nValor Inicial: {div_inicial}\n')

while x <= meses:
    print(f'Mês {x}:')
    juros_pagos += div_inicial * taxa_juros
    div_inicial += (div_inicial * taxa_juros)
    total_pago += pagamento_mensal
    div_inicial -= pagamento_mensal
    print(f'Valor: {div_inicial:5.2f}')
    x += 1

print(f'\nTotal meses: {meses}')
print(f'Total pago: {total_pago:5.2f}')
print(f'Juros total pago: {juros_pagos:5.2f}')