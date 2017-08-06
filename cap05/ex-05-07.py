i = int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))
tab = int(input("Tabuada: "))

while i <= fim:
    print("%d X %d = %d" % (tab, i, tab * i))
    i += 1