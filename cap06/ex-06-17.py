estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]}

total = 0

while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            estoque[produto][0] -= quantidade
            preco = estoque[produto][1]
            print("{:12s} {:5} x {:4} = {:5.2f}".format(produto, quantidade, preco, preco*quantidade))
            total += preco * quantidade
        else:
            print("Estoque disponível: {}.".format(estoque[produto][0]))
    else:
        print("Produto não encontrado!")
print("Total R${:5.2f}".format(total))