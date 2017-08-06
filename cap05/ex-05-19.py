valor = float(input("Digite o valor: "))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if apagar >= 1:
            print("%d cédulas de R$%5.2f" % (cedulas, atual))
        else:
            print("%d moedas de R$%5.2f" % (cedulas, atual))
        if apagar < 0.01:
            print("1 moedas de R$ 0.01")
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0