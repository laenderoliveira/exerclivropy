num = int(input("Digite o número: "))
div = int(input("Digite o número para calcular o resto da divisão: "))
resto = num
while resto >= div:
    resto -= div
print("O resto da divisão de {} / {} é {}".format(num, div, resto))