preco = 5.2468

print('\nQUANTIDADE DE CASA DECIMAIS')
# alinhado a direita, com 10 caracteres e 2 casas decimais
print(f'Preço: {preco:.2f}')
print(f'Preço: {preco:.3f}')
print(f'Preço: {preco:.4f}')


print('\nALINHAMENTO DOS VALORES')
# alinhado a direita, com 10 caracteres e 2 casas decimais
print(f'Preço: {preco:>10.2f}')
# alinhado a esquerda, com 10 caracteres e 2 casas decimais
print(f'Preço: {preco:<10.2f}')
# alinhado ao centro, com 10 caracteres e 2 casas decimais
print(f'Preço: {preco:^10.2f}')

print('\nSUBSTITUIÇÃO DOS ESPAÇOS EM BRANCO')
# preenchimento de espaços em branco
print(f'Preço: {preco:.>10.2f}')
print(f'Preço: {preco:.<10.2f}')
print(f'Preço: {preco:.^10.2f}\n')

print(f'Preço: {preco:_>10.2f}')
print(f'Preço: {preco:_<10.2f}')
print(f'Preço: {preco:_^10.2f}\n')

print(f'Preço: {preco:~<10.2f}')
print(f'Preço: {preco:~>10.2f}')
print(f'Preço: {preco:~^10.2f}\n')
