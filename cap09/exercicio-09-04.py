import sys


if len(sys.argv) != 3:
    print("Uso: python ex09-04 primeiro.txt segundo.txt")
else:
    primeiro = open(sys.argv[1], "r")
    segundo = open(sys.argv[2], "r")
    saida = open("saida.txt", "w")
    for l1 in primeiro:
        saida.write(l1)
    for l2 in segundo:
        saida.write(l2)
    saida.close()
    primeiro.close()
    segundo.close()