impares = open("impares.txt", "w")
pares = open("pares.txt", "w")
for n in range(1, 1001):
    if n % 2 == 0:
        pares.write("{}\n".format(n))
    else:
        impares.write("{}\n".format(n))
impares.close()
pares.close()
