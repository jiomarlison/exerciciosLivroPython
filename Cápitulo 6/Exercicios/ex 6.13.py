t = [-10, -8, 0, 1, 2, 5, -2, -4]
media = 0
maximo = t[0]
minimo = t[0]

for e in t:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e
    media += e

media = media / len(t)

print(f"Lista de Temperaturas: {t}")
print(f'Temperatura Máxima: {maximo}')
print(f'Temperatura Minima: {minimo}')
print(f'Média das temperaturas: {media}')

# print(max(t))
# print(min(t))
