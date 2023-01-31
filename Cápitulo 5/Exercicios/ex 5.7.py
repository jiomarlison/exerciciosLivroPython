const = 2
inicio = int(input("iniciar por: "))
fim = int(input("Finalizar em: "))

while inicio <= fim:
    print(f'{const} X {inicio} = {const * inicio}')
    inicio += 1

