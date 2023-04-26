compras = []
while True:
    produto = input("Produto: ")
    if produto.upper() == 'FIM':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto, quantidade, preco])
soma = 0.0
print(f'{"Nome Produto ":20s}   {"Quantidade":5s} {"Preço":7s} {"Valor Total":8s}')
for e in compras:
    print(f'{e[0]:20s} x {e[1]:10d} {e[2]:5.2f} {e[2] * e[2]:10.2f}')