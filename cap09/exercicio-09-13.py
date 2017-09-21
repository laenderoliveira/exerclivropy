import sys


if len(sys.argv) != 4:
    print("Uso: e9-13.py arquivo.txt inicio fim")
    sys.exit(1)
nome = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3]) + 1
arquivo = open(nome)
linhas = arquivo.readlines()
for linha in linhas[inicio:fim]:
    print(linha, end="")
arquivo.close()