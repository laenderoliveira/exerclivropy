LARGURA = int(input("Número de caracteres por linha: "))
LINHAS = int(input("Número de linhas por página: "))
NOME_DO_ARQUIVO = "lorem.txt"


def verifica_pagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodape = "= %s - Página: %d =" % (NOME_DO_ARQUIVO, pagina)
        arquivo.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina


def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")
    return verifica_pagina(arquivo, nlinhas+1, pagina)

entrada = open(NOME_DO_ARQUIVO, encoding="utf-8")
saida = open("saida_paginada.txt", "w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saida, linha, linhas, pagina)
            linha = ""
        linha += p + " "
    if linha != "":
        linhas, pagina = escreve(saida, linha, linhas, pagina)

# Para imprimir o número na última página
while linhas != 1:
    linhas, pagina = escreve(saida, "", linhas, pagina)

entrada.close()
saida.close()
