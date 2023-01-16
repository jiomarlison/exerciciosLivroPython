valor_casa = float(input('Valor da casa a se comprar: '))
salario = float(input('Valor do salario: '))
quantidade_anos = int(input('Quantos anos deseja pagar: '))

quantidade_meses = quantidade_anos * 12
valor_parcelas = valor_casa / quantidade_meses

print(f'\nTotal de parcela: {quantidade_meses:6.2f}\nValor de cada parcela: {valor_parcelas:6.2f}')

if valor_parcelas > salario * 0.30:
    print('\nEmprestimo Negado!')
else:
    print('\nEmprestimo Aprovado!')