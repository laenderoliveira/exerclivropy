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
# Arquivo: exercicios_resolvidos\capitulo 10\exercicio-10-02.py
##############################################################################
class Televisão:
     def __init__(self, canal_inicial, min, max):
         self.ligada = False
         self.canal = canal_inicial
         self.cmin = min
         self.cmax = max
     def muda_canal_para_baixo(self):
         if(self.canal-1 >= self.cmin):
               self.canal -= 1
     def muda_canal_para_cima(self):
         if(self.canal+1 <= self.cmax):
               self.canal += 1
tv=Televisão(5,1,99)

print(tv.canal)
