a = input("Primeira string: ")
b = input("Segunda string: ")
c = ""
for l in b:
    if l in a and l not in c:
        c += l
print(c)
