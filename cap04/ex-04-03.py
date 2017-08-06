a = int(input("1°: "))
b = int(input("2°: "))
c = int(input("3°: "))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

print("Maior:", maior)
print("Menor:", menor)
