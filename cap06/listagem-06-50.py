tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50}

while True:
    prod = input("Nome do produto: ")
    if prod == "fim":
        break
    if prod in tabela:
        print("Preço R${:5.2f}".format(tabela[prod]))
    else:
        print("Produto não encontrado!")