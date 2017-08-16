v = [12, 34, 56, 67, 54, 12, 12, 52, 4, 345, 2]
p = []
i = []
for x in v:
    if x % 2 == 0:
        p.append(x)
    else:
        i.append(x)

print("Pares", p)
print("Impares", i)
