deposito = float(input("Depósito inicial: "))
mensal = float(input("Depósito mensal: "))
poupanca = deposito
taxa = float(input("Taxa de juros: "))
mes = 1
while mes <= 24:
    poupanca =  poupanca + (poupanca * (taxa / 100)) + mensal
    print("Mês %d, seu saldo é de R$%5.2f!" % (mes, poupanca))
    mes += 1
print("Em 24 meses rendeu R$%5.2f " % (poupanca - deposito))