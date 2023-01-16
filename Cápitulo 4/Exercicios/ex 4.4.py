salario = float(input('Digite o salario para calculo de aumento: '))

if salario > 1.250:
    print(f"Aumento de 10%, que equivale a R$: {salario * 0.10:6.2f}")
    salario += salario * 0.10
if salario < 1250:
    print(f"Aumento de 15%, que equivale a R$: {salario * 0.15:6.2f}")
    salario += salario * 0.15

print(f'Salario após aumento: {salario:6.2f}')