lista_1 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
lista_2 = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
lista_3 = []
x = 0
while x < (len(lista_1)):
    if lista_1[x] in lista_3:
        x += 1
        pass
    else:
        lista_3.append(lista_1[x])
        x += 1
x = 0
while x < (len(lista_2)):
    if lista_2[x] in lista_3:
        x += 1
        pass
    else:
        lista_3.append(lista_2[x])
        x += 1

print('Lista 1: ', lista_1)
print('Lista 2: ', lista_2)
print('Lista 3(Lista 1 + 2): ', lista_3)
