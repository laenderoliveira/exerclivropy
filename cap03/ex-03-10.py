salario = float(input("Salario: "))
p_aumento = float(input("Aumento%: "))
aumento = (salario * p_aumento / 100)
novo_salario = salario + aumento
print("O aumento foi de R$%5.2f e seu novo salário é de R$%5.2f" % (aumento, novo_salario))
