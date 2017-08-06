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
# Arquivo: exercicios_resolvidos\capitulo 07\exercicio-07-01.py
##############################################################################
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

posição = primeira.find(segunda)

if posição == -1:
    print("'%s' não encontrada em '%s'" % (segunda, primeira))
else:
    print("%s encontrada na posição %d de %s"  % (segunda, posição, primeira ))

