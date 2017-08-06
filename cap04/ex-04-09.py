casa = float(input("Valor da casa: "))
salario = float(input("Salário: "))
anos = int(input("Anos para quitar a casa: "))
casa_mes = casa / (anos * 12)
salario_mes = salario * 0.30
if casa_mes > salario_mes:
    print("O financiamento não foi aprovado")
else:
    print("O financiamento foi aprovado %d parcelas de R$%5.2f" % (anos * 12, casa_mes))