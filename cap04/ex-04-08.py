a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
op = input("Digite a operação (*) (/) (+) (-) : ")
if op == '*':
    res = a * b
elif op == '/':
    res = a / b
elif op == "+":
    res = a + b
elif op == '-':
    res = a - b
else:
    print("Operação inválida!")
    res = 0
print("Resutado: %5.2f" % res)
