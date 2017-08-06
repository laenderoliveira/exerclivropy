total = 0
while True:
    item = int(input("Digite o número do item: "))
    if item == 0:
        break
    preco = 0
    if item == 1:
        preco = 0.50
    elif item == 2:
        preco = 1.00
    elif item == 3:
        preco = 4.00
    elif item == 5:
        preco = 7.00
    elif item == 9:
        preco = 8.00
    else:
        print("Código inválido!")
    if preco != 0:
        qtd = int(input("Digite a quantidade: "))
        print("%d X R$%5.2f = R$%5.2f" % (qtd, preco, preco * qtd))
        total = total + (preco * qtd)
print("Total: R$%5.2f " %total)