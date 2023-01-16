distancia_percorrer = float(input('Insira a distância a percorrer: '))

if distancia_percorrer <= 200:
    passagem = distancia_percorrer * 0.50
    print(f'Valor da passagem: {passagem:6.2f}')
else:
    passagem = distancia_percorrer * 0.45
    print(f'Valor da passagem: {passagem:8.2f}')
