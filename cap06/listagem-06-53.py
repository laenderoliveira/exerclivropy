estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]}

venda = [["tomate", 5], ["batata", 10], ["alface", 5]]

total = 0

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    estoque[produto][0] -= quantidade
    print("{:12s}: {:3d} x R${:6.2f} = R${:6.2f}".format(
        produto, quantidade, preco, custo
    ))
    total += custo
print("Custo total R${:5.2f}".format(total))
print("Estoque: \n")
print("Produto |Quantidade |Preço |")
for chave, dados in estoque.items():
    print("{:8s}|{:11}|{:6}|".format(chave, dados[0], dados[1]))