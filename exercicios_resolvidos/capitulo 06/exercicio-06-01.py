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
# Arquivo: exercicios_resolvidos\capitulo 06\exercicio-06-01.py
##############################################################################
notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 7:
     notas[x] = float(input("Nota %d:" % x))
     soma += notas[x]
     x += 1
x = 0
while x < 7:
     print("Nota %d: %6.2f" % (x, notas[x]))
     x += 1
print("Média: %5.2f" % (soma/x))
