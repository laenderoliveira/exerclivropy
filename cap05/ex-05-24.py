p = int(input("Digite N primeiros números primos: "))
conta_primos = 0
n = 0
c = n - 2
while conta_primos < p:
    if n % 2 == 0:
        c = 0
    c = n - 2
    while c >= 2:
        if n % c == 0:
            break
        c -= 2
    if c == 1 or n == 2:
        print("{} É primo!".format(n))
        conta_primos += 1
    n += 1