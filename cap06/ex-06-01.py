notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
i = 0
while i < 7:
    notas[i] = int(input("Digite sua nota {}: ".format(i+1)))
    i += 1
i = 0
while i < 7:
    print("Nota {}: {}".format(i+1, notas[i]))
    soma += notas[i]
    i += 1
print("Média: {}".format(soma / i))