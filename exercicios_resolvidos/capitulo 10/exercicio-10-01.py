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
# Arquivo: exercicios_resolvidos\capitulo 10\exercicio-10-01.py
##############################################################################
class Televisão:
	def __init__(self):
		self.ligada = False
		self.canal = 2
		self.tamanho = 20
		self.marca = "Ching-Ling"

tv = Televisão()
tv.tamanho = 27
tv.marca = "LongDang"
tv_sala = Televisão()
tv_sala.tamanho = 52
tv_sala.marca = "XangLa"

print("tv tamanho=%d marca=%s" % (tv.tamanho,tv.marca ))
print("tv_sala tamanho=%d marca=%s" % (tv_sala.tamanho,tv_sala.marca ))
