salario = float(input("Salário: "))
aumento = 0.10
if salario <= 1250:
    aumento = 0.15
print("Seu salário era de R$%5.2f" % salario)
print("Terá um aumento de R$%5.2f" % (salario * aumento))
