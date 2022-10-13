salario = float(input("DIGITE O SÁLARIO: "))
aumento = float(input("DIGITE A PORCENTAGEM DO AUMENTO: "))
print(f"Valor do Aumento: {salario * aumento/100:5.2f}")
print(f"Salario Após Aumento: {salario + (salario * aumento / 100):5.2f}")