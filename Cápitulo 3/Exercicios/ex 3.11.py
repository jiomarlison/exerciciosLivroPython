preco_produto = float(input("VALOR DO PRODUTO: "))
desconto = int(input("VALOR DO DESCONTO: "))
print(f"Desconto de R$ {preco_produto * desconto / 100:.2f}")
print(f"Valor Produto Após Deconto: {preco_produto - (preco_produto * desconto / 100):.2f}")
