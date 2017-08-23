x = input("String: ")
c = {}
for letra in x:
    if letra in c:
        c[letra] += 1
    else:
        c[letra] = 1

for l in c:
    print("{}: {}x".format(l, c[l]))
