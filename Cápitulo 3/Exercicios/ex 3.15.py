cigaros = int(input("Quantos Cigaros Fumados Por Dia: "))
anos = int(input("Quantidade de Anos Fumando: "))

print(f"Tempo de Vida Reduzido em Dias: {((cigaros*365*anos)*10/60)/24:.0f}")
