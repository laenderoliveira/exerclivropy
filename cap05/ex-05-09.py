dividendo = int(input("Digite o primeiro número: "))
divisor = int(input("Digite o segundo número: "))
x = dividendo
quociente = 0
while divisor <= x:
    x -= divisor
    quociente +=1
resto = x
print("%d / %d = %d" %(dividendo, divisor, quociente))
print("Resto: %d" % resto)
