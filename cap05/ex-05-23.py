#VERIFICAR SE NÚMERO É PRIMO
n = int(input("Digite um número: "))
if n % 2 == 0:
    c = 0
c = n - 2
while c >= 2:
    if n % c == 0:
        break
    c -= 2
if c == 1 or n == 2:
    print("É primo!")
else:
    print("Não é primo!")