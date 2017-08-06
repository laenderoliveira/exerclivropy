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
# Arquivo: exercicios_resolvidos\capitulo 02\exercicio-02-02.py
##############################################################################
# O resultado da expressão:
# 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# é 81.0
#
# Realizando o cálculo com as prioridades da página 39,
# efetuando apenas uma operação por linha,
# temos a seguinte ordem de cálculo:
# 0 --> 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# 1 --> 10 % 3 * 100     + 1 - 10 * 4 / 2
# 2 --> 1      * 100     + 1 - 10 * 4 / 2
# 3 -->          100     + 1 - 10 * 4 / 2
# 4 -->          100     + 1 - 40     / 2
# 5 -->          100     + 1 - 20
# 6 -->          101         - 20
# 7 -->                        81
#
# Se você estiver curioso(a) para saber por que o resultado
# é 81.0 e não 81, leia a seção 3.2, página 45.
# A operação de divisão sempre resulta em um número de ponto flutuante.

