preco = float(input("Digite o preço: "))
p_desconto = float(input("Digite o % de desconto: "))
desconto = preco * p_desconto / 100
preco_final = preco - desconto
print("Desconto R$%5.2f" % desconto)
print("Preço final R$%5.2f" % preco_final)
