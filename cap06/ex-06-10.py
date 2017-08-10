l = [12, 34, 343, 56]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0
achouP = -1
achouV = -1
primeiro = 0
while x < len(l):
    if l[x] == p:
        achouP = x
    if l[x] == v:
        achouV = x
    x += 1
if achouP != -1:
    print("p: {} foi encontrado na pos. {}!".format(p, achouP))
else:
    print("p: {} não enconrado!".format(p))
if achouV != -1:
    print("v: {} foi encontrado na pos. {}!".format(v, achouV))
else:
    print("v: {} não encontrado!".format(v))
if achouP != -1 and achouV != -1:
    if achouP < achouV:
        print("p foi encontrado primeiro")
    else:
        print("p foi encontrado primeiro")