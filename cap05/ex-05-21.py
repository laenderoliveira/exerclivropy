total = 0
contador = 0
while True:
    n = float(input("Digite um número ou 0 para sair: "))
    if n == 0:
        print("Você escolheu sair!")
        break
    total += n
    contador += 1
print("Total {}".format(total))
media = total / contador
print("Média {}".format(media))