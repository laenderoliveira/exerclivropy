l = [12, 3, 5, 1, 8]
tam_l = len(l)

for x in range(tam_l):
    trocou = False
    for i in range(tam_l-1):
        if l[i] < l[i+1]: # Inverter sinal da condição < para decrescente e > para crescente
            l[i], l[i+1] = l[i+1], l[i]
    if not trocou:
        break
print(l)