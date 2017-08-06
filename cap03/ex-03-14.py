km = float(input("KM percorridos: "))
dias = int(input("Quantidade de dias: "))
total = km * 0.15 + dias * 60
print("O valor total a pagar é de R$%5.2f" % total)
