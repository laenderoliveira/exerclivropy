parenteses = input("Insira os parenteses: ")
x = 0
pilha = []
while x < len(parenteses):
    if parenteses[x] == "(":
        pilha.append("(")
    elif parenteses[x] == ")":
        if len(pilha) > 0 and pilha[-1] == "(":
            t = pilha.pop(-1)
        else:
            pilha.append(")")
            break
    x += 1

if len(pilha) == 0:
    print("{:10} OK".format(parenteses))
else:
    print("{:10} Erro".format(parenteses))