dias = int(input("Digite a Quantidade de dias: "))
horas = int(input("Digite a Quantidade de Horas: "))
minutos = int(input("Digite a Quantidade de Minutos: "))
segundos = int(input("Digite a Quantidade de Segundos: "))

segundos_totais = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"Dias:{dias}, Horas:{horas}, Minutos:{minutos}, Segundos:{segundos}.\nSegundos Totais: {segundos_totais}")
