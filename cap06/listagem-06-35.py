lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1:
        print("Sala inválida!")
    elif lugares_vagos[sala-1] == 0:
        print("Desculpe, sala lotada!")
    else:
        print("{} lugares vagos".format(lugares_vagos[sala-1]))
        lugares = int(input("Quantos lugares você deseja? "))
        if lugares > lugares_vagos[sala-1]:
            print("Esse nḿero de lugares não está disponível")
        elif lugares < 0:
            print("Número inválido!")
        else:
            lugares_vagos[sala-1] -= lugares
            print("{} lugares vendidos".format(lugares))

print("-="*10)
print("Utilização das salas: ")
print("-="*10)
for i, x in enumerate(lugares_vagos):
    print("Sala [{:}] - {:03} lugar(es) vazio(s)".format(i+1, x))