a = input("Primeira string: ")
b = input("Segunda string: ")
p = a.find(b)
if p != -1:
    print("{} encontrado no posição {} de {}".format(b, p, a))
