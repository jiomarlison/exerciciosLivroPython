num_1 = int(input("Número 1: "))
num_2 = int(input("Número 2: "))
result = 0
x = 1

while x <= num_1:
    result += num_2
    x += 1

print(f'Resultado multiplicação: {result}')
