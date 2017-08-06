total = 0
c = 0
while True:
    n = float(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    total += n
    c += 1
print("%03d números digitados" % c)
print("Média: %5.2f" % (total / c))
print("Total: %5.2f" % total)