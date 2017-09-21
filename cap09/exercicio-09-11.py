import sys

if len(sys.argv) != 2:
    print("\nUso: e09-09.py arquivo\n")
    sys.exit(1)
ocorencias = {}
arquivo = open(sys.argv[1])
for linha in arquivo:
    palavras = linha.split()
    for palavra in palavras:
        p = palavra.strip(",.").lower()
        ocorencias[p] = ocorencias.get(p, 0) + 1
arquivo.close()

for chave, valor in ocorencias.items():
    print("[{0}] = {1}".format(chave, valor))
