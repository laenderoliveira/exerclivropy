cigarrosdia = int(input("Cigarros fumados por dia: "))
anos = float(input("Quantidade de anos fumados: "))
vidamenos = (cigarrosdia * 10 * 365 * anos) / 1440
print("Você tera %.2f dias a menos de vida" %vidamenos)
