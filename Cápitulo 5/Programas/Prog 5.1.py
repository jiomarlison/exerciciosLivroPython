# Contagem de cédulas
valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if apagar == 0:
            break
        elif apagar == 50:
            atual = 20
        elif apagar == 20:
            atual = 10
        elif apagar == 10:
            atual = 5
        elif apagar == 5:
            atual = 1
        cedulas = 0
