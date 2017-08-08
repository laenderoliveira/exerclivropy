num = int(input("Digite o número para verificar se é palimdromo: "))
pal = num
nov = ''
while pal != 0:
    nov += str(pal % 10)
    pal //= 10
if num == int(nov):
    print("{} é palímdromo".format(nov))
else:
    print("{} não é palimdromo".format(num))

'''
s = input ("Digite o número a verificar, sem espaços:")
i = 0
f = len(s)-1 # posição do último caracter da string
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print("%s é palíndromo" % s)
else:
    print("%s não é palíndromo" % s)
'''