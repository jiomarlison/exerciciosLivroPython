tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50
          }
while True:
    produto = input("Digite o Nome do produto, ou FIM para sair: ")
    if produto.upper() == "FIM":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado")
print(tabela)