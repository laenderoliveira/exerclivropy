l = [7, 4, 3, 12, 8]
tam_l = len(l)

for i in range(tam_l):
    trocou = False
    for j in range(tam_l-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            trocou = True
    if not trocou:
        break
print(l)