##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: exercicios_resolvidos\capitulo 09\exercicio-09-05.py
##############################################################################
pares = open("pares.txt","r")
saída = open("pares_invertido.txt","w")

L = pares.readlines()
L.reverse()
for l in L:
    saída.write(l)

pares.close()
saída.close()

# Observe que lemos todas as linhas antes de fazer a inversão
# Esta abordagem não funciona com arquivos grandes
# Alternativa usando with:
#
##with open("pares.txt","r") as pares, open("pares_invertido.txt","w") as saída:
##    L = pares.readlines()
##    L.reverse()
##    for l in L:
##        saída.write(l)
