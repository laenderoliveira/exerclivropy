entrada = open("entrada.txt")
LARGURA = 79

for linha in entrada.readlines():
    if linha.startswith(";"):
        continue
    elif linha.startswith(">"):
        print(linha[1:].rjust(LARGURA))
    elif linha.startswith("*"):
        print(linha[1:].center(LARGURA))
    elif linha.startswith("="):
        print("=" * 40)
    elif linha.startswith("."):
        input("Digite Enter para continuar: ")
    else:
        print(linha)
entrada.close()