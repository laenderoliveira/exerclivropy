kwh = int(input("Quatidade de kWh: "))
instalacao = input("(R) Residencial, (C) Comercial, (I) Industrial? ")
if instalacao == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0,65
elif instalacao == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.65
elif instalacao == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Tipo de instalação inválida")
    preco = 0
print("Você pagará R$%5.2f" % (kwh * preco))

