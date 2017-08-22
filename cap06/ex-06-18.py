palavra = input("Digite a palavra: ")
c = {}
for letra in palavra:
    if letra in c:
        c[letra] += 1
    else:
        c[letra] = 1

for l, x in c.items():
    print("[{}] = {}".format(l, x))
