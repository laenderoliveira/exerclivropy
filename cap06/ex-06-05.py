ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    op = input("Digite A, F ou S: ")
    x = 0
    while x < len(op):
        if op[x] == 'A':
            if len(fila) > 0:
                r = fila.pop(0)
                print("Cliente {} atendido!\n".format(r))
            else:
                print("Não existe cliente na fila!\n")
        elif op[x] == "F":
            ultimo += 1
            fila.append(ultimo)
            print("Cliente {} entou na fila!\n".format(ultimo))
        elif op[x] == "S":
            break
        else:
            print("Somente A, F ou S\n")
        print("Existe {} cleintes na fila".format(len(fila)))
        x += 1