listax = []
while True:
    n = int(input("Digite 1 número para adicionar na lista X: (0 para sair): "))
    if n == 0:
        break
    listax.append(n)
listay = []
while True:
    n = int(input("Digite 1 número para adicionar na lista Y: (0 para sair): "))
    if n == 0:
        break
    listay.append(n)
listaz = listax[:]
listaz.extend(listay)

x = 0
while x < len(listaz):
    print("({}) {}".format(x, listaz[x]))
    x += 1