l = [12, 34, 343, 56]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(l):
    if l[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if l[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print("{} foi encontrado!".format(p))
else:
    print("{} não enconrado!".format(p))
if achouV:
    print("{} foi encontrado".format(v))
else:
    print("{} foi encontrado!".format(v))
if primeiro == 1:
    print("{} foi encontrado primeiro!".format(p))
elif primeiro == 2:
    print("{} foi encontrado primeiro!".format(v))