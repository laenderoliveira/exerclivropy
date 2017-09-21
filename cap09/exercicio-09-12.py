import sys

if len(sys.argv) != 2:
    print("\nUso: e09-09.py arquivo\n")
    sys.exit(1)
ocorencias = {}
arquivo = open(sys.argv[1])
for l, linha in enumerate(arquivo):
    palavras = linha.split()
    p = 1
    for palavra in palavras:
        palavra = palavra.strip(",.").lower()
        if palavra in ocorencias:
            ocorencias[palavra].append((l+1, p))
        else:
            ocorencias[palavra] = [(l+1, p)]
        p += len(palavra) + 1
arquivo.close()

for chave, valor in ocorencias.items():
    print("[{0}] = {1}".format(chave, valor))
