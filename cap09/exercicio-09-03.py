pares = open("pares.txt")
impares = open("impares.txt")
pareseimpares = open("pareseimpares.txt", "w")
numeros = []
numeros.extend(pares.readlines())
numeros.extend(impares.readlines())
numeros = [int(numero) for numero in numeros]  # Converte itens em inteiro
numeros.sort()
for row in numeros:
    pareseimpares.write("{}\n".format(row))
pares.close()
impares.close()
pareseimpares.close()
