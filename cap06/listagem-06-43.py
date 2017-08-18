compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for item in compras:
    print("{:20} {:5} x {:5} = {:5.2f}".format(item[0],
                                            item[1], item[2],
                                            item[1] * item[2]))
    soma += item[1] * item[2]
print("Total: {:6.2f}".format(soma))