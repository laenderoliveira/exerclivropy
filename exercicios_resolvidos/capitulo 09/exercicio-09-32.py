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
# Arquivo: exercicios_resolvidos\capitulo 09\exercicio-09-32.py
##############################################################################
import sys
import os.path

if len(sys.argv)<2:
	print("Digite o nome do arquivo ou diretório a verificar como parâmatro!")
	sys.exit(1)

nome = sys.argv[1]
if os.path.isdir(nome):
     print("O diretório %s existe." % nome)
elif os.path.isfile(nome):
	print ("O arquivo %s existe." % nome)
else:
     print("%s não existe." % nome)
