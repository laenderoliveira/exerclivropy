import sys

if len(sys.argv) < 2:
    print("\nUso: e09-09.py arquivo1 arquivo2 arquivo3 arquivoN\n")
    sys.exit()

saida = open("grande.txt", "w", encoding="utf-8")
for nome in sys.argv[1:]:
    arquivo = open(nome, "r")
    for linha in arquivo:
        saida.write(linha)
    arquivo.close()
saida.close()
