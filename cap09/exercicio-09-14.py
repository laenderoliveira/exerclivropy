arquivo = open("lorem.txt")
saida = open("saida.txt", "w")


for linha in arquivo:
    if linha != "\n":
        palavras = linha.split()
        for palavra in palavras:
            if palavra == "":
                print("a")
            palavra = palavra.strip()
            saida.write(palavra+" ")
        saida.write("\n")
arquivo.close()
saida.close()