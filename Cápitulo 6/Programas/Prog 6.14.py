# LENDO E IMPRIMINDO UMA LISTA DE COMPRAS
compras = []
print('Digite FIM para sair')
while True:
    produto = input('Produto: ')
    if produto.upper() == 'FIM':
        break
    compras.append(produto)
    if len(compras) % 10 == 0:
        print('Digite FIM para sair')
for p in compras:
    print(p)
