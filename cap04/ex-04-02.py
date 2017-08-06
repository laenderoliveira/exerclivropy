velocidade = int(input("Velocidade em Km/h: "))
if velocidade <= 80:
    print("Você não foi multado!")
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multato em R$%5.2f" % multa)
