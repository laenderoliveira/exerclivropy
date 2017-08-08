notas = [6, 7, 5, 8, 9]
soma = 0
i = 0
while i < 5:
    soma += notas[i]
    i += 1
print("Média: {:05.2f}".format(soma / i))