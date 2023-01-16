maior = 0
menor = 999
for _ in range(3):
    numero = float(input(f'Digite o {_ + 1}º número: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f'Maior: {maior}\nMenor: {menor}')
