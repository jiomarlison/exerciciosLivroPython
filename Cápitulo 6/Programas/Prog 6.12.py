# COPIA DE ELEMENTOS PARA OUTRAS LISTAS
v = [9, 8, 7, 12, 0, 13, 21]
p = []
i = []
for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)
print('Pares: ', p)
print('Impares: ', i)