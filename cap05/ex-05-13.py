divida = float(input("Valor da dívida: "))
saldo = divida
taxa = float(input("Juros mensal: "))
jurospago = 0
pagamento = float(input("Valor pago por mês: "))
mes = 1
while saldo > pagamento:
    juros = saldo * (taxa / 100)
    saldo = saldo + juros - pagamento
    jurospago = jurospago + juros
    print("O saldo da dívida do mês %d é de R$%5.2f" % (mes, saldo))
    mes = mes + 1
print("Voce vai demorar %d meses para quitar!" % (mes - 1))
print("Pagando R$%5.2f de juros" % jurospago)
print("Você tera um saldo haver de R$%5.2f " % (saldo))