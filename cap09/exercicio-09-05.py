pares = open("pares.txt", "r")
saida = open("saida_pares.txt", "w")

# l = pares.readlines()
# l.reverse()
for linha in pares.readlines()[::-1]:
    saida.write(linha)

saida.close()
pares.close()