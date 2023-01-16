kwh = float(input('Quantos Kwh foram utilizados: '))
print('''Tipos de instalação
R para residencia
I para industria
C para comercio
''')
tipo_instalcao = str(input('Qual o tipo de instalação R, I ou C: ')).upper()

if tipo_instalcao == 'R':
    if kwh <= 500:
        print(f'Valor a pagar: {kwh * 0.40}')
    if kwh > 500:
        print(f'Valor a pagar: {kwh * 0.65}')
elif tipo_instalcao == 'I':
    if kwh <= 1000:
        print(f'Valor a pagar: {kwh * 0.55}')
    if kwh > 1000:
        print(f'Valor a pagar: {kwh * 0.60}')

elif tipo_instalcao == 'C':
    if kwh <= 5000:
        print(f'Valor a pagar: {kwh * 0.55}')
    if kwh > 5000:
        print(f'Valor a pagar: {kwh * 0.60}')
