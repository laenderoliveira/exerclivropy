a = input("Primeira string: ")
b = input("Segunda string: ")
c = ""

for letra in a:
    if letra not in b and letra not in c:
        c += letra
print(c)
