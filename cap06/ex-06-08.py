l = [12, 34, 343, 56]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(l):
    if l[x] == p:
        break
    x += 1
if x < len(l):
    print("Achou {} na posição {}.".format(p, x))
else:
    print("{} não encontrado.".format(p))