questao = 1
pontos = 0
while questao <= 3:
    resp = input("Resposta da questão %d : " % questao)
    if questao == 1 and (resp == 'b' or resp == 'B'):
        pontos += 1
    if questao == 2 and (resp == 'a' or resp == 'A'):
        pontos += 1
    if questao == 3 and (resp == 'd' or resp == 'D'):
        pontos += 1
    questao += 1
print("Total de pontos:", pontos)