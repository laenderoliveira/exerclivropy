distancia = float(input("Distancia que deseja percorrer em Km: "))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5
print("O valor da passagem é de R$%5.2f" % preco)