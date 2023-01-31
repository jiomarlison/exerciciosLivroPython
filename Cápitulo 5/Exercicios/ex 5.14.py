x = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma += num
    x += 1
media = soma / x
print(f'Soma dos números: {soma} \nQuantiade de números digitados: {x} \nMédia aritmética: {media:5.2f}')
