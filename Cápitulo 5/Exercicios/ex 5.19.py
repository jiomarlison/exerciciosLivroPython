
valor = float(input('Digite o Valor: '))
valor_int = round(valor)
cedulas = 0
cedulas_atual = 100
apagar = valor_int

moedas_atual = 0.50
centavos = valor - valor_int

while True:
    if cedulas_atual <= apagar:
        apagar -= cedulas_atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${cedulas_atual}')
        if apagar == 0:
            break
        if apagar == 50:
            cedulas_atual = 20
        elif apagar == 20:
            cedulas_atual = 10
        elif apagar == 10:
            cedulas_atual = 5
        elif apagar == 5:
            cedulas_atual = 1
        cedulas = 0

