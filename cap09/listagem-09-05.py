pares = open("pares.txt", "r")
mult4 = open("multiplos4.txt", "w")
for n in pares.readlines():
    if int(n) % 4 == 0:
        mult4.write("{}\n".format(n))
pares.close()
mult4.close()
