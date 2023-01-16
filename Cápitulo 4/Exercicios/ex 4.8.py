numero_1 = float(input('Digite o 1º numero: '))
numero_2 = float(input('Digite o 2º numero: '))
print('''Operações: 
+ para somar os números
- para bubtrair o segundo numero do primeiro
* para multiplicar o primeiro pelo segundo
/ para dividir o primeiro pelo segundo
''')
operacao = str(input('Digite a operação: '))

if operacao == '+':
    soma = numero_1 + numero_2
    print(f'soma de {numero_1} + {numero_2} = {soma}')
elif operacao == '-':
    subtracao = numero_1 - numero_2
    print(f'subtracao de {numero_1} - {numero_2} = {subtracao}')
elif operacao == '*':
    multiplicacao = numero_1 * numero_2
    print(f'multiplicacao de {numero_1} * {numero_2} = {multiplicacao}')
elif operacao == '/':
    divisao = numero_1 / numero_2
    print(f'divisao de {numero_1} / {numero_2} = {divisao}')
