velocidade = int(input("Qual a velocidade do carro? "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Valor multa R$:  {multa:.2f}')