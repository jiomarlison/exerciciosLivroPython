num_1 = int(input("Número 1: "))
num_2 = int(input("Número 2: "))
result = 0
x = 0

while num_2 <= num_1:
    x += 1
    num_1 -= num_2
    result = num_1 - num_2

print(f'Resultado: {x}')
print(f'resto: {num_1}')
